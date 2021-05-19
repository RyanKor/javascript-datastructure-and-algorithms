import sys


n = int(sys.stdin.readline())
lst = []
for i in range(n):
    case = list(map(int,sys.stdin.readline().split()))
    lst.append(case)
for i in range(1, n):
    for j in range(len(lst[i])):
        if j == 0:
            lst[i][j] += lst[i-1][j]
        elif j==i:
            lst[i][j] +=lst[i-1][j-1]
        else :
            lst[i][j] += max(lst[i-1][j],lst[i-1][j-1])
print(max(lst[n-1]))
