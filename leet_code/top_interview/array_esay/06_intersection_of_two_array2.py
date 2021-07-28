# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        result = []
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        for i in nums1:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for i in nums2:
            if i in dic and dic[i]:
                dic[i] -= 1
                result.append(i)
        return result