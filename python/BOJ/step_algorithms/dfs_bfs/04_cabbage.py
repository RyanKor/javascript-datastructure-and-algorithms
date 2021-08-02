import sys

num = int(sys.stdin.readline().rstrip())


def dfs(i, j, lst):
    if i < 0 or i >= len(lst) or j < 0 or j >= len(lst[0]) or lst[i][j] != 1:
        return
    lst[i][j] = 0

    dfs(i + 1, j, lst)
    dfs(i - 1, j, lst)
    dfs(i, j + 1, lst)
    dfs(i, j - 1, lst)


for i in range(num):
    answer = 0
    m, n, k = map(int, sys.stdin.readline().split())
    lst = [[0] * n for i in range(m)]
    for j in range(k):
        l, r = map(int, sys.stdin.readline().split())
        lst[l][r] = 1
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == 1:
                dfs(i, j, lst)
                answer += 1

    print(answer)