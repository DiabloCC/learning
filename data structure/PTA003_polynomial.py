# -*- coding: utf-8 -*-
# PTA003_polynomial.py

def getPoly(string):
  slist = string.split(' ')
  r = [[int(slist[i+1]),eval(slist[i])] for i in range(1,len(slist)-1,2)]
  r.sort(reverse=True)
  return r

def sortResult(rlist):
  # rlist.sort(reverse=True)
  return [str(x[1])+' '+str(x[0]) for x in rlist]

def sumPoly1(p1,p2):
  if len(p1) == 0:
    return p2
  if len(p2) == 0:
    return p1

  # print(p1)
  # print(p2)
  r = []
  k = 0
  if p1[-1][0]>p2[-1][0]:
    p1, p2 = p2, p1
  for i in p1:
    power1 = i[0]
    # print(power1)
    while k < len(p2):
      power2 = p2[k][0]
      if power2 > power1:
        r.append(p2[k])
        k += 1
      else:
        if power2 == power1:
          r.append([power1,i[1] + p2[k][1]])
          k += 1
        else:
          r.append(i)
        break
    else:
      r.append(i)
  # print(r)
  return r

def multiPoly1(p1, p2):
  # print('p1=',p1)
  # print('p2=',p2)
  r = []
  for i in p1:
    r1 = []
    for j in p2:
      r1 += [[i[0]+j[0],i[1]*j[1]]]
    r1.sort(reverse=True)
    # print('r1=',r1)
    r = sumPoly1(r,r1)
    # print('r=',r)
  return r

def sumPoly(p1,p2):
  r = sortResult(sumPoly1(p1,p2))
  return ' '.join(r)

def multiPoly(p1,p2):
  r = sortResult(multiPoly1(p1,p2))
  return ' '.join(r)

def main():
  # p1 = getPoly(input())
  # p2 = getPoly(input())
  p1 = '4 3 4 -5 2 6 1 -2 0'
  p2 = '3 5 20 -7 4 3 1'
  # print(getPolyorm(p1))
  # print(multiPoly(p1,p2))
  print(multiPoly(getPoly(p1),getPoly(p2)))
  print(sumPoly(getPoly(p1),getPoly(p2)))


if __name__ == '__main__':
  main()