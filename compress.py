import numpy as np
import gmpy2
import os
import stringgit 
class Compress:
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
    def generateBible(self,c):
        with open("./"+inputFile,"r") as readFile:
            for line in readFile:
                for c in line:
                    self.read(c)
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
        self.right = self.left + diff * self.rp2[self.last * self.total + ord(c)]
        self.left = self.left + diff * self.lp2[self.last * self.total + ord(c)]

    #计算左右区间相同的数字并写入文件
    def generateWriteData(self):
            leftInt = int(self.left*10)
            rightInt = int(self.right*10)
            if leftInt == rightInt:
                self.writeData *= 10
                self.writeData += leftInt
                self.left = self.left * 10 - leftInt
                self.right = self.right * 10 - rightInt
                return True 
            else: 
                return False

    #压缩(TODO)
    def ziptxt(self,inputFile,outputFile):
        generateBible(self)
        with open("./"+inputFile,"r") as readFile:
            with open("./"+outputFile,"wb") as writeFile:
                lines=0
                for line in readFile:
                    for c in line:
                        self.transform(c)
                        while self.generateWriteData():
                            pass
                #将maxCharDigits写入，告知decompress文件maxCharDigits是多少，以读字典(TODO)
                writeFile.write(self.maxCharDigits)
                #写标志符(TODO)
                writeFile.write('#')
                #将字典写入文件（四位按字节写入？）(TODO)
                for num in cnt:
                    bit = cnt.digits(2)

                #将编码结果写入文件(TODO)
                bit = self.writeData.digits(2)
                while len(bit) != 0:
                    qwq = int(bit[1:9],2)
                    writeFile.write(qwq.to_bytes(1, byteorder = 'big', signed = False));
                    bit = bit[9:]
        print("the size of the inputfile:"+str(os.path.getsize(inputFile))+" byte")
        print("the size of the outputfile:"+str(os.path.getsize(outputFile))+" byte")

