# https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        answer = nums1 + nums2
        answer.sort()
        length = len(answer) // 2
        even = answer[length] + answer[length - 1]
        odd = answer[length]
        if answer == []:
            return float("{0:.5f}".format(0))

        if len(answer) % 2 == 0:
            return float("{0:.5f}".format(even / 2))
        else:
            return float("{0:.5f}".format(odd))