import sys
cnt = []
for i in range(10):
    num = int(sys.stdin.readline())
    cnt.append(num % 42)

print(len(set(cnt)))
