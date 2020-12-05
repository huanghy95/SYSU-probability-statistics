import numpy as np
import string
class Compress:
    #初始化变量
    def __init__(self):
        self.left=0.0#左区间
        self.right=1.0#右区间
        self.last=''#上一个字符
        self.cnt={}#字典
        self.total=256
        #初始化字典(每个出现一次,方便计算概率)
        for i in range(self.total):
            self.cnt[chr(i)]=1
            for j in range(self.total):
                self.cnt[chr(i)+chr(j)]=1
        #初始化一阶概率的左右端点
        self.lp1=np.zeros(self.total)
        self.rp1=np.zeros(self.total)
        #初始化二阶概率的左右端点
        self.lp2=np.zeros(self.total*self.total)
        self.rp2=np.zeros(self.total*self.total)
        self.update()

    #读取一个字符(TODO)
    def read(self,c):
        diff=self.right-self.left
        self.right=self.left+diff*self.rp1[c]
        self.left=self.left+diff*self.lp1[c]
        self.cnt[c]+=1
        if self.last!='':
            self.cnt[self.last+c]+=1
        self.last=c

    #更新字典
    def update(self):
        #计数
        cur=0
        for i in range(self.total):
            self.rp1[cur]=(0 if cur==0 else self.rp1[cur-1])+self.cnt[chr(i)]
            cur+=1
        cur=0
        for i in range(self.total):
            for j in range(self.total):
                self.rp2[cur]=(0 if cur==0 else self.rp2[cur-1])+self.cnt[chr(i)+chr(j)]
                cur+=1
        #计算
        total1=self.rp1[self.total-1]
        self.rp1/=total1
        total2=self.rp2[self.total*self.total-1]
        self.rp2/=total2
        self.lp1[1:self.total]=self.rp1[0:self.total-1]
        self.lp2[1:self.total*self.total]=self.rp2[0:self.total*self.total-1]

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



