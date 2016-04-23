# -*- coding:utf-8 -*-
# tp0503_Triangle.py

def is_triangle(a, b, c):
	if (c>a+b) or (a>b+c) or (b>a+c):
		return False
	else:
		return True

def main():
	print('Please input 3 numbers to test if they can build a triangle.')
	#print('The 4 numbers represent a b c n in turn.')
	s = input('Each number is seperated by a space:\n').split(' ')
	r = is_triangle(int(s[0]), int(s[1]), int(s[2]))
	if r:
		print('\nYES!')
	else:
		print('\nNo!')

if __name__ == '__main__':
	main()