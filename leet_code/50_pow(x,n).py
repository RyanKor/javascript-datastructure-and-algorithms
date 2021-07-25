# https://leetcode.com/problems/powx-n/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # solution1 --> 단순한 제곱 연산
        # return x ** n
        # solution2 --> 내장함수를 사용한 풀이가 연산속도가 훨씬 빠르다. 상위 90% 이상이다.
        return pow(x, n)
