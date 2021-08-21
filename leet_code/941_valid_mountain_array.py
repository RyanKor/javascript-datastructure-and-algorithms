# https://leetcode.com/problems/valid-mountain-array/
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if max(arr) == arr[0] or max(arr) == arr[-1] : return False
        idx = arr.index(max(arr))
        half = arr[:idx]
        end = arr[idx:]

        for i in range(1, len(half)):
            if half[i-1] >= half[i]:
                return False
        
        for i in range(1, len(end)):
            if end[i-1] <= end[i]:
                return False
            
        return True