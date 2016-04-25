# -*- coding: utf-8 -*-
# codewars kata5_powerset.py

import itertools

def powerset(s):
	r = [[]]
	for i in range(0,len(s)):
		if [s[i]] not in r:
			r.append([s[i]])
		for j in range(1, len(s)-i):	# subset items count - 1
			for k in range(i+1, len(s)-j + 1):
				#if k + j<len(s):
					n = [s[i]]
					for l in range(0,j):
						n.append(s[k+l])
					#print(n1,n2)
					if n not in r:
						r.append(n)
						#print(r)
	return r

def powerset1(s):
	r =[[]]
	for n in s:
		r += [x+[n] for x in r if x+[n] not in r]
	return r

# --------------------------------
# The previous functions take lists that include same values into consider.
# Functions below will fail when the argument list includes same value.
# -------------------------------- 

def powerset2(s):
	return [list(c) for i in range(len(s)+1) for c in itertools.combinations(s,i)]

def powerset3(s):
	return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1) )

def powerset4(s):
	r = set([(), tuple(s)])
	r.update(*(powerset4(s[:i] + s[i+1:]) for i in range(len(s))))
	return r

def powerset5(s):
	# this is the default subset. empty
	r = [[]]
	for element in s:
		# circle all the elements for the given set,
		# for every element a powerset is the sum of:
		# * the subsets that contains that element
		# * the subsets that do not contain the element (previous sets)
		r.extend([previous_set + [element] for previous_set in r])
	return r

def powerset6(s):
	if not s: return [[]]
	x, r = s[0], s[1:]
	rsubs = powerset6(r)
	return rsubs + [[x]+y for y in rsubs]

def main():
	s = [1,2,1,6]
	print(powerset(s))

if __name__ == '__main__':
	main()



