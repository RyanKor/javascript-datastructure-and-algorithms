import sys

# for i in range(1, int(sys.stdin.readline().rstrip())+1):
#     print("*"*i)


cnt = int(sys.stdin.readline().rstrip())
i = 1
while True:
    print(" "*(cnt-1) + "*"*i)
    cnt -= 1
    i += 1
    if (cnt == 0):
        break
