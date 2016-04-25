# -*- coding: utf-8 -*-
# learn lxf_generator.py

def triangles():
	s = [1]
	yield s
	while True:
		r = []
		head = 0
		for i in range(len(s)):
			r += [head + s[i]]
			head = s[i]
		r += [s[-1]]
		yield r
		s = r

def main():
	n = 0
	for t in triangles():
		print(t)
		n = n+1
		if n == 10:
			break

if __name__ == '__main__':
	main()



