# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left:int, right:int)->str:
            # 작은 크기의 palindrome에서부터 큰 크기의 palindrome까지 확장해나가는 형태다.
            while left >= 0 and right <len(s) and s[left] == s[right]:
                left -=1
                right +=1
            return s[left+1:right]
        
        if len(s) == 1 and s == s[::-1]:
            return s
    
        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i+1), expand(i,i+2),key=len)
        return result

        # maxLength = 1

        # start = 0
        # length = len(s)

        # low = 0
        # high = 0

        # # One by one consider every character as center point of
        # # even and length palindromes
        # for i in range(1, length):
        #     # Find the longest even length palindrome with center
        #     # points as i-1 and i.
        #     low = i - 1
        #     high = i
        #     while low >= 0 and high < length and s[low] == s[high]:
        #         if high - low + 1 > maxLength:
        #             start = low
        #             maxLength = high - low + 1
        #         low -= 1
        #         high += 1

        #     # Find the longest odd length palindrome with center
        #     # point as i
        #     low = i - 1
        #     high = i + 1
        #     while low >= 0 and high < length and s[low] == s[high]:
        #         if high - low + 1 > maxLength:
        #             start = low
        #             maxLength = high - low + 1
        #         low -= 1
        #         high += 1

        # return s[start:start + maxLength]