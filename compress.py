import numpy as np
import gmpy2
import os
import string
import math
import utils
class Compress:
    #初始化变量
    def __init__(self):
        gmpy2.get_context().precision = 1000
        self.left=gmpy2.mpfr(0.0)#左区间
        self.right=gmpy2.mpfr(1.0)#右区间
        self.writeData=gmpy2.mpz(1)#最大相同次数
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


    def read(self, c):
        diff = self.right - self.left
        self.right = self.left + diff * self.rp1[ord(c)]
        self.left = self.left + diff * self.lp1[ord(c)]
        self.update_table(c)


    #计算可写入文件数字
    def generateWriteData(self):
        while True:
            leftInt=int(self.left*10)
            rightInt=int(self.right*10)
            if leftInt==rightInt:
                self.writeData*=10
                self.writeData+=leftInt
                self.left=self.left*10-leftInt
                self.right=self.right*10-rightInt
            else: 
                break

    #压缩
    def ziptxt(self,inputFile,outputFile):
        with open("./"+inputFile,"r") as readFile:
            with open("./"+outputFile,"wb") as writeFile:
                writeFile.write(os.path.getsize(inputFile).to_bytes(4, byteorder = 'big', signed = False));
                lines=0
                for line in readFile:
                    for c in line:
                        self.read(c)
                        # print("left",str(self.left))
                        # print("right",str(self.right))
                        self.generateWriteData()
                    lines+=1
                self.writeData*=10
                self.writeData+=int(self.right*10)
                self.right=self.right*10-int(self.right*10)
                # print("self.writeData",str(self.writeData))
                while(len(self.writeData.digits(2)) %8 != 0):
                    self.writeData*=10
                    self.writeData+=int(self.right*10)
                    self.right=self.right*10-int(self.right*10)
                # print(self.writeData.digits())
                bit = self.writeData.digits(2)
                # print("bit ",bit)
                while len(bit) >= 8:
                    qwq = int(bit[0:8],2)
                    # print(qwq)
                    writeFile.write(qwq.to_bytes(1, byteorder = 'big', signed = False));
                    bit = bit[8:]
                # print('********')
                # print(len(bit))
                # if len(bit) != 0:
                #     qwq = int(bit, 2)
                #     qwq <<= 8 - len(bit)
                #     writeFile.write(qwq.to_bytes(1, byteorder = 'big', signed = False));

        print("the size of the inputfile:"+str(os.path.getsize(inputFile))+" byte")
        print("the size of the outputfile:"+str(os.path.getsize(outputFile))+" byte")

