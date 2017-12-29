# -*- coding: utf-8 -*-
# @Author: emlslxl
# @Date:   2016-09-26 17:35:17
# @Last Modified by:   emlslxl
# @Last Modified time: 2016-09-26 18:09:27

fd = open("my_test.txt","w+")   #create a file

fd.write("hello!!!\n")  #写入内容
fd.write("jam")         #写入内容

fd.seek(0)          #从第一行读起
str = fd.readline() #读第一行
print(str)

str = fd.readline() #读第二行
print(str)

fd.seek(0)          #设置 byte offset = 0
pos = fd.tell()     #获取当前 byte offset
print(pos)

str = fd.read(10)   #从当前byte offset（0）开始读取10个byte
print(str)

pos = fd.tell()     #获取当前byte offset
print(pos)

fd.close()