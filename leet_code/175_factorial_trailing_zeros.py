# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
# my solution : 4580ms speed
#         memo = [1,2]
#         answer = 1
#         result = 0
#         if n == 0:
#             return n
#         for i in range(len(memo)+1, n+1):
#             answer = memo[-1] * i
#             memo.append(answer)
#             answer = 1
        
#         for i in str(memo[n-1])[::-1]:
#             if i != '0':
#                 return result
#             else:
#                 result +=1
#         return result

# solution2 : other one's answer, 24ms
        k,p=0,5
        while(n>=p):
            k,p=k+n//p,p*5
        return k   