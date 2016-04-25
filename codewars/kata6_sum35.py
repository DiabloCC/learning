# -*- coding: utf-8 -*-
# codewars  kata6_sum35.py

def sums(n):
	return (3 * ((n-1)//3)*((n-1)//3 + 1) + 5 * ((n-1)//5)*((n-1)//5 + 1) - 15*((n-1)//15)*((n-1)//15 + 1))//2

def sums1(n):
	r = 0
	s = []
	for i in range(1, (n+2)//3):
		if (i*5<n):
			if (i%5==0):
				r += 5*i
				s += [5*i]
			elif (i%5==0):
				r += 3*i
				s += [3*i]
			else:
				r += 8*i
				s += [3*i, 5*i]
		elif i%5 != 0:
			r += 3 * i
			s += [3*i]
	s.sort()
	s.append(r)
	return s

def main():
	while True:
		s = input('please select method 1 or 2 to calculate: ')
		if s == '1':
			while True:
				n = eval(input('please input an integer number: '))
				if n==0:
					print('return to select method.\n---------------')
					break
				print('The sum of %d is %d'%(n,sums(n)))
		elif s == '2':
			while True:
				n = eval(input('please input an integer number: '))
				if n==0:
					print('return to select method.\n---------------')
					break
				r = sums1(n)
				print('The sum of %d is %d. The list is '%(n,r[-1]),r[0:-1])
		else:
			break
		

if __name__ == '__main__':
	main()
