#函数功能测试

from system import system

#_file = open(system.shown,'w+')
#line = system.count(_file)
#_file.write('1\n')
#_file.write('1')
#_file.close()
#print(line)

#_file = system.openfile(system.userlist)
#if _file == False:
#	system.ErrorBack('Read File Error')
#else:
#	for line in _file:
#		print(line.strip('\n'))
#		for i in range(0,len(line)):
#
#	print('---')

#_kind = ''
#while _kind.isdigit()==False:
#	_kind = input('enter kind')

_in = input()

if system.compare(_in, 0):
	print('Yes')
else:
	print('No')
