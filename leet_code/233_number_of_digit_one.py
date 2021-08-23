# https://leetcode.com/problems/number-of-digit-one/
class Solution:
    def countDigitOne(self, n: int) -> int:
        # solution 1 : Time Exeeded
        # answer = 0
        # for i in range(n + 1):
        #     answer += str(i).count('1')
        # return answer
        
        # solution 2: very fast & correct answer
        if n < 1: return 0

        # i = 0
        p = 1 # 10 ** i
        c = 0 # count of 1s less than 10 ** i
        
        result = 0
        for char in str(n)[::-1]:
            d = int(char)
            # if d == 0: pass
            if d == 1:
                result += c + n%(p) + 1
            elif d > 1:
                result += p + d*c
            c += p + (c<<3)+c # c = p + 8*c + c
            p = (p<<3)+2*p # p *= 10
            # i += 1
        return result