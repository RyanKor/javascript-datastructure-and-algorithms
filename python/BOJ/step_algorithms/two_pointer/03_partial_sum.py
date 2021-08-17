# https://www.acmicpc.net/problem/1806

import sys

n, m = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))

i,j = 0,0
answer = sys.maxsize
temp_sum = 0
while True:
   if temp_sum >= m:
       answer = min(answer, j - i)
       temp_sum -= lst[i]
       i += 1

   elif j == n:
       break

   else:
       temp_sum += lst[j]
       j += 1

if answer == sys.maxsize:
   print(0)
else:
   print(answer)