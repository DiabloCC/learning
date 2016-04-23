# func_para.py
# demo for varargs parameters and keyword-only parameters

# VarArgs Parameters
# numbers is a tuple, keywords is a dictionary
def total1(initial=5, *numbers, **keywords):
	count = initial
	print('numbers=', numbers)
	print('count=', count)
	for number in numbers:
		count += number
		print('count=', count)
	for key in keywords:
		print('%s=%d' % (key, keywords[key]))
		count += keywords[key]
		print('count=', count)
	return count

# keyword-only parameters
# extra_number is a keyword-only parameter
def total2(initial=5, *numbers, extra_number):
	count =  initial
	print('numbers=', numbers)
	print('count=', count)
	for number in numbers:
		count += number
		print('count=', count)
	print('extra_number=', extra_number)
	count += extra_number
	print('count=', count)
	return count

print('total1 begins\n-------------')
print('The total is',total1(10,1,2,3,4,vegetables=50,fruits=100))
print()
print('total2 begins\n-------------')
print('The total is',total2(10,1,2,3,extra_number=100))
