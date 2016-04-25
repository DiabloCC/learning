# -*- coding: utf-8 -*-
# ds0202_PrefixExpression.py

op = {'+':0, '-':0, '*':1, '/':1, '^':2, '(':3, ")":3}

def prefixExp(string):
	i = len(string) - 1
	stack = []
	o = ''
	r = ''
	sig = 0 #sign for digits
	while i >= 0:
		if string[i] in op.keys():
			sig = 0
			if string[i] == '(':
				o = stack.pop()
				while o != ')':
					r = o + ' ' + r
					o = stack.pop()
			elif len(stack) > 0:
				if (op[stack[-1]] <= op[string[i]]) or (string[i] == ')') or (stack[-1] == ')'):
					stack.append(string[i])
				else:
					r = string[i] + ' ' + r
			else:
				stack.append(string[i])
		else:
			if sig == 0:
				r = string[i] + ' ' + r
			else:
				r = string[i] + r
			sig = 1

		# print('string[%d]=%s\tr=%s\tstack='%(i,string[i],r),stack)
		i -= 1
	for i in stack[::-1]:
		r = i + ' ' + r
	return r.strip()

def doPrefix(string):
	s = string.split(' ')
	# print(s)
	i = len(s) - 1
	stack = []
	while i >= 0:
		# print('s[%d] = ' % i, s[i], '\tstack =',stack)
		if s[i] in op.keys():
			if s[i] == '+':
				stack.append(stack.pop() + stack.pop())
			if s[i] == '-':
				stack.append(stack.pop() - stack.pop())
			if s[i] == '*':
				stack.append(stack.pop() * stack.pop())	
			if s[i] == '/':
				stack.append(stack.pop() / stack.pop())
			if s[i] == '^':
				stack.append(stack.pop() ** stack.pop())
			# print('r =',r)
		else:
			stack.append(eval(s[i]))
		i -= 1
	return stack.pop()

def main():
	s = '1+((32+3)*14)-5'
	print(doPrefix(prefixExp(s)))

if __name__ == '__main__':
	main()
 