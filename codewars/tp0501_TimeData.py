# -*- coding:utf-8 -*-
# tp0501_TimeData.py

import time

def GetTimeData(t):
	days = t // 60 // 60 // 24
	years = days // 365
	hours = t // 60 // 60 % 24
	minutes = t // 60 % 60
	seconds = t % 60
	return [days, hours, minutes, seconds, years]

def main():
	r = GetTimeData(time.time())
	print('It is %d days %d hours %d minutes %d seconds past the very beginning of the system time!' % (r[0], r[1], r[2],r[3]))
	print('It is about %d years have past.' % (r[4]))

if __name__ == '__main__':
	main()
