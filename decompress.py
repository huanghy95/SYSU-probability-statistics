import numpy as np
import gmpy2
import os
import string
import math
import utils
class Decompress:
    #初始化变量
    def __init__(self):
        gmpy2.get_context().precision = 1000
        self.left=gmpy2.mpfr(0.0)#左区间
        self.right=gmpy2.mpfr(1.0)#右区间
        self.readData=gmpy2.mpz(0)#最大相同次数
        # self.last=-1#上一个字符的ascii码
        self.total=256
        self.cnt1=np.zeros(self.total)
        # self.cnt2=np.zeros(self.total*self.total)#字典
        #初始化字典(每个出现一次,方便计算概率)
        for i in range(self.total):
            self.cnt1[i]=1
            # for j in range(self.total):
            #     self.cnt2[i*self.total+j]=1
        #初始化一阶概率的左右端点
        self.lp1=np.zeros(self.total)
        self.rp1=np.zeros(self.total)
        for i in range(self.total):
            self.rp1[i] = (1 if i == 0 else self.rp1[i - 1] + self.cnt1[i])
        tmp = self.rp1[self.total - 1]
        self.rp1 /= tmp 
        self.lp1[1:self.total] = self.rp1[0:self.total - 1]
        # 不整二阶
        # #初始化二阶概率的左右端点
        # self.lp2=np.zeros(self.total*self.total)
        # self.rp2=np.zeros(self.total*self.total)
        # utils.update(self.lp1,self.rp1,self.cnt1,self.total)

    def update_table(self, c):
        self.cnt1[ord(c)] = self.cnt1[ord(c)] + 1
        for i in range(self.total):
            self.rp1[i] = (self.cnt1[0] if i == 0 else self.rp1[i - 1] + self.cnt1[i])
        tmp = self.rp1[self.total - 1]
        self.rp1 /= tmp 
        self.lp1[1:self.total] = self.rp1[0:self.total - 1]

    def check(self, i):
        diff = self.right - self.left
        curleft = self.left + diff * self.lp1[i]
        curright = self.left + diff * self.rp1[i]
        qwq = self.cur / self.log10
        qwq = qwq - gmpy2.floor(qwq)
        # print(curleft)
        # print(qwq)
        # print(curright)
        if curleft > qwq:
            return False
        if curright < qwq:
            return False 
        self.left = curleft
        self.right = curright
        return True

    def update_cur(self):
        while True:
            leftInt=int(self.left*10)
            rightInt=int(self.right*10)
            if leftInt==rightInt:
                self.left=self.left*10-leftInt
                self.right=self.right*10-rightInt
                if (len(self.readData) != 0):
                    self.cur *= 10
                    self.cur += ord(self.readData[0]) - 48
                    self.readData = self.readData[1:]
            else: 
                break

    def get_c(self):
        c = chr(49)
        for i in range(self.total):
            if self.check(i):
                c = chr(i)
                break
        self.update_table(c)
        self.update_cur()
        print(self.left)
        print(self.right)
        return c

    #解压
    def unziptxt(self,inputFile,outputFile):
        with open("./"+inputFile,"rb") as readFile:
            while True:
                i = readFile.read(1)
                if not i:
                    break
                i = int.from_bytes(i, byteorder='big', signed=False)
                # print(i)
                self.readData *= 256
                self.readData += i
        self.readData = self.readData.digits(10)
        # print(self.readData)
        self.readData = self.readData[1:]#cut the first sign position
        self.cur = gmpy2.mpfr(1.0)
        self.log10 = gmpy2.mpfr(1.0)
        self.len = min(100, len(self.readData))
        for i in range(self.len):
            self.log10 *= 10
        for i in range(self.len):
            self.cur *= 10
            self.cur += ord(self.readData[0]) - 48
            self.readData = self.readData[1:]
        with open("./"+outputFile,"w") as writeFile:
            while len(self.readData) != -1:
                c = self.get_c()
                writeFile.write(c)


        print("the size of the inputfile:"+str(os.path.getsize(inputFile))+" byte")
        print("the size of the outputfile:"+str(os.path.getsize(outputFile))+" byte")

