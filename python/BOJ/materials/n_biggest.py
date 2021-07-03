n = int(input())

for i in range(n):
    test = list(map(int, input().split()))
    test.sort()
    print(test[-3])