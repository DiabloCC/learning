# -*-coding:utf8 -*-
# qpy:3
# qpy:console
# kata3_MakeASpiral.py

def headto(canvas, rail, dx, dy):
  if dx != 0:
    if (rail[0]+dx==-1) or (rail[0]+dx==len(canvas)) or (canvas[rail[1]][rail[0]+dx*2]=='1'):
      dx, dy = dy, dx
    return [rail[0]+dx,rail[1]+dy]
  elif (rail[1]+dy==-1) or (rail[1]+dy==len(canvas)) or (canvas[rail[1]+dy*2][rail[0]]=='1'):
    dx, dy = dy, dx
    return [rail[0]+dx,rail[1]+dy]

def flip(canvas):
  return 
   
def spiralize(size):
  if size == 1:
    return [[1]]
  if size == 2:
    return [[1,1],[0,1]]
  r = spiralize(size-2)
  r[0].insert(0,1)
  r[0].insert(0,1)
  for i in range(1,size-2):
    r[i].insert(0,0)
    r[i].insert(0,1)
  r.append([1])
  for i in range(size-1):
    r[-1].append(0)
  r.append([])
  for i in range(size):
    r[-1].append(1)
  return [x[::-1] for x in r][::-1]
  
def spitalize1(size):
  dx, dy = {"left":(-1,0),
            "right":(1,0),
            "up":(0,-1),
            "down":(0,1)}[direction]
  
  # build empty canvase
  c = []
  for i in range(size):
    r.append([])
    for j in range(size):
      r[-1].append('0')
  rail = [0,0]
  while rail:
    c[rail[1]][rail[0]] = '1'
    rail = headto(c,rail,dx,dy)
  return c

def main():
  size = input('input a number')
  for i in spiralize(size):
    print(i)
    
if __name__=='__main__':
  main()
