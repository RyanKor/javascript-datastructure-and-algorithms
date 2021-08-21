# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
        # 1. 소수를 구하고자 하는 구간의 모든 수를 나열
        sieve = [1] * n

        # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
        m = int(n ** 0.5)
        for i in range(2, m + 1):
            if sieve[i] == 1:           # i가 소수인 경우
                sieve[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)
                # for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                #     sieve[j] = False

        # 소수 목록 산출
        if n <2: return 0
        return sum(sieve) - 2
