import sys
temp = []
i = 0
while True:
    num = int(sys.stdin.readline())
    temp.append(num)
    i += 1
    if i == 9:
        break

print(max(temp), temp.index(max(temp))+1)
