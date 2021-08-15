# https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # lst = range(1,len(nums)+1)
        # cnt = Counter(nums)
        # answer = [cnt.most_common(1)[0][0]]
        # for i in lst:
        #     if i not in cnt:
        #         answer.append(i)
        #         break
        # return answer
    
        n = len(nums)
        true_sum = n*(n+1)//2
        actual_sum = sum(nums)
        set_sum = sum(set(nums))
        return [actual_sum - set_sum, true_sum - set_sum]