'''
문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.

출력
첫째 줄에 N!을 출력한다.

*주의사항*
- 팩토리얼 알고리즘을 이전에도 몇 번이나 봤는데 지금 못 푸는 것은 내가 이전에도 답을 찾아서 문제를 풀었기 때문이다.
- 코드를 작성할 때, 항상 충분히 생각해보고 답을 찾자 (최소 문제 푸는데 20분은 들여야한다.)
'''

import sys

factorial_number = int(sys.stdin.readline())


def factorial(n):
    result = 1
    if n == 1 or n == 0:  # 예외처리 조심하기
        return 1

    while True:
        result *= n
        # 이것도 어떻게 보면 동적 프로그래밍 방법의 일환인가? 이전에 곱했던 값을 특정 변수에서 저장해 기억하고 있으니?
        n -= 1
        if n == 1:
            return result
            break


print(factorial(factorial_number))
