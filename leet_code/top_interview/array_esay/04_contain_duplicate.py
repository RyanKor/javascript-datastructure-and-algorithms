# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for key, value in dic.items():
            if value > 1:
                return True

        return False