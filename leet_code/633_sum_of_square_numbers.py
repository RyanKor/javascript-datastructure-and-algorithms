# https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        pointer = int(c ** 0.5)
        left = 0
        right = pointer
        while left <= right:
            res = left ** 2 + right ** 2
            if res == c:
                return True
            elif res < c:
                left += 1
            elif res > c:
                right -= 1
        return False