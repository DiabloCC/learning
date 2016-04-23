# print_numbers.py
# To test different methods of printing integers, one number per line
# two methods are tested: for-loop and recursive

def printNum_1(N):
	for i in range(1,N+1):
		print(i)

def printNum_2(N):
	if N>0:
		printNum_2(N-1)
		print(N)

def main():
	N = int(input('Please input an positive integer:'))
	M = input('Please choose which mothod to be called (f for for-loop / r for recursive, others for exit):')
	if M == 'f':
		printNum_1(N)
	elif M == 'r':
		printNum_2(N)
	else:
		exit(0)

if __name__ == '__main__':
	main()

# test result:
# in recursive mothod, the max number is 995 under python 3.5.1

