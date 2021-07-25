# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        answer = 0
        copy = x
        # 101 -> 1 * (10 ** 2) + 0 * (10 ** 1) + 1 * (10 ** 0)
        if x < 0:
            return False
        while copy != 0:
            temp = copy % 10
            answer = answer * 10 + temp
            copy //= 10
        if answer == x:  # x becomes 0 after the while loop
            return True
        return False