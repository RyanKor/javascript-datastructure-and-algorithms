# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums.count(0) == len(nums):
            return nums
        zero = []
        not_zero = []
        for i in nums:
            if i == 0:
                zero.append(i)
            else:
                not_zero.append(i)
        nums[:] = not_zero + zero
