import sys
while True:
    a = sys.stdin.readline().rstrip().split()
    # 입력 값을 2개로 받지 말고, 하나의 리스트로 받으면 빈 배열 때, break 가능
    if a == []:
        break
    print(int(a[0])+int(a[1]))
