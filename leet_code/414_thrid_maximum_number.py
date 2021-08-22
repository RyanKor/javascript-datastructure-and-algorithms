# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3 or len(set(nums)) < 3: return max(nums)
        return sorted(list(set(nums)))[-3]