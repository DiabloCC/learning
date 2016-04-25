# -*- coding: utf-8 -*-
# learn lxf_functions.py

def hanoi(n, a, b, c, steps=[]):
	'''
	Hanoi Tower Solver

	Recursive method to solve the Hanoi Tower question.
	The function recieves 4 arguments:
	  1. number of plates on pillar A
	  2. name of pillar A
	  3. name of pillar B
	  4. name of pillar C
	'''
	if n == 1:
		steps.append('{0} --> {1}'.format(a,c))
		return		
	hanoi(n-1, a, c, b, steps)
	steps.append('{0} --> {1}'.format(a,c))
	hanoi(n-1, b, a, c, steps)



def main():
	a=[]
	hanoi(5, 'A', 'B', 'C',a)
	print('\n'.join(a))
	print('Total number of steps is', len(a))

if __name__ == '__main__':
	main()

