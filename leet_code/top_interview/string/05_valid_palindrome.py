# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        comp = re.compile("[a-zA-Z0-9]")
        alphabet = comp.findall(s)
        alphabet = ''.join(alphabet).lower()
        if alphabet == alphabet[::-1]:
            return True
        return False