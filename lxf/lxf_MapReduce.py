# -*- coding: utf-8 -*-
# lxf_MapReduce.py

from functools import reduce

def normalize(s):
  if s=='':
    return s
  if len(s)==1:
    return s[0].upper()
  return s[0].upper()+s[1:].lower()

def prod(L):
  def multi(a1, a2):
    return a1 * a2
  return reduce(multi, L)

def str2float(s):
  def mapf(a):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '.':}[a]
  def reducef(a1, a2):
    if a2 == '.':
      return a1 / 10
    else:
      return a1 / 10 + a2 
  
def main():
  # 测试:
  print('-----map------')
  L1 = ['adam', 'LISA', 'barT']
  L2 = list(map(normalize, L1))
  print(L2)
  print('-----reduce------')
  L1 = [3,5,7,9]
  print('3*5*7*9 =',prod(L1))
  print('-----map & reduce------')

if __name__=='__main__':
  main()