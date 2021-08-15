# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = Counter(s)
        if len(set(cnt.values())) == 1:
            return True
        
        return False