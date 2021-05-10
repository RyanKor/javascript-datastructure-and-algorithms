# import sys
# from itertools import product

# 내 정답 --> 메모리 초과 (정답은 맞는 것 같은데, 공간 복잡도 통과가 안된 듯하다.)
# N, M = map(int, sys.stdin.readline().split())
# temp = list(product(range(1,N+1),repeat=M))
# answer = []
# for i in temp:
#     arr = sorted(i)
#     answer.append(tuple(arr))
# answer = list(set(answer))
# answer.sort()
# for i in answer:
#     print(*i)

N, M = map(int, input().split())
out = []

def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        out.append(i+1)
        solve(depth+1, i, N, M)
        out.pop()

solve(0, 0, N, M)