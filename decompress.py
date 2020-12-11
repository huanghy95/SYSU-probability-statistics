import numpy as np
import gmpy2
import os
class Decompress:
    #初始化变量
    def __init__(self):
        self.left=gmpy2.mpz(0)#左区间
        self.right=gmpy2.mpz(0)#右区间
        self.readData=gmpy2.mpz(0)#最大相同次数
        self.maxCharDigits = 16 #规定个字符可能出现次数的二进制位数，字符表将占用32*maxCharDigits个Byte
        self.total=256
        self.cnt=np.zeros(self.total)
        self.cntSum=0 #字符总数
        self.minCnt = -1 #最小字符数
        self.foot = 0.0 #最小步长
        #初始化一阶概率的左右端点
        self.lp=np.zeros(self.total)
        self.rp=np.zeros(self.total)

    #算出静态字典以及最小步长
    def generateDict(self,inputFile):
        with open("./"+inputFile,"rb") as readFile:
            for i in range(256):
                self.cnt[i]=int.from_bytes(readFile.read(2),byteorder = 'big')
                if self.cnt[i] == 0:
                    continue
                if self.minCnt == -1:
                    self.minCnt = self.cnt[i]
                else:
                    self.minCnt = (self.minCnt if self.minCnt < self.cnt[i] else self.cnt[i])
                self.cntSum+=self.cnt[i]
        self.foot = self.minCnt * 1.0 / self.cntSum 
        print(self.cnt)
        print(self.cntSum)
        print(self.minCnt)
        print(self.foot)

    #还原区间表
    def generateChart(self):
        cur = 0
        for i in range(self.total):
            self.rp[cur] = (0 if cur == 0 else self.rp[cur - 1]) + self.cnt[i]
            cur += 1
        total1 = self.rp[self.total-1]
        self.rp /= total1
        self.lp[1:self.total]=self.rp[0:self.total-1]
        print(self.lp)
        print(self.rp)

    #根据值落在哪个区间转换为字符,并同时更新区间上下限
    def transform(self,c):
        diff = self.right-self.left
        num = self.readData / diff
        for i in range(self.total):
            if num >= self.lp[i]:
                c = chr(i)
                self.right = self.left + diff * self.rp[i]
                self.left = self.left + diff * self.lp[i]
                break


    #读取编码后的数字（高精度大整数）到readData中(TODO)
    def getData(self, inputFile):
        with open("./"+inputFile,"rb") as readFile:
            pass

    #读取每个字符并转换为区间
    def transform(self,c):
        diff = self.right-self.left
        self.right = self.left + diff * self.rp[ord(c)]
        self.left = self.left + diff * self.lp[ord(c)]

    #压缩(TODO)
    def unziptxt(self,inputFile,outputFile):
        self.generateDict(inputFile)
        self.generateChart()
        #读取编码后的数字（高精度大整数）到readData中
        #self.getData(self,inputFile)
        pass

