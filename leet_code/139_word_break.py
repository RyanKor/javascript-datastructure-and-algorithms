# https://leetcode.com/problems/word-break/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_length = [len(a) for a in wordDict]
        result = [False] * (len(s) + 1)
        result[0] = True
        for i in range(len(s)):
            if result[i]:
                for j in range(len(word_length)):
                    if s[i : i + word_length[j]] == wordDict[j]:
                        result[i + word_length[j]] = True
        return result[-1]