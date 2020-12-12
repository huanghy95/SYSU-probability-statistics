import numpy as np
import gmpy2
import os
from tqdm import tqdm

class Decompress:
    #初始化变量
    def __init__(self):

        gmpy2.get_context().precision = 1000  # gmpy2精度
        self.left = gmpy2.mpfr(0.0)  # 左区间
        self.right = gmpy2.mpfr(1.0)  # 右区间
        self.readData = gmpy2.mpz(0)  # 最大相同次数
        self.total = 256  # 计算的ascii码表大小
        self.cnt1 = np.zeros(self.total)  # 字典
        self.finish = 0  # 当前轮次读了多少数字

        #初始化字典(每个出现一次,方便计算概率)
        for i in range(self.total):
            self.cnt1[i] = 1

        #初始化概率的左右端点
        self.lp1 = np.zeros(self.total)
        self.rp1 = np.zeros(self.total)
        for i in range(self.total):
            self.rp1[i] = (1 if i == 0 else self.rp1[i - 1] + self.cnt1[i])
        tmp = self.rp1[self.total - 1]
        self.rp1 /= tmp
        self.lp1[1:self.total] = self.rp1[0:self.total - 1]

    #更新字典
    def update_table(self, c):
        #字符数+1
        self.cnt1[ord(c)] = self.cnt1[ord(c)] + 1

        #重新计算字典
        for i in range(self.total):
            self.rp1[i] = (self.cnt1[0] if i ==
                           0 else self.rp1[i - 1] + self.cnt1[i])
        tmp = self.rp1[self.total - 1]
        self.rp1 /= tmp
        self.lp1[1:self.total] = self.rp1[0:self.total - 1]

    #判断字典的当前字符是否满足要求
    def check(self, i):
        #区间大小
        diff = self.right - self.left

        #新的左右区间
        curleft = self.left + diff * self.lp1[i]
        curright = self.left + diff * self.rp1[i]

        #读取的数转化为小数
        decimal = gmpy2.mpfr(self.cur / self.log10)
        decimal = decimal - gmpy2.floor(decimal)

        #判断是否满足要求
        if curleft > decimal:
            return False
        if curright < decimal:
            return False

        #更新区间
        self.left = curleft
        self.right = curright

        #通过decimal计算新的cur，抛弃掉cur前导多余数字，cur维持为整数防止精度缺失
        self.cur = decimal*self.log10
        self.cur = gmpy2.rint_round(self.cur)
        return True

    #更新cur,将多余的cur前导数字消除
    def update_cur(self):
        while True:
            #抛弃left和right相同的部分
            leftInt = int(self.left*10)
            rightInt = int(self.right*10)
            if leftInt == rightInt:
                self.left = self.left*10-leftInt
                self.right = self.right*10-rightInt
                self.cur *= 10
                self.finish += 1
                #持续更新未更新的数位
                if (len(self.readData) != 0):
                    self.cur += ord(self.readData[0]) - 48
                    self.readData = self.readData[1:]
            else:
                break

    #计算字符
    def get_c(self):
        c = chr(49)

        #遍历表进行判断
        for i in range(self.total):
            if self.check(i):
                c = chr(i)
                break

        #更新表和cur
        self.update_table(c)
        self.update_cur()
        return c

    #解压
    def unziptxt(self, inputFile, outputFile):
        print("Decompressing")
        #读取二进制文件
        with open("./"+inputFile, "rb") as readFile:
            while True:
                i = readFile.read(1)
                if not i:
                    break
                i = int.from_bytes(i, byteorder='big', signed=False)
                self.readData *= 256
                self.readData += i

        #将其转化为十进制
        self.readData = self.readData.digits(10)

        #消除最前的1
        self.readData = self.readData[1:]

        #总长度
        size = len(self.readData)

        #cur表示当前需要运算的大整数
        self.cur = gmpy2.mpfr(1.0)

        #log10表示大整数的数位
        self.log10 = gmpy2.mpfr(1.0)

        #初始化
        self.len = min(100, len(self.readData))  # 最多为cur读取100位进行运算
        self.finish = self.len

        #更新cur和log10
        for i in range(self.len):
            self.log10 *= 10
        for i in range(self.len):
            self.cur *= 10
            self.cur += ord(self.readData[0]) - 48
            self.readData = self.readData[1:]

        #计算字符并写文件
        with tqdm(total=size) as pbar:
            with open("./"+outputFile, "w") as writeFile:
                while True:
                    c = self.get_c()
                    pbar.update(self.finish)
                    self.finish = 0
                    #末尾的结束标记
                    if c == chr(8):
                        break
                    writeFile.write(c)

        print("the size of the compressd file:" +
              str(os.path.getsize(inputFile))+" bytes")
        print("the size of the source file:" +
              str(os.path.getsize(outputFile))+" bytes")
