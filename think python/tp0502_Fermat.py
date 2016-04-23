# -*- coding:utf-8 -*-
# tp0502_Fermat.py


def check_fermat(a,b,c,n):
	if (a**n + b**n == c**n):
		return True
	else:
		return False

def main():
	print('Please input 4 numbers to test Fermat\'s Last Theorem.')
	print('The 4 numbers represent a b c n in turn.')
	s = input('Each number is seperated by a space:\n').split(' ')
	if (int(s[3]) > 2):
		r = check_fermat(int(s[0]), int(s[1]), int(s[2]), int(s[3]))
		if r:
			print('\nHoly smokes, Fermat was wrong!')
		else:
			print('\nNo, that doesn\'t work.')
	else:
		print('\nThe number n mustn\'t less than 3!')

if __name__ == '__main__':
	main()