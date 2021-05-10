import sys
num = int(sys.stdin.readline().rstrip())

for i in range(1, num+1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print("Case #{}:".format(i), str(a) + " +", str(b) + " =", a+b)
