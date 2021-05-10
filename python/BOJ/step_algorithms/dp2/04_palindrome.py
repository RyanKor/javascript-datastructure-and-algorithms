'''
문제
명우는 홍준이와 함께 팰린드롬 놀이를 해보려고 한다.

먼저, 홍준이는 자연수 N개를 칠판에 적는다. 그 다음, 명우에게 질문을 총 M번 한다.

각 질문은 두 정수 S와 E(1 ≤ S ≤ E ≤ N)로 나타낼 수 있으며, S번째 수부터 E번째 까지 수가 팰린드롬을 이루는지를 물어보며, 명우는 각 질문에 대해 팰린드롬이다 또는 아니다를 말해야 한다.

예를 들어, 홍준이가 칠판에 적은 수가 1, 2, 1, 3, 1, 2, 1라고 하자.

S = 1, E = 3인 경우 1, 2, 1은 팰린드롬이다.
S = 2, E = 5인 경우 2, 1, 3, 1은 팰린드롬이 아니다.
S = 3, E = 3인 경우 1은 팰린드롬이다.
S = 5, E = 7인 경우 1, 2, 1은 팰린드롬이다.
자연수 N개와 질문 M개가 모두 주어졌을 때, 명우의 대답을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열의 크기 N (1 ≤ N ≤ 2,000)이 주어진다.

둘째 줄에는 홍준이가 칠판에 적은 수 N개가 순서대로 주어진다. 칠판에 적은 수는 100,000보다 작거나 같은 자연수이다.

셋째 줄에는 홍준이가 한 질문의 개수 M (1 ≤ M ≤ 1,000,000)이 주어진다.

넷째 줄부터 M개의 줄에는 홍준이가 명우에게 한 질문 S와 E가 한 줄에 하나씩 주어진다.

출력
총 M개의 줄에 걸쳐 홍준이의 질문에 대한 명우의 답을 입력으로 주어진 순서에 따라서 출력한다. 팰린드롬인 경우에는 1, 아닌 경우에는 0을 출력한다.

동적 프로그래밍 정답 블로그
https://developmentdiary.tistory.com/377
'''
import sys

# 해당 방법은 시간 초과가 발생한다.
# num = int(sys.stdin.readline())

# test = list(sys.stdin.readline().split())

# case = int(sys.stdin.readline())

# for i in range(case):
#     x, y = map(int, sys.stdin.readline().split())
#     if ''.join(test[x-1:y]) == ''.join(test[x-1:y])[::-1]:
#         print(1)
#     else:
#         print(0)

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):  # 길이가 1일때
    dp[i][i] = 1
    if i < N-1 and num_list[i] == num_list[i+1]:  # 길이가 2일때
        dp[i][i+1] = 1


for i in range(1, N):
    for j in range(1, i+1):
        if num_list[i] == num_list[i-j] and dp[i-j+1][i-1] == 1:
            dp[i-j][i] = 1

M = int(sys.stdin.readline())
for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(dp[S-1][E-1])
