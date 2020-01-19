# this file used to create default system.user for debug 
# DANGEROUS! All system.user will be replaced by default system.user

from system import system

def create():
	_ul = open(system.userlist, 'w')
	_ul.write(system.IDsign + '111' + system.namesign + '111\n')
	_ul.write(system.IDsign + '1' + system.namesign + '1\n')
	_ul.write(system.IDsign + '22' + system.namesign + '22\n')
	_ul.write(system.IDsign + '22222' + system.namesign + '22222\n')
	_ul.write(system.IDsign + '2' + system.namesign + '2\n')
	_ul.write(system.IDsign + '222' + system.namesign + '222\n')
	_ul.write(system.IDsign + '2222' + system.namesign + '2222\n')
	_ul.close()
	
	_uf = open(system.userdir + '111', 'w')
	_uf.write('111\n'+'boy\n'+'20\n')
	_uf.close()
	_uf = open(system.userdir + '1', 'w')
	_uf.write('1\n'+'boy\n'+'2\n')
	_uf.close()
	_uf = open(system.userdir + '22', 'w')
	_uf.write('22\n'+'b\n'+'20\n')
	_uf.close()
	_uf = open(system.userdir + '22222', 'w')
	_uf.write('22222\n'+'y\n'+'0\n')
	_uf.close()
	_uf = open(system.userdir + '2', 'w')
	_uf.write('2\n'+'o\n'+'20\n')
	_uf.close()
	_uf = open(system.userdir + '222', 'w')
	_uf.write('222\n'+'d\n'+'02\n')
	_uf = open(system.userdir + '2222', 'w')
	_uf.write('2222\n'+'boy2\n'+'220\n')
	_uf.close()

	_uf.close()

if __name__ == '__main__':
	system.rmAlluser()
	create()
