# https://leetcode.com/problems/three-divisors/

class Solution:
    def isThree(self, n: int) -> bool:
        divisors = []
        divisors_back = [] 

        for i in range(1, int(n**(1/2)) + 1): 
            if (n % i == 0):            
                divisors.append(i)
                if (i != (n // i)): 
                    divisors_back.append(n//i)
        if len(divisors + divisors_back[::-1]) == 3:
            return True
        return False