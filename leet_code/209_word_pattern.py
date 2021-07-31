# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        unique_s, unique_p = [], []
        for i in range(len(s)):
            if s[i] in unique_s:
                pass
            else:
                unique_s.append(s[i])

            if pattern[i] in unique_p:
                pass
            else:
                unique_p.append(pattern[i])

        p_answer = ''
        s_answer = ''
        for i in range(len(s)):
            s_answer += str(unique_s.index(s[i]))
            p_answer += str(unique_p.index(pattern[i]))

        if p_answer == s_answer:
            return True

        return False