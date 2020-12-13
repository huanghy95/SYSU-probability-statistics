# SYSU-probability-statistics-static
mid-term project

compress.py -> 压缩核心代码

decompress.py -> 解压核心代码

zip.py -> 压缩运行代码

unzip.py -> 解压运行代码

- 下载插件hexdump用于二进制文件的查看
  - 右上角进行查看(show hexdump按钮)
- 大概思路
  - 读入数据，计算字符出现次数，得到出现次数表
  - 这里的lp和rp是概率表,标志着每一个字符组合的概率区间
    - 概率表的下标是ord(`{ascii码}`),ascii码是chr(`{下标}`)
  - 每读取一个字符
    - 更新区间left,right,如果两个数字有相同的数字,使用generateWriteData函数生成待写入数字,并使用写进二进制数字
      - 具体实现为用一个num数组存储所有相同的数字（但是先不写）
      - 然后所有字符读取完成后再将整一个数组转化成二进制数字bin数组
  - 输出各个字符的出现次数，然后输出编码后数字
  - 解码
    - 读入次数表，再读入编码后数字，然后遍历所有可能的字符，找到数字所在的区间，更新左右区间
