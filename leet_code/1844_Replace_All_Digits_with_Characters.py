# https://leetcode.com/problems/replace-all-digits-with-characters/
class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        def shift(letter:str, idx:str) -> str:
            return chr(ord(letter) + int(idx))
        
        for i in range(1,len(s),2):
            s[i] = shift(s[i-1], s[i])
        
        return ''.join(s)