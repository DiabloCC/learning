# ThinkPython
# tp0401_turtle.py

import turtle
import math

def square(t):
	for i in range(4):
		t.fd(100)
		t.rt(90)

def square2(t, length):
	for i in range(4):
		t.fd(length)
		t.rt(90)

def polygon(t, length, n, angle):
	for i in range(n):
		t.fd(length)
		t.rt(angle/n)

def circle(t, r):
  l = 2 * math.pi * r
  n = int(l / 50) + 1
  polygon(t, l/n, n, 360.0)

def arc(t, r, angle):
	l = 2 * math.pi * r * angle / 360
	n = int(l / 40) + 1
	polygon(t, l/n, n, angle)

if __name__ == '__main__':
	bob = turtle.Turtle()
	#circle(bob, 100)
	arc(bob, 100, 360)
	turtle.mainloop()


