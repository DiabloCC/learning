# -*- coding: utf-8 -*-
# codewars kata4_ValidBraces.py

BRACES = {'(':')', '[':']', '{':'}'}

def validBraces(string):
  r_end = len(string)
  for i in range(len(string)):
    r_brace = BRACES.get(string[i], False)
    if not r_brace: return False
    j = string.find(r_brace,i + 1)  
    if (j == -1) or (j > r_end): return False
    n = string.count(string[i],i+1,j)
    for k in range(n):
      j = string.find(r_brace,j+1)
    if (j == -1) or (j > r_end): return False
    r_end = j
  return True

def main():
	s = '[]'
	print(validBraces(s))

if __name__ == '__main__':
	main()