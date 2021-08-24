# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # solution1
#         dic = dict()
#         for i in range(len(s)): dic[indices[i]] = s[i]
#         dic = dict(sorted(dic.items(), key=lambda x : x[0]))
        
#         return ''.join(dic.values())

        # solution2
        lst = [None]*len(s)
        for i in range(len(indices)):
            lst[indices[i]]=s[i]
        return ''.join(lst)