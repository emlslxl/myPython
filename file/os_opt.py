# -*- coding: utf-8 -*-
# @Author: emlslxl
# @Date:   2016-09-26 15:44:36
# @Last Modified by:   emlslxl
# @Last Modified time: 2016-09-26 17:31:30
import os

pwd = os.getcwd()	#get current path
print("cur pwd = %s" %(pwd))

file_list = os.listdir(pwd)	#get file name in current path

print(file_list)

for i in file_list:
	print(i)