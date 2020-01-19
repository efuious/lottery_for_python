from system import system
from system import lottery
from system import setting
from system import info

def MainPage():
	while 1:
		Instructions()
		num = input()
		if num == "1":
			lottery.lottery()
		elif num == "2":
			setting.setting()
		elif num == "3":
			info.information()
		elif num == "4":
			exit()
		else:
			system.clrscr()
			system.ErrorBack(("error input:", num));

def Instructions():
	system.clrscr()
	print("welcom to lottery systemtem")
	print("1.start")
	print("2.setting")
	print("3.infomation")
	print("4.exit")

MainPage()
