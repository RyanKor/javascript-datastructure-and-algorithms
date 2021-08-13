# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        for word in words:
            if s:
                if s.startswith(word):
                    s = s[len(word):]
                else:
                    return False

        if not s:
		    # for the case when len(s) > len(len(words[0])......len(words[n-1])
            return True

        return False