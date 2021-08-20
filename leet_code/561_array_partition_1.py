# https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # solution 1
        # nums.sort()
        # answer = 0
        # while len(nums) != 0:
        #     answer += min(nums[:2])
        #     nums[:] = nums[2:]
        # return answer
        
        # solution2
        # return sum(sorted(nums)[::2])
        
        # solution 3
        
        nums.sort()
        pairs = []
        answer = 0
        for i in nums:
            pairs.append(i)
            
            if len(pairs) == 2:
                answer += min(pairs)
                pairs = []
        return answer