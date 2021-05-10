'''
문제
자연수 과 정수 가 주어졌을 때 이항 계수 
를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 4,000,000, 0 ≤  ≤ )

출력
 
를 1,000,000,007로 나눈 나머지를 출력한다.
'''
# 페르마의 소정리 이용
import sys
# 분할 정복을 이용하여 a^b를 구한다.


def power(a, b):
    if b == 0:
        return 1
    if b % 2:  # 홀수이면
        return (power(a, b // 2) ** 2 * a) % p
    else:
        return (power(a, b // 2) ** 2) % p


p = 1000000007
N, K = map(int, sys.stdin.readline().split())

# nCk를 나타내기 위해 팩토리얼을 dp로 구해줍니다.
fact = [1 for _ in range(N + 1)]

for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % p

# A는 nCk의 분자가되고 B는 분모가 됩니다.
A = fact[N]
B = (fact[N - K] * fact[K]) % p

# 여기서 페르마의 소정리가 사용됨
print((A % p) * (power(B, p - 2) % p) % p)
