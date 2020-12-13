# SYSU-probability-Dynamemic_zero
mid-term project

- 下载插件hexdump用于二进制文件的查看
  - 右上角进行查看(show hexdump按钮)
- 大概思路
  - 阶数设置
    - 先所有的字符组合都计数为1,用于概率的初始化
    - 0阶全部初始化为一
    - 这里的lp和rp是概率表,标志着每一个字符组合的概率区间
    - 概率表的下标是ord(`{ascii码}`),ascii码是chr(`{下标}`)
  - 压缩
    - 每读取一个字符
        - WriteData初始化为1，解决前导零问题
        - 根据该字母在概率表的区间更新区间left,right
        - 精度解决：left、right高位相同字母丢到WriteData里
        - 更新概率表用于下一次计算
    - 最后加一个ascii为8的Back Space符，表示文章结束
    - 由于文件写入只能以字节写入，为方便期间，取WriteData为右区间right，从某位截断，以保证WriteData在二进制下的位数是8的倍数
  - 解压
    - 读取全部数，还原出数字出来，并预先取前len个数放到cur
    - 查找概率表，找到cur所在的区间，输出字符，更新概率表，更新左右区间
        - 区间比较时，令$ qwq = \frac{cur}{10^{len}} $，并截去qwq的整数部分，与以这个字符更新的左右区间比较
        - 解码到Back Space符时，解码结束
- 存在问题
  - ~~文章过长时，解码不成功，中途某处出现乱码，调整精度len会有所变化，初步怀疑比较的精度问题~~及时去掉qwq超出部分ztlyyds
