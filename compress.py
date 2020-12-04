import numpy as np
import string
class Compress:
    def __init__(self):
        self.left=0.0
        self.right=1.0
        self.last=" "
        self.cnt={}
        for first in string.ascii_lowercase:
            self.cnt[first]=1
            for second in string.ascii_lowercase:
                self.cnt[first+second]=1
        self.lp=np.zeros(256)
        self.rp=np.zeros(256)
        self.total1=256
        self.total2=65536

    def read(self,c):
        diff=self.right-self.left
        self.right=self.left+diff*self.rp[c]
        self.left=self.left+diff*self.lp[c]
        self.cnt[c]+=1
        self.cnt[self.last+c]+=1
        self.last=c
        self.total1+=1
        if self.total1>1:
            self.total2+=1

    def update(self):
        self.
        pass

mycompress=Compress()
with open("./data.txt","r") as file:
    for line in file:
        for c in line:
            mycompress.read(c)

with open("./write.data","wb") as file:
    file.write(bytes([10,2,3]))
