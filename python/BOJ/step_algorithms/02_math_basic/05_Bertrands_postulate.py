'''
문제
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.

입력의 마지막에는 0이 주어진다.

출력
각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

항상 주어진 조건을 잘 봐야한다.
'''
import sys

# 첫번째 방법 -> 에라토스테네스의 채를 그대로 이용한다 / 시간 초과가 나왔다??

# def isPrime(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True

# while True:
#     cnt = 0
#     N = int(sys.stdin.readline())
#     if N != 0:
#         for i in range(N+1, 2*N+1):
#             if isPrime(i):
#                 cnt += 1
#         print(cnt)
#     else:
#         break


N = 123456 * 2 + 1  # 미리 주어질 값의 최대 범위까지 모든 소수를 구해 놓는다.
sieve = [True] * N
for i in range(2, int(N**0.5)+1):
    if sieve[i]:  # i가 소수면
        for j in range(2*i, N, i):  # i의 배수는 모두 소수가 아니므로 걸러낸다.
            sieve[j] = False


def prime_cnt(val):
    cnt = 0
    for i in range(val + 1, val * 2 + 1):
        if sieve[i]:
            cnt += 1
    print(cnt)


while True:
    val = int(sys.stdin.readline())
    if val == 0:
        break
    prime_cnt(val)
