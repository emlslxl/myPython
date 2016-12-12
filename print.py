# -*- coding: utf-8 -*-
# @Author: emlslxl
# @Date:   2016-09-14 16:02:41
# @Last Modified by:   emlslxl
# @Last Modified time: 2016-12-12 14:17:40

print('hello world')
print('hello world\n'*3)

import logging 

#（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET）
logging.basicConfig(level=logging.DEBUG,  
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                datefmt='%a, %d %b %Y %H:%M:%S',  
                filename='./test.log',  
                filemode='w') 

logging.debug('debug message')  
logging.info('info message')  
logging.warning('warning message')  
logging.error('error message')  
logging.critical('critical message') 

data = 254
print('data = %d' %data)
print('data = %X' %data)