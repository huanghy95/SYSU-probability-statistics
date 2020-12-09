import numpy as np
import os
import math
#暴力将长度为lenght的浮点数转化为二进制数
def float2bin(nums,codeLength):
    bins = np.array([])
    length=len(nums)
    cnt=0
    forward=0
    codeLength=int(codeLength)
    while cnt<codeLength:
        for i in range(length-1,-1,-1):
            nums[i]=2*int(nums[i])
            if forward:
                nums[i]+=1
                forward=0
            if i==0:
                if  nums[i]>=10:
                    bins=np.append(bins,int(1))
                    forward=1
                    nums[i]-=10
                else:
                    bins=np.append(bins,int(0))
            else:
                if  nums[i]>=10:
                    forward=1
                    nums[i]-=10      
        cnt+=1
    return bins

#将二进制数精确转化为浮点数
def bin2float(bins):
    exponent=np.arange(0,len(bins),1)
    nums=np.sum(np.multiply(bins,1/pow(2,exponent)))
    return nums

def bin2hex(bins):
    hexs=np.array([])
    cur=0
    cnt=0
    for i in bins:
        cur*=2
        cur+=i
        cnt+=1
        if cnt==4:
            cnt=0
            hexs=np.append(hexs,cur);
            cur=0
    return hexs
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
    diff=self.right-self.left #一开始的区间长度

    #读取第一个数字时用一阶（不需要update）
    if self.last==-1:
        ordC=ord(c) #下标
        #更新左右区间
        self.right=self.left+diff*self.rp1[ordC] 
        self.left=self.left+diff*self.lp1[ordC]
        self.last=ord(c) # 记录上次出现字符
    #其他状况用二阶
    else:
        ordC=self.last*self.total+ord(c) #下标
        self.right=self.left+diff*self.rp2[ordC] 
        self.left=self.left+diff*self.lp2[ordC]
        # print("lp ",str(self.lp2[ordC]),' rp ',str(self.rp2[ordC]))
        # print("new left ",str(self.left)," new right ",str(self.right))
        self.cnt2[ordC]+=1 
        self.last=ord(c) # 记录上次出现字符
        update(self.lp2,self.rp2,self.cnt2,self.total*self.total) #更新字典
