# -*- coding: utf-8 -*-
# ds0102_BinarySearch.py

import random

def PrintResult(Sep, bottom, top):
	print(Sep*10)
	print('bIndex=',bottom)
	print('tIndex=',top)
	a=input('Press any key to continue...')

def BinarySearch(SearchList, ToFind):
	bIndex = 0
	tIndex = len(SearchList) - 1
	while tIndex >= bIndex:
		if ToFind == SearchList[(tIndex + bIndex) // 2]:
			bIndex = tIndex = (tIndex + bIndex) // 2
			PrintResult('!',bIndex,tIndex)
			return bIndex
		elif ToFind > SearchList[(tIndex + bIndex) // 2]:
			bIndex = (tIndex + bIndex) // 2 + 1
			PrintResult('+',bIndex,tIndex)
		elif ToFind < SearchList[(tIndex + bIndex) // 2]:
			tIndex = (tIndex + bIndex) // 2 - 1
			PrintResult('-',bIndex,tIndex)
	else:
		return -1


s = []
for i in range(100):
	s.append(random.randint(100,9999))
s.sort()
print(s)
a=eval(input('Please input an integer between 100 and 9999: '))
print('ToFind=',a)
b = BinarySearch(s,a)
if b == -1:
	print('The value %d does not exists in the list!' % a)
else:
	print('The value %d is located in the index of %d in the list!' % (a, b))


