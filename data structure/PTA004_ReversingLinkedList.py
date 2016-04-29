# -*- coding: utf-8 -*-
# PTA004_ReversingLinkedList.py

def sortList(s,head):
  addr = [i[0] for i in s]
  r = []
  while head != '-1':
    r.append(s[addr.index(head)])
    head = r[-1][2]
  return r

def reverseList(s,k):
  r= [[0,0,0]]
  for i in range(0, len(s) - len(s) % k, k):
    r1 = [[s[j][0],s[j][1],s[j-1][0]] for j in range(i+k-1,i,-1)] + [s[i]]
    r[-1][2] = r1[0][0]
    r += r1
  if len(s) % k != 0:
    r[-1][2] = s[-(len(s) % k)][0]
    r += s[-(len(s) % k):]
  r[-1][2] = '-1'
  return r[1:]

def reverseList1(s,k):
  r = []
  for i in range(0,len(s) - len(s) % k, k):
    r += s[i:i+k][::-1]
  if len(s) % k != 0:
    r += s[-(len(s) % k):]
  for i in range(len(r)-1):
    r[i][2] = r[i+1][0]
  r[-1][2] = '-1'
  return r

def sortList2(s,head):
  addr = [i[0] for i in s]
  r = [['0',0,0,0]]
  while head != '-1':
    r.append(s[addr.index(head)]+[r[-1][0]])
    head = r[-1][2]
  return r[1:]

def reverseList2(s,k):
  r= [[0,0,0]]
  for i in range(0, len(s) - len(s) % k, k):
    r1 = [[s[j][0],s[j][1],s[j][3]] for j in range(i+k-1,i-1,-1)]
    r[-1][2] = r1[0][0]
    r += r1
  if len(s) % k != 0:
    r[-1][2] = s[-(len(s) % k)][0]
    r += s[-(len(s) % k):]
  r[-1][2] = '-1'
  return r[1:]

def main():
  from time import clock
  s = [['00100','6','3'],['00000','4','99999'],['00100','1','12309'],['68237','6','-1'],['33218','3','00000'],['99999','5','68237'],['12309','2','33218']]
  s1 = sortList(s[1:],s[0][0])
  for i in s1:
    print(' '.join(i))
  print('---------------------')
  print('-----reverseList-----')
  clock()
  s2 = reverseList(s1,int(s[0][2]))
  print('time =', clock())
  for i in s2:
    print(' '.join(i))
  print('-----reverseList1-----')
  clock()
  s2 = reverseList1(s1,int(s[0][2]))
  print('time =', clock())
  for i in s2:
    print(' '.join(i))
  s = [['00100','6','3'],['00000','4','99999'],['00100','1','12309'],['68237','6','-1'],['33218','3','00000'],['99999','5','68237'],['12309','2','33218']]
  s1 = sortList2(s[1:],s[0][0])
  print('-----reverseList2-----')
  clock()
  s2 = reverseList2(s1,int(s[0][2]))
  print('time =', clock())
  for i in s2:
    print(' '.join(i))

def main1():
  s = []
  s.append(input().split(' '))
  for i in range(int(s[0][1])):
    s.append(input().split(' '))
  s1 = reverseList(sortList(s[1:],s[0][0]),int(s[0][2]))
  for i in s1:
    print(' '.join(i))

def main2():
  t = input().split(' ')
  s1 = []
  s2 = []
  for i in range(int(t[1])):
    l = input().split(' ')
    s1.append([l[0],l[1]])
    s2.append([l[0],l[2]])
  d1 = dict(s1)
  d2 = dict(s2)


if __name__ == '__main__':
  main()