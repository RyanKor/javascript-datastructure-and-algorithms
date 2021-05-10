import sys

test_case = int(sys.stdin.readline())
result = []
for i in range(test_case):
    num, alpha = sys.stdin.readline().split()
    for j in alpha:
        print(j*int(num), end="")
    print()
