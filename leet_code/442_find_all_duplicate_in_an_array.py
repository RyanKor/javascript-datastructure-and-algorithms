# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        return [key for key, value in Counter(nums).items() if value == 2]