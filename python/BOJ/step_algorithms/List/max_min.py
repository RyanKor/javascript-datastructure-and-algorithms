import sys

num = int(sys.stdin.readline())
lst = sorted(map(int, sys.stdin.readline().split()))

print(lst[0], lst[-1])
