# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solution1 : this is not the efficient solution
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # solution2 : Hash Table
        dic = {}
        for idx, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], idx]
            dic[num] = idx
