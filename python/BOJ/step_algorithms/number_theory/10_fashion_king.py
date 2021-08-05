# https://www.acmicpc.net/problem/9375
import sys

num = int(sys.stdin.readline().rstrip())

for i in range(num):
    n = int(sys.stdin.readline().rstrip())
    dic = {}
    for i in range(n):
        m,k = sys.stdin.readline().split()
        if k in dic:
            dic[k] +=1
        else:
            dic[k] = 1
    answer = 1
    for key, value in dic.items():
        answer *= (value + 1)
    print(answer - 1)