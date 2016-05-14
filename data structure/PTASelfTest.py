# -*- coding: utf-8 -*-
# PTAST001_shalou.py

import math

def shalou(num, mark):
  n = int(math.sqrt((num+1)/2)) - 1
  for i in range(n,-1,-1):
    print(' '*(n-i)+mark*(2*i+1))
  for i in range(1,n+1):
    print(' '*(n-i)+mark*(2*i+1))
  print(num-(n+1)**2*2+1)

def sushudui(num):
  # get pime list
  s = [x for x in range(3,num+1,2) if x%6==1 or x%6==5]
  n = num**0.5
  for i,v in enumerate(s):
    if v<=n:
      s = s[:i+1]+[x for x in s[i+1:] if x%v != 0 and x != v]
    else: break
  s = [3]+s
  for i in range(0,len(s)-1):
    s[i] = s[i+1]-s[i]
  print(s.count(2))
 
  # print(len(s))
  # print(s)




def main():
  # s=input().split(' ')
  # shalou(int(s[0]),s[1])
  sushudui(7)


if __name__ == '__main__':
  main()
