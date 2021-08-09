# https://leetcode.com/problems/sqrtx/
from math import sqrt
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))
        # return int(x**0.5)
        # return int(pow(x,0.5))