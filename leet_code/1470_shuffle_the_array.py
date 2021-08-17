# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # first = nums[:n]
        # second = nums[n:]
        # answer = []
        # for i in range(n):
        #     answer.append(first[i])
        #     answer.append(second[i])
        # return answer
        
        return [j for i in zip(nums[:n], nums[n:]) for j in i]