# -*- coding: utf-8 -*-
# lxf_filter.py

def is_palindrome(n):
  r = 0
  s = n
  while n > 0:
    r = r*10+n%10
    n = n//10
  return s == r
  
def is_palindrome1(n):
  return str(n) == str(n)[::-1]
    
def main():
  out = filter(is_palindrome1, range(1,1000))
  print(list(out))
  
if __name__=='__main__':
  main()