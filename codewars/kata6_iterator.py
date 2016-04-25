# -*- coding: utf-8 -*-
# codewars kata6_iterator.py

def get_double(n):
	return n * 2

def create_iterator(func, n):
	def decorated_fun(r):
		for i in range(n):
			r = func(r)
		return r
	return decorated_fun

def main():
	double_iterator = create_iterator(get_double, 2)
	print(double_iterator(3))

if __name__ == '__main__':
	main()
