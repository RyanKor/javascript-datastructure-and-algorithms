# https://www.acmicpc.net/problem/1676
import sys

n = int(sys.stdin.readline().rstrip())
k,p=0,5
while(n>=p):
    k,p=k+n//p,p*5
print(k)  