import numpy as np
import gmpy2
import os
class Decompress:
    #初始化变量
    def __init__(self):
        self.left=0.0#左区间
        self.right=1.0#右区间
        self.writeData=gmpy2.mpz(0)#最大相同次数
        self.maxCharDigits = 12 #规定个字符可能出现次数的二进制位数，字符表将占用32*maxCharDigits个Byte
        self.total=256
        self.cnt=np.zeros(self.total)
        #初始化一阶概率的左右端点
        self.lp=np.zeros(self.total)
        self.rp=np.zeros(self.total)

    #算出静态字典
    def generateBible(self,inputFile):
        with open("./"+inputFile,"r") as readFile:
            for line in readFile:
                for c in line:
                    self.cnt[ord(c)] += 1
        cur=0
        for i in range(self.total):
            self.rp[cur] = (0 if cur == 0 else self.rp[cur - 1]) + self.cnt[i]
            cur += 1
        total1 = self.rp[self.total-1]
        self.rp /= total1
        self.lp[1:self.total]=self.rp[0:self.total-1]

    #读取每个字符并转换为区间
    def transform(self,c):
        diff = self.right-self.left
        self.right = self.left + diff * self.rp[ord(c)]
        self.left = self.left + diff * self.lp[ord(c)]

    #计算左右区间相同的数字放进大整数writeData中
    def generateWriteData(self):
        while True:
            leftInt = int(self.left*10)
            rightInt = int(self.right*10)
            if leftInt == rightInt:
                self.writeData *= 10
                self.writeData += leftInt
                self.left = self.left * 10 - leftInt
                self.right = self.right * 10 - rightInt
            else: 
                break

    #压缩(TODO)
    def ziptxt(self,inputFile,outputFile):
        self.generateBible(inputFile)
        with open("./"+inputFile,"r") as readFile:
            with open("./"+outputFile,"wb") as writeFile:
                # lines=0
                for line in readFile:
                    for c in line:
                        self.transform(c)
                        self.generateWriteData()
                        # print(self.left," ",self.right)
                    # lines+=1
                    # print("Finished ",lines," lines.")
                self.writeData*=10
                self.writeData+=int(self.right*10)
                #将编码结果写入文件
                gmpy2.get_context().precision=9000
                bit = self.writeData.digits(2)
                while len(bit) != 0:
                    qwq = int(bit[0:8],2)
                    writeFile.write(qwq.to_bytes(1, byteorder = 'big', signed = False));
                    bit = bit[9:]
        print("the size of the inputfile:"+str(os.path.getsize(inputFile))+" bytes")
        print("the size of the outputfile:"+str(os.path.getsize(outputFile))+" bytes")

