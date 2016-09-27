# -*- coding: utf-8 -*-
# @Author: emlslxl
# @Date:   2016-09-26 16:26:52
# @Last Modified by:   emlslxl
# @Last Modified time: 2016-09-26 17:11:52

#args 可变长参数，不带有key值
def say_hello(greeting,*args):
	if len(args) == 0:
		print("%s!" %(greeting))
		print()
	else:
		print("len(args) = %d" %(len(args)))
		print('%s, %s!' % (greeting, ','.join(args)))
		print()

say_hello("hello")
say_hello("hello","allen")
say_hello("hello","1","2","3")