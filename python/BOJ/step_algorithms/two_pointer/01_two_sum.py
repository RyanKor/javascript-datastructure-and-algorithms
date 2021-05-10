'''
문제
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

출력
문제의 조건을 만족하는 쌍의 개수를 출력한다.
'''
import sys
test_case = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

answer = int(sys.stdin.readline())

result = 0
# 방법 1 -> 시간초과 에러가 나온다.
# for i in range(test_case):
#     for j in range(i, test_case):
#         if arr[i] + arr[j] == answer:
#             result += 1


# 방법 2 -> 시간 초과 에러가 나온다
# i = 0
# j = 0

# while True:

#     if arr[i] + arr[j] == answer:
#         result += 1
#         j += 1
#     else:
#         j += 1
#     if j == len(arr):
#         i += 1
#         j = i + 1
#     if i == len(arr) - 1:
#         break
# print(result)

arr.sort()  # 정렬을 해야... 연산 속도가 훨씬 줄어드네...?
left, right = 0, len(arr) - 1

while left < right:
    tmp = arr[left] + arr[right]
    if tmp == answer:
        result += 1
    if tmp < answer:
        left += 1
        continue
    right -= 1
print(result)
