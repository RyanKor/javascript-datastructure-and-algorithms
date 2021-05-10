'''
문제
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

입력
첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

출력
첫째 줄에 자연수 N의 최댓값을 출력한다.
'''
import sys
num = int(sys.stdin.readline())
result = 0
i = 1
while num > 0:
    num -= i
    if num >= 0:
        result += 1
        i += 1
    else:
        print(result)
        break
