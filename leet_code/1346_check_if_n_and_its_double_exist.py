# https://leetcode.com/problems/check-if-n-and-its-double-exist/
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        lst = Counter(arr)
        if lst[0] > 1: return True
        if 0 in lst: lst.pop(0)
        for a in arr:
            if 2*a in lst: return True
        return False