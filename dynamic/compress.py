import numpy as np
from gmpy2 import mpz, mpfr, get_context
from os import path
from tqdm import tqdm


class Compress:
    #初始化变量
    def __init__(self):
        get_context().precision = 1000  # gmpy2的精度
        self.left = mpfr(0.0)  # 左区间
        self.right = mpfr(1.0)  # 右区间
        self.writeData = mpz(1)  # 最大相同次数
        self.total = 256  # 计算ascii码表的大小
        self.cnt1 = np.zeros(self.total)  # 字典
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

    #读取字符
    def read(self, c):
        #更新区间
        diff = self.right - self.left
        self.right = self.left + diff * self.rp1[ord(c)]
        self.left = self.left + diff * self.lp1[ord(c)]

        #更新字典
        self.update_table(c)

    #计算可写入文件数字

    def generateWriteData(self):
        while True:
            leftInt = int(self.left*10)
            rightInt = int(self.right*10)

            #left和right相同部分写入文件
            if leftInt == rightInt:
                #更新writeData
                self.writeData *= 10
                self.writeData += leftInt
                #更新left和right
                self.left = self.left*10-leftInt
                self.right = self.right*10-rightInt
            else:
                break

    #压缩
    def ziptxt(self, inputFile, outputFile):
        lines = sum([1 for i in open("./"+inputFile, "r")])
        print("Compressing")
        #读取文件
        with open("./"+inputFile, "r") as readFile:
            with open("./"+outputFile, "wb") as writeFile:
                for line in tqdm(readFile, total=lines):
                    for c in line:
                        self.read(c)
                        self.generateWriteData()

                #末尾加上退格符当做结束标记
                self.read(chr(8))
                self.generateWriteData()

                #在left和right第一位不同部分选择用right的数位写入，保证writeData在left和right之间
                self.writeData *= 10
                self.writeData += int(self.right*10)
                self.right = self.right*10-int(self.right*10)

                #如果二进制表示不是8的整数则多取一位right的数值
                while(len(self.writeData.digits(2)) % 8 != 0):
                    self.writeData *= 10
                    self.writeData += int(self.right*10)
                    self.right = self.right*10-int(self.right*10)

                #二进制表示
                bit = self.writeData.digits(2)

                #8位8位写入文件
                while len(bit) >= 8:
                    qwq = int(bit[0:8], 2)
                    writeFile.write(qwq.to_bytes(
                        1, byteorder='big', signed=False))
                    bit = bit[8:]

        print("the size of the source file:" +
              str(path.getsize(inputFile))+" bytes")
        print("the size of the compressd file:" +
              str(path.getsize(outputFile))+" bytes")
        print("the compression ratio:%.2lf%%" %
              (100*path.getsize(outputFile)/path.getsize(inputFile)))
