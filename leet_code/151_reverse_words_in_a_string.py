# https://leetcode.com/problems/reverse-words-in-a-string/

import re


class Solution:
    def reverseWords(self, s: str) -> str:
        s = re.sub("[\s]{2,}", ' ', s)
        return ' '.join(s.split()[::-1])
