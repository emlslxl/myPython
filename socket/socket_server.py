# -*- coding: utf-8 -*-
# @Author: emlslxl
# @Date:   2017-01-05 14:58:56
# @Last Modified by:   emlslxl
# @Last Modified time: 2017-01-06 11:06:02

import socketserver  # 导入socketserver模块
import binascii	#2进制转ascii
import time

############################################################
import logging 

#（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET）
logging.basicConfig(level=logging.DEBUG,  
                format='%(asctime)s %(message)s',  
                datefmt='%Y-%m-%d %H:%M:%S',  
                filename='./test.log',  
                filemode='w') 
##############################################################



def analyze_Msg(addr):
	index = 0

	index += 2
	if addr[index] == 0x2:
		print("实时",end="  ")
		logging.info("实时")
	elif addr[index] == 0x3:
		print("补发",end="  ")
		logging.info("补发")

	index += 1
	index += 1
	# print("%s" %(get_vin(index,17)))
	
	index += 17
	
	index += 3
	print("终端时间 |%d-%.2d-%.2d %.2d:%.2d:%.2d|" %(addr[index+0]+2000,addr[index+1],
		addr[index+2],addr[index+3],addr[index+4],addr[index+5]),end="  ")
	logging.info("终端时间 |%d-%.2d-%.2d %.2d:%.2d:%.2d|" %(addr[index+0]+2000,addr[index+1],
		addr[index+2],addr[index+3],addr[index+4],addr[index+5]))

	# 格式化成2016-03-20 11:45:39形式
	print ("本地时间 |"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"|")




class MyServer(socketserver.BaseRequestHandler):  # 创建一个类，继承自socketserver模块下的BaseRequestHandler类
    def handle(self):  # 要想实现并发效果必须重写父类中的handler方法，在此方法中实现服务端的逻辑代码（不用再写连接准备，包括bind()、listen()、accept()方法）
        while 1:
            conn = self.request
            addr = self.client_address
            # 上面两行代码，等于 conn,addr = socket.accept()，只不过在socketserver模块中已经替我们包装好了，还替我们包装了包括bind()、listen()、accept()方法
            while 1:
                # accept_data = str(conn.recv(1024), encoding="utf8")	#ascii
                # print(accept_data)
                # 
                accept_data = conn.recv(1024)	#hex
                print(binascii.b2a_hex(accept_data[0:]))	#打印接收到的16进制消息
                if accept_data[0] == 0x23 and accept_data[1] == 0x23:
                	analyze_Msg(accept_data)

            conn.close()


if __name__ == '__main__':
    sever = socketserver.ThreadingTCPServer(("192.168.1.170", 12001),
                                            MyServer)  # 传入 端口地址 和 我们新建的继承自socketserver模块下的BaseRequestHandler类  实例化对象

    sever.serve_forever()  # 通过调用对象的serve_forever()方法来激活服务端