# -*- coding: utf-8 -*-
# @Author: emlslxl
# @Date:   2016-09-26 15:47:44
# @Last Modified by:   emlslxl
# @Last Modified time: 2016-09-26 17:14:36

def my_sum(x,y):
	return x+y

def my_sub(x,y):
	if x < y:
		print("x < y")
		return 0
	return x-y

def my_sum_sub(x,y):
	return my_sum(x,y),my_sub(x,y)

# print("sum = %d, sub = %d" %(my_sum_sub(100,20)))

# x,y = my_sum_sub(10,2)
# print(x,y)