# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == len(nums):
            return nums
        if k > len(nums):
            share = k % len(nums)
            nums[:] = nums[-share:] + nums[:-share]
        else:
            nums[:] = nums[-k:] + nums[:-k]