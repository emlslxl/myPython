import os

decodeData = []
#16进制表示的ascii，转换成字符串。'3''1' -> '1'
def ascii16_2_str(addr,len):
	str_list = []
	for i in range(1,len+1):
		str_list.append(chr(int(addr[(i-1)*2:i*2],16)))	#将16进制ascii按顺序加入列表
	return ''.join(str_list)	#列表转字符串

#字符型u8整数 转换成 整数
def ascii8_2_u8(addr):
	return int(addr[0:2],16)

#字符型u16整数 转换成 整数
def ascii16_2_u16(addr):
	return int(addr[0:2],16) | (int(addr[2:4],16) << 8)

def analyze_MsgHead(addr):
	index = 0
	index += 8
	decodeData.append(get_device_name(addr[index:],16))#list[0]
	logging.info("ID : %s" %(get_device_name(addr[index:],16)))
	index += 32

	decodeData.append(ascii16_2_u16(addr[index:]))#list[1]
	logging.info("SN : %d" %(ascii16_2_u16(addr[index:])))
	index += 4

	decodeData.append(ascii8_2_u8(addr[index:]))#list[2]
	logging.info("body num : %d" %(ascii8_2_u8(addr[index:])))
	index += 2

	decodeData.append(ascii16_2_u16(addr[index:]))#list[3]
	logging.info("msg len : %d" %(ascii16_2_u16(addr[index:])))
	index += 4

def analyze_MsgId1(addr):
	index = 0
	logging.info("厂家编号 中断型号 客户编号 车型编号 协议版本 固件版本 硬件版本")
	logging.info("%d        %d        %d        %d        %d       %d       %d" %(ascii8_2_u8(addr[index:])\
		,ascii8_2_u8(addr[index+2:]),ascii8_2_u8(addr[index+4:]),ascii8_2_u8(addr[index+6:])\
		,ascii8_2_u8(addr[index+8:]),ascii8_2_u8(addr[index+10:]),ascii8_2_u8(addr[index+12:])))

def get_device_name(addr,len):
	return ascii16_2_str(addr,len)

def calc_BCC(addr):
	hex_list = []
	j = 0
	for i in addr:
		if j%2 == 0:
			a = i
			# print("a =",a)
		else:
			b = i
			# print("b =",b)
			hex_list.append(a+b)
		j += 1
	
	j = decodeData[3]+25-3	#len
	count = 0
	bccValue = 0
	while(count < j):
		bccValue = bccValue^int(hex_list[3+count],16)
		count += 1
	return bccValue
		

		


############################################################
import logging 

#（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET）
logging.basicConfig(level=logging.DEBUG,  
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                datefmt='%a, %d %b %Y %H:%M:%S',  
                filename='./test.log',  
                filemode='w') 
##############################################################

f = open("./uploadData.txt", "r")

str1 = f.readline()
# logging.info(str1)
f.close()

if('[INFO]' in str1):
	index = str1.index('INFO')

if('F1F2FF' in str1):
	index = str1.index('F1F2FF')

analyze_MsgHead(str1[index:])
index += 50

logging.info("msg ID : %d" %(ascii16_2_u16(str1[index:])))
index += 4
logging.info("msg len : %d" %(ascii16_2_u16(str1[index:])))
index += 4

analyze_MsgId1(str1[index:])

logging.info("BCC : 0x%X" %calc_BCC(str1))
