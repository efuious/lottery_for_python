from system import system, usermanage
import os


def setting():
	while 1:
		Show_Ins()
		_input = input()
		if _input == "1":
			set_slogen()
		elif _input== "2":
			set_present()
		elif _input == "3":
			delete_history()
		elif _input == "4":
			set_user()
		elif _input == "5":
			set_shown()
		elif _input == "6":
			return 0
		else:
			system.ErrorBack("error input:" + _input)
			

def Show_Ins():
	system.clrscr()
	print("====Setting====")	
	print("1.set slogen")
	print("2.set present")
	print("3.delete history informations")
	print("4.user management")
	print("5.shown management")
	print("6.back")

def set_slogen():
	_input = input("input the slogen:")
	slogen = open(system.slogen, "w")
	slogen.write(_input)
	slogen.close()
	system.ErrorBack("success...")	

def delete_history():
	_input = input("are you sure to delete it? [Y/n]")
	if _input == "Y":
		try:
			os.remove(system.history)
		except IOError:
			system.ErrorBack("delete failed")
	else:
		return 0

def set_user():
	while 1:
		system.clrscr()
		show_set_user()
		_input = input()
		if _input == "1":
			usermanage.add()
		elif _input == "2":
			usermanage.delete()
		elif _input == "3":
			usermanage.change()
		elif _input == "4":
			return 0
		else:
			system.ErrorBack("Error input: " + _input)

def show_set_user():
	print("1.add user")
	print("2.delete user")
	print("3.change user information")
	print("4.back")

def set_shown():
	show_shown()
	_ID = input("show user ID? " + system.yon + " : ")
	_name = input("show user name? " + system.yon + " : ")
	_file = open(system.shown, 'w')

	if _ID == 'Y':
		_file.write('1\n')
	else:	_file.write('0\n')
	if _name == 'Y':
		_file.write('1')
	else:	_file.write('0')
	_file.close()
	return 0

def show_shown():
	system.clrscr()
	_file = system.openfile(system.shown)
	shown = list(range(0,2))

	if (_file == False):
		print('shown not setting!')
		return False
	else:
		for line,i in zip(_file,range(0,2)):
			shown[i] = line.strip('\n')
		if shown[0] == '1':
			print("show ID: Yes")
		else:
			print("show ID: No")
		if shown[1] == '1':
			print("show name: Yes")
		else:
			print("show name: No")
		_file.close()
		return True

def set_present():
	system.clrscr()
	print('set present')
	_kinds  = input('input the kinds of present') 
	if system.compare(_kinds, 1):
			system.ErrorBack("you must input a number bigger than 1")
			return 
	for i in range(0,_kinds):
		print("set present:",i)
		_name = input("name: ")
		_code = input("code: ")
		_num  = input("number:")
		if system.compare(_num, 1):
			system.ErrorBack('you must input a number bigger than 1')

