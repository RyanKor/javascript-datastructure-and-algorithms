# https://leetcode.com/problems/string-to-integer-atoi/

import re


class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r'^\s*([+|-]?\d+)', s)

        if match:
            integer = int(match.group())
            return max(-(1 << 31), min(integer, (1 << 31) - 1))
        # 1<<31 == 2**31 / bit연산자를 사용해 결과값 도출
        return 0