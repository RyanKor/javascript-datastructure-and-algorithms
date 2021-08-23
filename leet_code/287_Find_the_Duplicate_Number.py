# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for key,value in Counter(nums).items():
            if value > 1:
                return key
            