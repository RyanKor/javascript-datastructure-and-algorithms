# https://leetcode.com/problems/concatenation-of-array/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # return [nums[i] for i in range(len(nums))] * 2
        return nums * 2