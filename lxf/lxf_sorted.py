# -*- coding: utf-8 -*-
# lxf_sorted.py

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
  return t[0]

def by_score(t):
  return t[1]
def main():
  print('sort by name\n',sorted(L, key=by_name))
  print('sort by score\n',sorted(L, key=by_score,reverse=True))
  
if __name__=='__main__':
  main()