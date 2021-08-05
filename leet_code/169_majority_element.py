# https://leetcode.com/problems/majority-element/

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return [n for n in cnt if cnt[n] > len(nums)/2][0]