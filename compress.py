import numpy as np
import string
class Compress:
    #初始化变量
    def __init__(self):
        self.left=0.0#左区间
        self.right=1.0#右区间
        self.last=" "#上一个字符
        self.cnt={}#字典
        #初始化字典(每个出现一次,方便计算概率)
        for first in string.ascii_lowercase:
            self.cnt[first]=1
            for second in string.ascii_lowercase:
                self.cnt[first+second]=1
        #初始化总数
        self.total1=256
        self.total2=65536
        #初始化概率的左右端点
        self.lp1=np.zeros(256)
        self.rp1=np.zeros(256)

    #读取一个字符(TODO)
    def read(self,c):
        diff=self.right-self.left
        self.right=self.left+diff*self.rp1[c]
        self.left=self.left+diff*self.lp1[c]
        self.cnt[c]+=1
        self.cnt[self.last+c]+=1
        self.last=c
        self.total1+=1
        if self.total1>1:
            self.total2+=1

    #更新字典(TODO)
    def update(self):
        pass

    #读取文件(TODO)
    def readFile(self,inputFile):
        with open("./"+inputFile,"r") as file:
            for line in file:
                for c in line:
                    self.read(c)

    #写文件(TODO)
    def writeFile(self,outputFile):
        with open("./"+outputFile,"wb") as file:
            file.write("TODO")

    #压缩(TODO)
    def ziptxt(self,filename):
        pass



