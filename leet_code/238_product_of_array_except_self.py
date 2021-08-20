# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        p = 1
        out = []
        
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]
        
        p = 1
        
        for i in range(len(nums) - 1, 0-1,-1):
            out[i] = out[i] * p
            p = p * nums[i]
        
        return out