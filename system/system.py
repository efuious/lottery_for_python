# do not change this file!

import os
import fileinput

sysdir   = "../sysinf/"
userdir  = "../user/"
namesign = "@"
IDsign   = "#"
yon	 = "[Y/n]"

slogen   = sysdir+"slogen.txt"
history  = sysdir+"history.txt"
about    = sysdir+"about.txt"
userlist = sysdir+"userlist.txt"
shown	 = sysdir+"shown.txt"
single	 = sysdir+"single.txt"


speed 	 = 1000

def clrscr():
	r = os.system("cls")

def PressBack():
	_input = input("press a button to back")
	return 0

def ErrorBack(str):
	print(str)
	PressBack()

def rmAlluser():
	ls = os.listdir(userdir)
	for name in ls:
		file = os.path.join(userdir,name)
		os.remove(file)
	if os.path.exists(userlist):
		os.remove(userlist)


def openfile(_path):
	try:
		_file = open(_path,'r')
	except IOError:
		return False
	return _file

def inputfile(_path):
	try:
		_file = fileinput.input(_path,inplace=0)
	except FileNotFoundError:
		return False
	return _file

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



