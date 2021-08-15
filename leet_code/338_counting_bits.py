# https://leetcode.com/problems/counting-bits/
class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = range(n+1)
        answer = [bin(i)[2:].count("1") for i in lst]
            
        return answer