import numpy as np
import os
import math
def float2bin(num,length):
    bins = np.array([])
    while length > 0:
        num = num * 2
        if num >= 1.0:
            np.append(bins,1)
        else:
            np.append(bins,0)
        num -= int(num)
        length -= 1
    return bins

def bin2float(bin):
    exponent=np.arange(0,len(bin),1)
    num=np.sum(np.multiply(bin,1/pow(2,exponent)))
    return num

def update(lp,rp,cnt,total):
    cur=0
    for i in range(total):
        rp[cur]=(0 if cur==0 else rp[cur-1])+cnt[i]
        cur+=1
    sum=rp[total-1]
    rp/=sum
    lp[1:total]=rp[0:total-1]

def read(self,c):
    print(ord(c))
    diff=self.right-self.left
    #读取第一个数字
    if self.last==-1:
        ordC=ord(c)
        self.right=self.left+diff*self.rp1[ordC]
        self.left=self.left+diff*self.lp1[ordC]
        self.cnt1[ord(c)]+=1
        self.last=ord(c)
        update(self.lp1,self.rp1,self.cnt1,self.total)
    else:
        ordC=self.last*self.total+ord(c)
        self.right=self.left+self.diff*self.rp2[ordC]
        self.left=self.left+diff*self.lp2[ordC]
        self.cnt2[ordC]+=1
        self.last=ord(c)
        update(self.lp2,self.rp2,self.cnt2,self.total)
