# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if i != 0 and digits[i] >= 10:
                temp = digits[i]
                digits[i] %= 10
                digits[i - 1] += temp // 10
        if digits[0] >= 10:
            temp = digits[0]
            digits[0] %= 10
            digits.insert(0, temp // 10)
        return digits