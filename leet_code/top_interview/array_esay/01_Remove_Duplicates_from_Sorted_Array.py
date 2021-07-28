# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)