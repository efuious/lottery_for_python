from system import system


def information():
	while 1:
		Show_Ins()
		_input = input()
		if _input == "1":
			std_show(system.slogen)
		elif _input == "3":
			std_show(system.history)
		elif _input == "4":
			check_user()
		elif _input == "5":
			show_userlist()
		elif _input == "6":
			std_show(system.about)
		elif _input == "7":
			return 0;
		else:
			system.ErrorBack(("error input:" + _input))
	

def Show_Ins():
	system.clrscr()
	print("1.check slogen")
	print("2.check present")
	print("3.check history")
	print("4.check users")
	print("5.user list")
	print("6.about")
	print("7.back")

def std_show(_filename):
	system.clrscr()
	_file = system.openfile(_filename)
	if(_file==False):
		system.ErrorBack("Nothing")
		return 0

	print(_file.read())
	_file.close()
	system.PressBack()
	return 0

def show_userlist():
	system.clrscr()
	_userlist = system.openfile(system.userlist)
	if(_userlist==False):
		system.ErrorBack("Nothing")
		return 0

	for line in _userlist:
		i = 0
		while line[i] is not system.namesign:
			i = i + 1
		print('ID: '+line[1:i]+" name: "+line[i+1:len(line)-1])
	
	_userlist.close()
	system.PressBack()

def check_user():
	system.clrscr()
	_ID = input("input the ID you want to inquire:")	
	_user = system.openfile(system.userdir + _ID)
	if _user == False:
		system.ErrorBack("No such ID: " + _ID)
		return 0
	num = 0
	for line in _user:
		if num == 0:print("Name: "+line.strip('\n'))
		elif num == 1: print("Age: "+line.strip('\n'))
		elif num == 2: print("Sex: "+line.strip('\n'))
		num+=1	

	system.PressBack()



