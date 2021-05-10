import sys

num = int(sys.stdin.readline())
cnt = 0
result = ''
for i in range(num):
    students = list(map(int, sys.stdin.readline().split()))
    temp = int(sum(students[1:]))/int(students[0])
    for j in range(1, int(students[0])+1):
        if students[j] > temp:
            cnt += 1
    result = '%.3f' % ((cnt/int(students[0])*100))
    print(result+"%")
    cnt = 0  # 다음 테스트 케이스 값 확인을 위해 cnt 초기화
