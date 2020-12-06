import numpy as np
import os
import string
import math
import utils
class Decompress:
    #初始化变量
    def __init__(self):
        self.left=0.0#左区间
        self.right=1.0#右区间
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
        utils.update(self.lp1,self.rp1,self.cnt1,self.total)

    #计算生成的字符
    def generateChar(self):
        pass

    #解压(TODO)
    def ziptxt(self,inputFile,outputFile):
        with open("./"+inputFile,"r") as readFile:
            with open("./"+outputFile,"wb") as writeFile:
                pass
