import numpy as np
import gmpy2
import os
class Decompress:
    #初始化变量
    def __init__(self):
        self.left=0.0#左区间
        self.right=1.0#右区间
        self.writeData=gmpy2.mpz(0)#最大相同次数
        self.maxCharDigits = 16 #规定个字符可能出现次数的二进制位数，字符表将占用32*maxCharDigits个Byte
        self.total=256
        self.cnt=np.zeros(self.total)
        self.cntSum=0 #字符总数
        #初始化一阶概率的左右端点
        self.lp=np.zeros(self.total)
        self.rp=np.zeros(self.total)

    #算出静态字典
    def generateDict(self,inputFile):
        with open("./"+inputFile,"rb") as readFile:
            for i in range(256):
                self.cnt[i]=int.from_bytes(readFile.read(2),byteorder = 'big')
                self.cntSum+=self.cnt[i]
        print(self.cnt)

    #读取每个字符并转换为区间
    def transform(self,c):
        diff = self.right-self.left
        self.right = self.left + diff * self.rp[ord(c)]
        self.left = self.left + diff * self.lp[ord(c)]

    #压缩(TODO)
    def unziptxt(self,inputFile,outputFile):
        self.generateDict(inputFile)
        pass

