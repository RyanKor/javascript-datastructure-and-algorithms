import sys

num = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))

lst = sorted(lst)

for i in range(1,len(lst)):
    lst[i] = lst[i-1] + lst[i]
print(sum(lst))