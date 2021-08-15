# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
        digit = ''
        for i in s:
            digit += str(alphabet.index(i)+1)
        
        while k != 0:
            temp = sum([int(i) for i in digit])
            digit = str(temp)
            k -= 1
        
        return int(digit)
        
