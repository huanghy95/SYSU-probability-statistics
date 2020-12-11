# SYSU-probability-statistics
final-term project

- 下载插件hexdump用于二进制文件的查看
  - 右上角进行查看(show hexdump按钮)
- 大概思路
  - 阶数设置
    - ~~最高的阶数设置为二阶~~**不整**
    - 先所有的字符组合都计数为1,用于概率的初始化
    - 1阶的只用于第一个字符的读入~~(所以一阶的不需要update)~~需要
    - ~~之后的全部用二阶进行计算~~**不整**
    - 这里的lp和rp是概率表,标志着每一个字符组合的概率区间
    - 概率表的下标是ord(`{ascii码}`),ascii码是chr(`{下标}`)
  - 每读取一个字符
    - 更新区间left,right,如果两个数字有相同的数字,使用generateWriteData函数生成待写入数字,并使用写进二进制数字
      - 具体实现为用一个num数组存储所有相同的数字（但是先不写）
      - 然后所有字符读取完成后再将整一个数组转化成二进制数字bit数组
    - 更新概率表用于下一次计算
-  已完成
   -  都完成了
- TODO
  - Debug，解码不成功，失败或乱码
