# https://leetcode.com/problems/permutations/

from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 기본적으로 permutations을 사용한 연산이 연산속도가 상당히 빠르다. 상위 99%에 이른다.
        lst = list(permutations(nums, len(nums)))
        return lst

'''
        result = []
        prev = []
        
        def dfs(element):
            if len(element) == 0:
                result.append(prev[:])
                
            for e in element:
                next_element = element[:]
                next_element.remove(e)
                
                prev.append(e)
                dfs(next_element)
                prev.pop()
        
        
        dfs(nums)
        return result
'''