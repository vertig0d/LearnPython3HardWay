def printTwo(*args):
	arg1, arg2 = args
	print(f'arg1: {arg1}, arg2: {arg2}')

def printTwoAgain(arg1, arg2):
	print(f'arg1: {arg1}, arg2: {arg2}')

def printOne(arg1):
	print('arg1: ',arg1)
	
def printNone():
	print('no param')

printTwo('zed','shaw')
printTwoAgain('zed','shaw')
printOne('zed')
printNone()
