#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from time import ctime,sleep;

print "good,good!"
print 62 *'='  
#write code here begin

import telnetlib  
  
'''''Telnet远程登录：Windows客户端连接Linux服务器'''  
  
# 配置选项  
Host = '192.168.59.130' # Telnet服务器IP  
username = 'weilaidb'   # 登录用户名  
password = '00000000'  # 登录密码 
usertips = 'ubuntu login: ' #登录提示信息 
passwdtips = 'Password: '   #密码提示信息
finish = ']$ '      # 命令提示符（标识着上一条命令已执行完毕）  


def telnet_init():
	# 连接Telnet服务器  
	tn = telnetlib.Telnet(Host)  
	# print 'connect host'
	# 输入登录用户名  
	tn.read_until(usertips)  
	# print 'read ubuntu login: '
	tn.write(username + '\n')  
	# print 'write username'
	# 输入登录密码  
	tn.read_until(passwdtips)  
	# print 'read Password'
	tn.write(password + '\n')  
	# print 'write password'
	# 登录完毕后，执行ls命令  
	tn.read_until(finish)  
	return tn
	pass


def telnet_write_printinfo(prefixstr, tn , cmd):
	print prefixstr
	tn.write(cmd)
	# print 'write cd linux'
	Temp=tn.read_until(finish)
	# print Temp
	print(Temp.decode('utf-8'))
	


# tn.write('ls -alh && echo nihaoma\n')  
# print 'write ls'
# ss=tn.read_all()
# print "%r",ss
# print ss

# ls命令执行完毕后，终止Telnet连接（或输入exit退出）  
# Temp=tn.read_until(finish)  
# print "%s",Temp
# print Temp

# telnet_write_printinfo('', tn,'ls -alh && echo nihaoma\n')
# telnet_write_printinfo('cd linux', tn, 'cd /home/weilaidb/work/linux/kernel/linux/\n')
# telnet_write_printinfo('git pull....', tn, 'git pull\n')


# print 'cd linux'
# tn.write()
# print 'write cd linux'
# Temp=tn.read_until(finish)
# print Temp
#git pull
# tn.write('git pull\n')  
# Temp=tn.read_until(finish)
# print Temp

# tn.write('find . -maxdepth 1\n')  
# Temp=tn.read_until(finish)
# print Temp

# tn.write('git pull\n') 
# Temp=tn.read_until(finish)
# print Temp

# tn.close() # tn.write('exit\n')  



def main():
	tn = telnet_init()
	telnet_write_printinfo('', tn,'ls -alh && echo nihaoma哈哈\n')
	telnet_write_printinfo('cd linux', tn, 'cd /home/weilaidb/work/linux/kernel/linux/\n')
	telnet_write_printinfo('git pull....', tn, 'git pull\n')
	tn.close()
	
	
if __name__=="__main__":
	main()
	#write code here end
	print 62 *'='  
	for i in range(2000000):
		sleep(10)
		print "loopint at pos " +	 str(i)

	sleep(100)