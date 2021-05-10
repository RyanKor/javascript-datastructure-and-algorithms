import sys

n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
max_num = max(score)
result = []
for i in score:
    result.append((i/max_num) * 100)

print(sum(result)/n)

# print(max_num)
