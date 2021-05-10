import sys

num = int(sys.stdin.readline())
temp = score = 0
for i in range(num):
    ox = sys.stdin.readline()
    for j in ox:
        if j == 'O':
            temp += 1
            score += temp
        else:
            temp = 0
    print(score)
    score = 0
