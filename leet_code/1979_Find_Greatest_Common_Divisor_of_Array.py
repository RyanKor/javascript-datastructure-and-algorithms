# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        def gcd(x,y):
            while y > 0:
                x, y = y, x % y
            return x
        
        return gcd(min(nums),max(nums))
        
                