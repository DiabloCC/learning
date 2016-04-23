# -*- coding: utf-8 -*-
# codewars kata4_Permutations.py


def permutations(string):
    #your code here
    if len(string) == 1:
        return [string]
    # r = []
    # for x in tuple(permutations(string[1:])):
    #     for i in range(len(x)):
    #         r.append(x[:i]+string[0]+x[i:])
    #     r.append(x+string[0])
    # return list(set(r))
    return list(set([x[:i]+string[0]+x[i:] for x in permutations(string[1:]) for i in range(len(x)+1)]))

def main():
	s = "aabb"
	print(permutations(s))

if __name__ == '__main__':
	main()