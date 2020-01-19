#main page

from system import system		#系统参数相关
from system import lottery		#抽奖相关(待实现)
from system import setting		#系统设置相关
from system import info			#系统信息相关

#主页
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

#主页操作提示
def Instructions():
	system.clrscr()
	print("welcom to lottery systemtem")
	print("1.start")
	print("2.setting")
	print("3.infomation")
	print("4.exit")

MainPage()
