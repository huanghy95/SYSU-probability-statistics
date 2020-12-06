import numpy as np
import os
import string
import math
import utils
class Compress:
    #初始化变量
    def __init__(self):
        self.left=0.0#左区间
        self.right=1.0#右区间
        self.writeData=0#最大相同次数
        self.last=-1#上一个字符的ascii码
        self.total=256
        self.cnt1=np.zeros(self.total)
        self.cnt2=np.zeros(self.total*self.total)#字典
        #初始化字典(每个出现一次,方便计算概率)
        for i in range(self.total):
            self.cnt1[i]=1
            for j in range(self.total):
                self.cnt2[i*self.total+j]=1
        #初始化一阶概率的左右端点
        self.lp1=np.zeros(self.total)
        self.rp1=np.zeros(self.total)
        #初始化二阶概率的左右端点
        self.lp2=np.zeros(self.total*self.total)
        self.rp2=np.zeros(self.total*self.total)
        utils.update(self)


    #计算可写入文件数字
    def generateWriteData(self):
        bits=0
        while True:
            leftInt=int(self.left*10)
            rightInt=int(self.right*10)
            if leftInt==rightInt:
                self.writeData*=10
                self.writeData+=leftInt
                self.left=self.left*10-leftInt
                self.right=self.right*10-rightInt
                bits+=1
            else: 
                self.writeData/=bits
                return bits

    #压缩(TODO)
    def ziptxt(self,inputFile,outputFile):
        with open("./"+inputFile,"r") as readFile:
            with open("./"+outputFile,"wb") as writeFile:
                lines=0
                for line in readFile:
                    for c in line:
                        utils.read(self,c)
                        bits=self.generateWriteData()
                        if bits:
                            # print(self.writeData)
                            # print("write into file "+str(self.writeData)+" "+str(bytes(self.writeData.to_bytes(1,byteorder='big',signed=True))))
                            writeFile.write(self.writeData.to_bytes(1,byteorder='big',signed=True))
                            self.writeData=0
                    lines+=1
                    print("finish "+ str(lines) +" lines")
                # while self.left:
                #     leftInt=int(self.left*10)
                #     self.left=self.left*10-leftInt
                #     writeFile.write(leftInt.to_bytes(1,byteorder='big',signed=True))
        print("the size of the inputfile:"+str(os.path.getsize(inputFile))+" byte")
        print("the size of the outputfile:"+str(os.path.getsize(outputFile))+" byte")

