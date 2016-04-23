# func_global.py

def printVar(X):
	print('X is',X)
	X = X - 10
	print('X minus 10 is',X)
	X = 100
	print('X now is',X)

def printVarGlobal():
	global X
	print('X is',X)
	X -= 10
	print('X minus 10 is',X)
	X = 100
	print('X now is',X)

X = 50
print('-------\nprintVar now begins\n-------')
printVar(X)
print('Finally X is',X)
print('\n-------\nprintVarGlobal now begins\n-------')
printVarGlobal()
print('Finally X is',X)