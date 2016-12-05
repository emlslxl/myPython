# -*- coding: utf-8 -*-
# @Author: emlslxl
# @Date:   2016-09-27 14:30:03
# @Last Modified by:   emlslxl
# @Last Modified time: 2016-09-27 15:01:47

class People(object):
	"""docstring for People"""
	def __init__(self, n,a,w):
		super(People, self).__init__()
		self.name = n
		self.age = a
		self.__weight = w	#私有属性
	name = ''
	age = 0
	__weight = 0
	def say_hello(self):
		print("my name is %s,age %d,weight is ***" %(self.name,self.age))

class Student(People):
	grade = ''
	"""docstring for Student"""
	def __init__(self, n,a,w,g):
		#调用父类构造函数
		People.__init__(self,n,a,w)
		self.grade = g
	#重写父类方法
	def say_hello(self):
		print("my name is %s,grade %s" %(self.name,self.grade))
		

p1 = People('jam',24,120)
p1.say_hello()

s1 = Student('tom',15,98,3)
s1.say_hello()
		