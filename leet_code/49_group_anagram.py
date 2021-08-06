# https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for w in strs:
            temp = ''.join(sorted(w))
            if temp in dic:
                dic[temp].append(w)
            else:
                dic[temp] = [w]
        return list(dic.values())