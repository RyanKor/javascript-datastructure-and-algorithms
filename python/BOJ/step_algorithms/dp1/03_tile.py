# https://www.acmicpc.net/problem/1904
import sys
from itertools import product

n = int(sys.stdin.readline())
# 첫번째 문제 풀이 -> 메모리 초과
# binary = ['0','1']
# answer = []
# if n == 1:
#     print(1)
# if n == 2:
#     print(2)

# arr = list(product(binary,repeat=n))
# for i in arr:
#     temp = ''.join(i)
#     if temp.count('0') % 2 !=0:
#         pass
#     elif '00' in temp:
#         answer.append(temp)
#     elif temp.count('1') == n:
#         answer.append(temp)
# print(len(answer))

def tile (n):
    answer = [0,1,2]
    if n == 1 or n == 2:
        return answer[n]
    else:
        for i in range(3, n+1):
            answer.append((answer[i-2] + answer[i-1])%15746)
    return answer[n] 

print(tile(4))