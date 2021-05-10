import sys
from itertools import permutations, product

# 내 코드 --> 정상작동 https://www.acmicpc.net/problem/15651
N, M = map(int, sys.stdin.readline().split())
for i in product(range(1,N+1),repeat=M):
    print(*i)
'''
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
'''

# N, M = map(int, input().split())
# out = []

# def solve(depth, N, M):
#     if depth == M:
#         print(' '.join(map(str, out)))
#         return
#     for i in range(N):
#         out.append(i+1)
#         solve(depth+1, N, M)
#         out.pop()

# solve(0, N, M)

import sys
from itertools import product
n,m = map(int, sys.stdin.readline())

for i in product(range(1,N+1), repeat=M):
    print(*i)