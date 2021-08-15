# https://leetcode.com/problems/maximum-number-of-words-you-can-type/
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split()
        cnt=0
        for i in text:
            flag=1
            for j in brokenLetters:
                if j in i:
                    flag=0
                    break
            cnt+=flag

        return cnt