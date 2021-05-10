import sys

while True:
    a = list(map(int, sys.stdin.readline().split()))
    if sum(a) ==0:
        break
    max_num = max(a)
    a.remove(max_num)
    if a[0]**2 + a[1]**2 == max_num**2:
        print("right")
    else:
        print("wrong")
    
