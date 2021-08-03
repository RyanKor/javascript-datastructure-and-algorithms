# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2" : "abc", "3" : "def", "4" : "ghi",
            "5" : "jkl", "6" : "mno", "7" : "pqrs",
            "8" : "tuv", "9" : "wxyz" 
        }
        result = []
        def dfs(idx, words):
            
            if len(words) == len(digits):
                result.append(words)
                return
        
            for i in range(idx, len(digits)):
                for j in phone[digits[i]]:
                    dfs(i+1, words + j)
                    
        if digits == "":
            return []
        
        dfs(0,"")
        
        return result
            