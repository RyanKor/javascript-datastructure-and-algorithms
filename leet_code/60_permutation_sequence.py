# https://leetcode.com/problems/permutation-sequence/

from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        # lst = list(map(list, permutations(range(1,n+1),n)))
        # return ''.join(map(str,lst[k-1]))
    
        nlist = [i for i in range(1, n+1)]
        multiple = [1] * n
        for i in range(1, n):
            multiple[i] = multiple[i-1] * (i+1)
        multiple[:] = multiple[::-1]
        ans = []
        i = 1
        k -= 1
        while k > 0:
            remain = k // multiple[i]
            mod = k % multiple[i]
            i += 1 
            ans.append(nlist[remain])
            del nlist[remain]
            k = mod
        ans.extend(nlist)
        return ''.join([str(i) for i in ans])