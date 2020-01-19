import fileinput
from system import system
import os


#this function used to create a new user
def add():
	system.clrscr()
	print("input the information:")
	_ID   = input("input the ID:")
	_name = input("input the name:")
	_age  = input("input the age:")
	_sex  = input("input the sex:")

# try to open user file to detect whether it existed
# error for non-existed and create it as a new user 
	try:
		_user_file = open(system.userdir + _ID, "r")
	except IOError:
		_user_file = open(system.userdir + _ID, "w")
		_user_file.write(_name+"\n"+_age+"\n"+_sex+"\n")
		_user_file.close()
# add user ID and user name to userlist 
		_user_list = open(system.userlist, "a")
		_user_list.write(system.IDsign + _ID + system.namesign + _name + '\n')
		_user_list.close()
		system.ErrorBack("success!")
		return 0
	system.ErrorBack("ID:" + _ID + " existed!")
	return 0

# this function used to detect user ID in userlist
# return True when find it
def detect(ID,line):
	ID_len = len(ID)
	line_len = len(line)
	for sign in range(0,line_len):
		if line[sign] == system.namesign:
			break
	if sign < ID_len+1:
		return False
	elif line[1:ID_len+1] == ID and line[ID_len+1] == system.namesign:
		return True
	else:
		return False

#this function used to delete a user 
def delete():
	_ID = input("input the ID you want to delete:")
# detect user file, no such user when user file non-existed, 
	try:
		_user = open(system.userdir + _ID, "r")
	except IOError:
		system.ErrorBack("No such ID:" + _ID)
		return 0
	_user.close()

# delect user name and ID in userlist and remove user file
	_delete = input("are you sure to delete ID:"+_ID+"[Y/n]")
	if _delete == "Y":
		_userlist = fileinput.input(system.userlist, inplace=1)
		
# if not detected in userlist, that's other user, copy them
# if detected, that's what we want to delete, do nothing
		for line in _userlist:
			if detect(_ID,line) == False:
                		print(line.strip('\n'))
		_userlist.close()
# delete user in userlist, remove user file
		os.remove(system.userdir + _ID)
		system.ErrorBack("success")
		return 0
	system.ErrorBack("cancel")


# this function used to change user information	
def change():
	_ID = input("input the ID you want to change:")
# detect user file, no such user when user file non-existed, 
	try:
		_user = open(system.userdir + _ID, "r")
	except IOError:
		system.ErrorBack("No such ID:" + _ID)
		return 0
# change open mode
	_user.close()
	_user = open(system.userdir + _ID, "w")
	print("input the information:")
	_name = input("name: ") 
	_age  = input("age: ")
	_sex  = input("sex: ")
# write changed information
	_user = open(system.userdir + _ID, 'w')
	_user.write(_name+'\n'+_age+"\n"+_sex)
# change user name in userlist
	_list = fileinput.input(system.userlist, inplace=1)
	for line in _list:
		if detect(_ID,line) == True:
			print(system.IDsign + _ID + system.namesign + _name)
		else:
			print(line.strip('\n'))
	_user.close()
	_list.close()
	system.ErrorBack("success!")
	return 0
