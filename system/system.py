# do not change this file!
#系统参数

import os
import fileinput

sysdir   = "../sysinf/"		#系统文件目录
userdir  = "../user/"		#用户文件目录
namesign = "@"				#姓名标识符
IDsign   = "#"				#ID标识符
yon	 = "[Y/n]"				#“yes or no”

slogen   = sysdir+"slogen.txt"		#标语文件
history  = sysdir+"history.txt"		#历史文件
about    = sysdir+"about.txt"		#关于文件
userlist = sysdir+"userlist.txt"	#用户列表文件
shown	 = sysdir+"shown.txt"		#显示设置文件
single	 = sysdir+"single.txt"		#单项抽奖文件


speed 	 = 1000			#滚动速度

#清屏函数
def clrscr():
	r = os.system("cls")

#点击返回
def PressBack():
	_input = input("press a button to back")
	return 0

#点击返回(提示信息)
def ErrorBack(str):
	print(str)
	PressBack()

#删除所有用户
def rmAlluser():
	ls = os.listdir(userdir)
	for name in ls:
		file = os.path.join(userdir,name)
		os.remove(file)
	if os.path.exists(userlist):
		os.remove(userlist)

#打开文件
def openfile(_path):
	try:
		_file = open(_path,'r')
	except IOError:
		return False
	return _file

#打开文件
def inputfile(_path):
	try:
		_file = fileinput.input(_path,inplace=0)
	except FileNotFoundError:
		return False
	return _file

#读取文件内容(指定行)
def readline(_file,_num):
	_file.seek(0)
	num = 0
	line = ''
	for line in _file:
		if num==_num: return line
		num+=1
	else: 	
		#ErrorBack("No such line: ")
		return line

#计数函数
def count(_file):
	lines = 0
	try:
		for line in _file:
			lines+=1
	except IOError:
		_file.seek(0)
		return -1
	_file.seek(0)
	return lines

#比较大小
def compare(_num,num):
	if _num.isdigit():
		n = int(_num)
		if n > num:
			return 1
		elif _num < num:
			return -1
		elif _num == num:
			return 0
	else:
		return False



