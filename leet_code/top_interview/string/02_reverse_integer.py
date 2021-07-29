# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/


class Solution:
    def reverse(self, x: int) -> int:
        negative_trigger = False
        answer = 0
        if x < 0:
            negative_trigger = True
            x = abs(x)

        while x != 0:
            answer = answer * 10 + x % 10
            x //= 10

        if answer < -(1 << 31) or answer > (1 << 31) - 1:
            return 0

        if negative_trigger:
            return -answer

        return answer