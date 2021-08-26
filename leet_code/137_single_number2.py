# https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        find_one = Counter(nums)
        for key, value in find_one.items():
            if value == 1:
                return key