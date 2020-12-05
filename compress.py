import numpy as np
import string
class Compress:
    #初始化变量
    def __init__(self):
        self.left=0.0#左区间
        self.right=1.0#右区间
        self.writeData=0#最大相同次数
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
        self.update(initialize=True)

    #读取一个字符
    def read(self,c):
        diff=self.right-self.left
        #读取第一个数字
        if self.last=='':
            self.right=self.left+diff*self.rp1[ord(c)]
            self.left=self.left+diff*self.lp1[ord(c)]
            self.cnt[c]+=1
            self.update()
        else:
            self.right=self.left+diff*self.rp2[ord(self.last)*self.total+ord(c)]
            self.left=self.left+diff*self.lp2[ord(self.last)*self.total+ord(c)]
            self.cnt[self.last+c]+=1
            self.last=c
            self.update()

    #更新字典
    def update(self,initialize=False):
        #初始化一阶
        if initialize:
            cur=0
            for i in range(self.total):
                self.rp1[cur]=(0 if cur==0 else self.rp1[cur-1])+self.cnt[chr(i)]
                cur+=1
            total1=self.rp1[self.total-1]
            self.rp1/=total1
            self.lp1[1:self.total]=self.rp1[0:self.total-1]

        #计算二阶前缀和
        cur=0
        for i in range(self.total):
            for j in range(self.total):
                self.rp2[cur]=(0 if cur==0 else self.rp2[cur-1])+self.cnt[chr(i)+chr(j)]
                cur+=1
        total2=self.rp2[self.total*self.total-1]
        self.rp2/=total2
        self.lp2[1:self.total*self.total]=self.rp2[0:self.total*self.total-1]

    #计算可写入文件数字
    def generateWriteData(self):
        # print("before "+str(self.left)+" "+str(self.right)+" "+str(self.writeData))
        while True:
            leftInt=int(self.left*10)
            rightInt=int(self.right*10)
            if leftInt==rightInt:
                self.writeData*=10
                self.writeData+=leftInt
                self.left=self.left*10-leftInt
                self.right=self.right*10-rightInt
            else: 
                # print("after "+str(self.left)+" "+str(self.right)+" "+str(self.writeData))
                return

    #压缩(TODO)
    def ziptxt(self,inputFile,outputFile):
        with open("./"+inputFile,"r") as readFile:
            with open("./"+outputFile,"wb") as writeFile:
                for line in readFile:
                    for c in line:
                        self.read(c)
                        self.generateWriteData()
                        if self.writeData:
                            print("write into file "+str(self.writeData)+" "+str(bytes(self.writeData.to_bytes(1,byteorder='big',signed=True))))
                            writeFile.write(self.writeData.to_bytes(1,byteorder='big',signed=True))
                            self.writeData=0
                        


