import sys
from itertools import permutations

# 내 정답 --> 정상 작동 https://www.acmicpc.net/problem/15650
# N, M = map(int, sys.stdin.readline().split())
# temp = list(permutations(range(1,N+1),M))
# answer = []
# for i in temp:
#     arr = sorted(i)
#     answer.append(tuple(arr))
# answer = list(set(answer))
# answer.sort()
# for i in answer:
#     print(*i)

N, M = map(int, input().split())
visited = [False] * N
out = []

def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(depth+1, i+1, N, M)
            visited[i] = False
            out.pop()
solve(0, 0, N, M)