# -*- coding: utf-8 -*-
# lxf_MapReduce.py

from functools import reduce

def normalize(s):
  if s=='':
    return s
  if len(s)==1:
    return s[0].upper()
  return s[0].upper()+s[1:].lower()
  
def main():
  # 测试:
  L1 = ['adam', 'LISA', 'barT']
  L2 = list(map(normalize, L1))
  print(L2)
  
if __name__=='__main__':
  main()