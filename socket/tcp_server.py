# -*- coding: utf-8 -*-
# @Author: emlslxl
# @Date:   2017-01-05 14:27:54
# @Last Modified by:   emlslxl
# @Last Modified time: 2017-01-05 14:52:12

import socket

sk = socket.socket()
sk.bind(("192.168.1.170", 12001))
sk.listen(5)
while True:
    conn, addr = sk.accept()
    while True:
        # accept_data = str(conn.recv(1024),encoding="utf8")
        accept_data = conn.recv(1024)
        if accept_data[0] == 0x23:
        	print("ssssssssssss")
        # print("".join(["接收内容：", accept_data, "     客户端口：", str(addr[1])]))
        # if accept_data == "byebye":  # 如果接收到“byebye”则跳出循环结束和第一个客户端的通讯，开始与下一个客户端进行通讯
        #     break
        # send_data = input("输入发送内p容：")
        # conn.sendall(bytes(accept_data, encoding="utf8"))
    conn.close()  # 跳出循环时结束通讯