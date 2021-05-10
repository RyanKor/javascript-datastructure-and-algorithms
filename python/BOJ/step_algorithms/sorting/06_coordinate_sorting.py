'''
문제
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
'''
import sys
num = int(sys.stdin.readline().rstrip())
result = []
for i in range(num):
    x, y = map(int, sys.stdin.readline().split())
    result.append([x, y])
result.sort()

# 시간 초과 발생 -> 되도록 정렬 문제를 풀 때는 Nested Loop 사용을 지양하자.
# for i in range(len(result)):
#     for j in range(i+1, len(result)):
#         if result[i][0] > result[j][0]:
#             result[i], result[j] = result[j], result[i]
#         elif result[i][0] == result[j][0] and result[i][1] > result[j][1]:
#             result[i], result[j] = result[j], result[i]
for i in result:
    print(*i)


# 누군가의 답

'''
우선 리스트형태로 입력을 받는다.

lambda를 사용하여 정렬 기준을 정해주는데, 먼저 첫번째 인자(x[0]) 즉, x줄부터 정렬을 하고

그다음 두번째 인자인(x[1]) y줄을 정렬해준다.

순서대로 출력해준다.
'''

# import sys
# n = int(sys.stdin.readline())
# so = []
# for i in range(n):
#     so.append(list(map(int, sys.stdin.readline().split())))
# so.sort(key=lambda x: (x[0], x[1]))
# for i in so:
#     print(i[0], i[1])
