# https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution:
    def countSegments(self, s: str) -> int:
        if s=="": 
            return 0
        return len(s.split())