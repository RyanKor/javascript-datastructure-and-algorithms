'''
문제
자연수 과 정수 가 주어졌을 때 이항 계수 
를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 10, 0 ≤  ≤ )

출력
 
를 출력한다.
'''
# -*- coding: utf-8 -*-
# # Python 3.4.5
import sys
memo = [0] * 11


def factorial(num):
    if num <= 1:
        memo[num] = 1
        return memo[num]  # 이미 계산된 값
    if memo[num] != 0:
        return memo[num]  # memoization
    memo[num] = num * factorial(num-1)
    return memo[num]


n, k = map(int, sys.stdin.readline().split())
print(factorial(n)//(factorial(k)*factorial(n-k)))
