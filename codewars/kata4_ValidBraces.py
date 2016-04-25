# -*- coding: utf-8 -*-
# codewars kata4_ValidBraces.py

BRACES = {'(':')', '[':']', '{':'}'}

# bugs remain

def validBraces1(string):
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
  
def validBraces2(string):
  r = True
  if len(string) > 0:
    if BRACES.get(string[0], '') == '':
      r = False
    else:
      j = string.rfind(BRACES[string[0]])
      if j == -1:
        r = False
      elif len(string) > 2:
        r = validBraces2(string[1:j]) and validBraces2(string[j+1:])
  return r
  
# no bugs
def validBraces(string):
  s = []
  for x in string:
    if BRACES.get(x, '') == '':
      if len(s) == 0:
        return False
      elif not BRACES[s.pop()] == x:
        return False
      else:
        s.append(x)
    return len(s) == 0

def main():
	s = '[({])['
	print(validBraces(s))

if __name__ == '__main__':
	main()