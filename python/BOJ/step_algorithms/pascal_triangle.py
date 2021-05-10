import sys

n, k = map(int, sys.stdin.readline().split())


result = [[1]]
for i in range(1, n):
    temp = []
    for j in range(i+1):
        if j == 0 or j == i: # 처음과 끝의 1 배치
            temp.append(1)
        else:
            temp.append(result[i-1][j-1] + result[i-1][j])
    result.append(temp)
print(result[n-1][k-1])