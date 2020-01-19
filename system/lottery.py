from system import system
import time


def lottery():
	while True:
		show_ins()
		_input = input()
		if _input == '1':single()
		elif _input == '2': return 0
		else:
			system.ErrorBack("error input: " + _input)

def show_ins():
	system.clrscr()
	print("1.single")
	print("2.back")

def rolling(_list):
	system.clrscr()
	_shown = system.openfile(system.shown)
	if _shown == False:
		system.ErrorBack("shown setting error")
		return False
	shown = list(range(0,2))
	for line,i in zip( _shown,range(0,2)):
		shown[i] = line.strip('\n')
#	_list = system.openfile(system.userlist)
	if _list == False:
		system.ErrorBack("No user set")
		return False
	_max = system.count(_list)
	print(_max)
	
	for i in range(0,_max):
		system.clrscr()
		print(system.readline(_list, i))
		time.sleep(0.1)

	_shown.close()
	return _max

def single():
	_list = system.openfile(system.userlist)
	n_user = rolling(_list)

	system.clrscr()
	
	if n_user == False:
		system.ErrorBack('Lottery failed')
		return 0
	_single = system.openfile(system.single)
	if _single == False:
		system.ErrorBack('Read present failed')
		return 0
	system.ErrorBack('SINGLE')
	return 0
