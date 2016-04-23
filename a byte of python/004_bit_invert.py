# 004_bit_invert.py

def binaryToInt(biNum, bUnsigned = False):
	iNum = 0
	print('biNum = ', biNum)
	bSign = int(biNum[0]) if not (bUnsigned or biNum[-1] == 'u') else 0
	biNum = biNum[(1 if not (bUnsigned or biNum[-1] == 'u') else 0):(len(biNum) if biNum[-1] != 'u' else -1)]
	print('biNum符号:', bSign)
	print('biNum数值部分:',biNum)
	print('-------------')
	for i in range(len(biNum)):
		iNum += int(biNum[i]) * 2 ** (len(biNum) - 1 - i)  # i.e 1101 1*2**2 + 1*2**1 + 0*2**0
		print(iNum)
	return(iNum if not bSign else -iNum)

def intToBinary(iNum, bUnsigned = False):
	bSign = '1' if iNum < 0 else '0'
	iLoopNum = int((iNum ** 2) ** 0.5)  # make positive!
	biNum = ''
	while iLoopNum:
		biNum += str(iLoopNum % 2)
		iLoopNum /= 2
	return bSign + biNum[::-1] if not bUnsigned else biNum[::-1] + 'u'

def main():
	biNum = input('请输入一个二进制值：')
	a = binaryToInt(biNum)
	print('转换结果：', a)

if __name__ == '__main__':
	main()

