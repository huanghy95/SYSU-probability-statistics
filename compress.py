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
        self.nums=np.array([])#记录概率的每位数字
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
        utils.update(self.lp1,self.rp1,self.cnt1,self.total)
        utils.update(self.lp2,self.rp2,self.cnt2,self.total*self.total)

    #计算可写入文件数字
    def generateWriteData(self):
        while self.left or self.right:
            leftInt=int(self.left*10)
            rightInt=int(self.right*10)
            # print(str(self.left),',',str(self.right))
            # print(str(leftInt),',',str(rightInt))
            if leftInt==rightInt:
                self.left=self.left*10-leftInt
                self.right=self.right*10-rightInt
                self.nums=np.append(self.nums,leftInt)
            else: 
                break

    #压缩(TODO)
    def ziptxt(self,inputFile,outputFile):
        with open("./"+inputFile,"r") as readFile:
            with open("./"+outputFile,"wb") as writeFile:
                lines=0
                for line in readFile:
                    for c in line:
                        utils.read(self,c)
                        # print("reading ",c)
                        self.generateWriteData()
                    lines+=1
                    print("finish "+ str(lines) +" lines")
                while self.left:
                    leftInt=int(self.left*10)
                    self.left=self.left*10-leftInt
                    self.nums=np.append(self.nums,leftInt)
                bins=utils.float2bin(self.nums)
                hexs=utils.bin2hex(bins)
                # print(self.nums[0])
                # print(bins[0])
                # print(hexs[0])
                # print("the nums")
                # for i in self.nums:
                #     print(int(i),end='')
                # print('')
                # print("the binary code")
                # for i in bins:
                #     print(i,end='')
                # print('')
                # print("the hex code")
                # for i in hexs:
                #     print(i,end='')
                for i in hexs:
                    writeFile.write(int(i).to_bytes(1,byteorder='big',signed=True))
                # while self.left:
                #     leftInt=int(self.left*10)
                #     self.left=self.left*10-leftInt
                #     writeFile.write(leftInt.to_bytes(1,byteorder='big',signed=True))
        print("the size of the inputfile:"+str(os.path.getsize(inputFile))+" byte")
        print("the size of the outputfile:"+str(os.path.getsize(outputFile))+" byte")

