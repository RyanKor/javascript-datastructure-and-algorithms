import sys

x1,y1 = map(int, sys.stdin.readline().split())
x2,y2 = map(int, sys.stdin.readline().split())
x3,y3 = map(int, sys.stdin.readline().split())
result = []
if x1 == x2 and x1 != x3:
    result.append(x3)
    if y2 == y3:
        result.append(y1)
    elif y1 == y3:
        result.append(y2)
elif x1 == x3 and x1 != x2:
    result.append(x2)
    if y2 == y3:
        result.append(y1)
    elif y2 == y1:
        result.append(y3)
elif x2 == x3 and x1 != x2:
    result.append(x1)
    if y1 == y3:
        result.append(y2)
    elif y1 == y2:
        result.append(y3)


print(*result)