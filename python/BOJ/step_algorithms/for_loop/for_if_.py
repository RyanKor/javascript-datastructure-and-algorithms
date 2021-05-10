import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
a = sys.stdin.readline().rstrip().split()
for i in range(n):
    if int(a[i]) < x:
        print(a[i], end=" ")
