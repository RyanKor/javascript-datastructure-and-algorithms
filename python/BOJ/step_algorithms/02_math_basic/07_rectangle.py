import sys

x,y,w,h = map(int, sys.stdin.readline().split())

left = (0,0)
right = (w,h)
hansu = (x,y)
x_min = min(abs(0-x),abs(w-x))
y_min = min(abs(0-y),abs(h-y))

print(min(x_min,y_min))