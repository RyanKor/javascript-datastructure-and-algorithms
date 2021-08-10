# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # solution 1
        # lst = range(len(nums) + 1)
        # for i in lst:
        #     if i not in nums:
        #         return i
        
        # solution 2
        # return ((len(nums) + 1) * len(nums)) // 2 - sum(nums)
        		
        # solution 3
        # res = 0
        # for i in range(1, len(nums)+1):
        #     res = res ^ i ^ nums[i-1]
        # return res
        
        # solution 4
        return sum(range(len(nums) + 1)) - sum(nums)