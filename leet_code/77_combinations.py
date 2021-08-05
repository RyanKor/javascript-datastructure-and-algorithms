from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # return list(combinations(range(1,n+1),k))
        result = []
        
        def dfs(element, start, k):
            if k == 0:
                result.append(element[:])
                return
            
            for i in range(start, n+1):
                element.append(i)
                dfs(element, i+1, k-1)
                element.pop()
        
        dfs([],1,k)
        return result