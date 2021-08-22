# https://leetcode.com/problems/perfect-number/
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        divisors = []
        divisors_back = []
        for i in range(1, int(sqrt(num)) + 1): 
            if (num % i == 0):            
                divisors.append(i)
                if i != (num // i) and num != (num // i) : 
                    divisors_back.append(num//i)
        return sum(divisors) + sum(divisors_back) == num