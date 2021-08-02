import sys

n = int(sys.stdin.readline().rstrip())
cnt = 0
num = []
total = []


def dfs(i, j, num):
    global cnt
    if i < 0 or i >= len(num) or j < 0 or j >= len(num[0]) or num[i][j] != '1':
        return
    cnt += 1
    num[i][j] = '0'

    dfs(i + 1, j, num)
    dfs(i - 1, j, num)
    dfs(i, j + 1, num)
    dfs(i, j - 1, num)


for i in range(n):
    temp = list(sys.stdin.readline())
    num.append(temp)

for i in range(len(num)):
    for j in range(len(num[0])):
        if num[i][j] == '1':
            dfs(i, j, num)
            total.append(cnt)
            cnt = 0
print(len(total))
total.sort()
for i in total:
    print(i)