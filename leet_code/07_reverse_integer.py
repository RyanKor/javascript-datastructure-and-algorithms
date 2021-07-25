# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        # solution 1
        result = ''
        if x < 0:
            result = str(x)[0] + str(x)[1:][::-1]
        else:
            result = str(x)[::-1]

        if int(result) < -2**31 or int(result) > 2**31 - 1:
            return 0
        return int(result)


# solution 2
#         newArr = []
#         isNegative = False

#         if (x < 0):
#             isNegative = True
#             x = -x

#         while (x > 0):
#             lastDigit = x % 10
#             newArr.insert(0, lastDigit)
#             x //= 10

#         result = 0
#         multiplier = 1
#         for num in newArr:
#             result += num  * multiplier
#             multiplier *= 10

#         if isNegative:
#             result = -result

#         if (result < -2**31 or result > 2**31-1):
#             return 0

#         return result