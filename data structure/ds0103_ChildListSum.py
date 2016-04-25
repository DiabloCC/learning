# -*- coding:utf-8 -*-
# ds0103_ChildListSum.py

def Sum1(TheList, N):
	MaxSum = 0
	MaxBotton = 0
	MaxTop = 0
	Count = 0
	for i in range(N):
		for j in range(i, N):
			ThisSum = 0
			for k in range(i, j+1):
				ThisSum += TheList[k]
				Count += 1
			if ThisSum > MaxSum:
				MaxSum = ThisSum
				MaxBotton = i
				MaxTop = j
	return [MaxSum, MaxBotton, MaxTop]

def Sum2(TheList, N):
	MaxSum = 0
	MaxBotton = 0
	MaxTop = 0
	Count = 0
	for i in range(N):
		ThisSum = 0
		for j in range(i, N):
			ThisSum += TheList[j]
			Count += 1
			if ThisSum > MaxSum:
				MaxSum = ThisSum
				MaxBotton = i
				MaxTop = j
	return [MaxSum, MaxBotton, MaxTop]

def Sum3(TheList, N):
	'''
	递归求解
	'''

	if N == 1:	# 终止条件：只有一个元素
		#print('---downstream to end----')
		if TheList[0] <= 0:
			return [0, None, None]
		else:
			return [TheList[0], 0, 0]

	if N > 1:
		LList = TheList[0:(N//2)]
		RList = TheList[(N//2):N]
		#print('--LEFT--')
		#print('LList =', LList)
		LSum = Sum3(LList, N//2)
		#LMax = LSum[0]
		#print('--RIGHT--')
		#print('RList =', RList)
		RSum = Sum3(RList, N - N//2)
		#RMax = RSum[0]

		if N == 2:
			LRSum = [LSum[0] + RSum[0], 0, 1]
		else:
			LEMax = [0, None]
			LESum = TheList[N//2 - 1]
			for i in range(N//2-2, -1, -1):
				LESum += TheList[i]
				if LESum > LEMax[0]:
					LEMax[0] = LESum
					LEMax[1] = i

			REMax = [0, None]
			RESum = TheList[N//2]
			for i in range(N//2+1, N):
				RESum += TheList[i]
				if RESum > REMax[0]:
					REMax[0] = RESum
					REMax[1] = i
			LRSum = [LEMax[0] + REMax[0], LEMax[1], REMax[1]]

		#print('N=',N)
		#print('LMax=',LMax)
		#print('RMax=',RMax)
		#print('LEMax=',LEMax)
		#print('REMax=',REMax)
		#print('-----')

		if LSum[0] >= RSum[0]:
			if LSum[0] >= LRSum[0]:
				return LSum
			else:
				return LRSum
		elif RSum[0] >= LRSum[0]:
				return RSum
		else:
			return LRSum

def main():
	s = [-1,-3,4,-3,5,-2,-1,2,6,-2]
	r = Sum3(s,10)
	print('''The max continuous sequence sum is %d.
The left index is %d.
The right index is %d.
The sequence is ''' % (r[0],r[1],r[2]), s[r[1]:r[2]+1])

if __name__ == '__main__':
	main()
