# -*-coding:utf8 -*-
# qpy:3
# qpy:console
# kata3_MakeASpiral.py

# maxium recursive error  
def spiralize1(size):
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
  

  
def spiralize(size):
  if size == 0:
      return []
  
  c = []
  for i in range(size):
    c.append([0 for j in range(size)]) 
  status = [(1,0),(0,1),(-1,0),(0,-1)]
  cornercount = 0
  row = col = 0 

  def calgrid():
    if row == -1 or row == size or col == -1 or col == size:
      return -1
    up = 0 if row == 0 else c[row-1][col]
    down = 0 if row == size-1 else c[row+1][col]
    left = 0 if col == 0 else c[row][col-1]
    right = 0 if col == size-1 else c[row][col+1]
    return up + down + left + right
 
  dx, dy = status[cornercount % 4]
  while True:
    c[row][col] = 1
    row += dy
    col += dx
    if calgrid() != 1:
      row -= dy
      col -= dx
      cornercount += 1
      dx, dy = status[cornercount % 4]
      row += dy
      col += dx
      if calgrid() != 1:
        break
  return c

# other's work
def spiralize2(size):
    
    def on_board(x, y):
        return 0 <= x < size and 0 <= y < size
        
    def is_one(x, y):
        return on_board(x, y) and spiral[y][x] == 1
        
    def can_move():
        return on_board(x+dx, y+dy) and not (is_one(x+2*dx, y+2*dy) or is_one(x+dx-dy, y+dy+dx) or is_one(x+dx+dy, y+dy-dx))
    
    
    spiral = [[0 for x in range(size)] for y in range(size)]   
    x, y = -1, 0
    dx, dy = 1, 0
    turns = 0
    
    while (turns < 2):
        if can_move():
            x += dx
            y += dy
            spiral[y][x] = 1
            turns = 0
        else:
            dx, dy = -dy, dx
            turns += 1
    
    return spiral

def spiralize3(size):
    spiral = [[1]*size for _ in xrange(size)]
    def ok(y, x):
        return y < size and x < size and y >= 0 and x >= 0 and spiral[y][x]
    y, x, dy, dx = 1, -1, 0, 1
    while ok(y + dy, x + dx):
        if ok(y + 2*dy, x + 2*dx):
            y += dy
            x += dx
        else:
            dx, dy = dy*(2*dx-1), dx
        spiral[y][x] = 0
    return spiral

def spiralize4(size):
    # Make a snake
    spiral = [[1 - min(i,j,size-max(i,j)-1)%2 for j in xrange(size)] for i in xrange(size)]
    for i in xrange(size/2-(size%4==0)):
      spiral[i+1][i] = 1 - spiral[i+1][i]
    return spiral

def main():
  # size = input('input a number')
  for i in spiralize(10):
    print(i)
    
if __name__=='__main__':
  main()
