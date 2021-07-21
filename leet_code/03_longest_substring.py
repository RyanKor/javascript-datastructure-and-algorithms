# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = []
        if len(set(s)) == 0:
            return 0
        if len(set(s)) == 1:
            return 1
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[j] in s[i:j]:
                    result.append(s[i:j])
                    break
                elif s[j] not in s[i:j] and j == len(s) - 1:
                    result.append(s[i:j] + s[j])
                    break
        result.sort(key=lambda x: len(x))
        return len(result[-1])