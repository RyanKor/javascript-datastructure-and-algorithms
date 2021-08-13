# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alphabet = {}
        cnt = 0
        for i in range(ord("a"),ord("j")+1):
            alphabet[chr(i)] = cnt
            cnt+=1
            
            firstWord = firstWord.replace(chr(i), str(alphabet[chr(i)]))
            secondWord = secondWord.replace(chr(i), str(alphabet[chr(i)]))
            targetWord = targetWord.replace(chr(i), str(alphabet[chr(i)]))

        return int(firstWord) + int(secondWord) == int(targetWord) 
                

