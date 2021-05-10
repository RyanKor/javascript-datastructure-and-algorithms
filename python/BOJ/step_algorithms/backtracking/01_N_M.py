'''
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

백트래킹 문제로, 단순히 itertools를 사용해서 중복되지 않는 순열을 작성하는 코드가 아니다.
'''
import sys
from itertools import permutations
N, M = map(int, sys.stdin.readline().split())
answer = list(permutations(range(1,N+1),M))
for i in answer:
    print(*i)
# num_list = [i + 1 for i in range(N)]
# check_list = [False] * N

# arr = []


# def dfs(cnt):
#     # 주어진 개수만큼 채워지면 출력한다
#     if(cnt == M):
#         print(*arr)
#         return

#     for i in range(0, N):
#         if(check_list[i]):
#             continue

#         # i번째는 거쳐갈거라서 True로 바꾼다.
#         check_list[i] = True
#         arr.append(num_list[i])
#         # 현재의 i를 기준으로 가지치기 시작
#         dfs(cnt + 1)
#         # 이 부분은
#         arr.pop()
#         # 여기서 print(arr)을 해보면 작동원리를 알 수 있다.
#         # print(arr)
# #         print(check_list)
#         check_list[i] = False


# dfs(0)
