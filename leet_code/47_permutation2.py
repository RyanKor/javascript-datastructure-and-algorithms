# https://leetcode.com/problems/permutations-ii/submissions/

from itertools import permutations


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        lst = list(permutations(nums, len(nums)))
        # 생각보다 set을 사용한 연산법이 속도가 빠르지 않다. (정답은 맞다.)
        # 더 빠른 연산에 대해 정답을 작성해 넣자.
        lst = list(set(lst))
        return lst