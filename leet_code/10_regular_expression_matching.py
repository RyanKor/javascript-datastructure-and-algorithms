# https://leetcode.com/problems/regular-expression-matching/

import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        comp = re.compile(p)
        boolean = comp.findall(s)  # 결과 값 list로 매칭되는 것 반환.
        for i in boolean:
            if i == s:
                return True
        return False