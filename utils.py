import numpy as np
import os
import math
#将长度为lenght的浮点数转化为二进制数
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

#将二进制数精确转化为浮点数
def bin2float(bin):
    exponent=np.arange(0,len(bin),1)
    num=np.sum(np.multiply(bin,1/pow(2,exponent)))
    return num

#更新字典
def update(lp,rp,cnt,total):
    cur=0
    for i in range(total):
        rp[cur]=(0 if cur==0 else rp[cur-1])+cnt[i]
        cur+=1
    sum=rp[total-1]
    rp/=sum
    lp[1:total]=rp[0:total-1]

#读入字符
def read(self,c):
    print(ord(c))
    diff=self.right-self.left
    #读取第一个数字时用一阶（不需要update）
    if self.last==-1:
        ordC=ord(c)
        self.right=self.left+diff*self.rp1[ordC]
        self.left=self.left+diff*self.lp1[ordC]
        # self.cnt1[ord(c)]+=1
        self.last=ord(c)
        # update(self.lp1,self.rp1,self.cnt1,self.total)
    #其他状况用二阶
    else:
        ordC=self.last*self.total+ord(c)
        self.right=self.left+self.diff*self.rp2[ordC]
        self.left=self.left+diff*self.lp2[ordC]
        self.cnt2[ordC]+=1
        self.last=ord(c)
        update(self.lp2,self.rp2,self.cnt2,self.total*self.total)
