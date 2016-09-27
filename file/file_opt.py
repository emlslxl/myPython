# -*- coding: utf-8 -*-
# @Author: emlslxl
# @Date:   2016-09-26 17:35:17
# @Last Modified by:   emlslxl
# @Last Modified time: 2016-09-26 18:09:27

fd = open("my_test.txt","w+")	#create a file

fd.write("hello!!!\n")
fd.write("jam")

fd.seek(0,0)
str = fd.readline()
print(str)

str = fd.readline()
print(str)

fd.seek(0,0)
pos = fd.tell()
print(pos)

str = fd.read(10)
print(str)

pos = fd.tell()
print(pos)

fd.close();