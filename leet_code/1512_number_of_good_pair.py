# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
#         if len(nums) == len(set(nums)):
#             return 0
#         answer = 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     answer +=1
        
#         return answer
        dic = Counter(nums)
        count= 0
        for val in dic.values():
            count+= (val*(val-1))//2
        return count