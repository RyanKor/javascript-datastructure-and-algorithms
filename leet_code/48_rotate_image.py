# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # solution 1 : use Nested Loop
#         answer = []
#         for i in range(len(matrix)):
#             temp = []
#             for j in range(len(matrix)-1,-1,-1):
#                 temp.append(matrix[j][i])
#             answer.append(temp)
                
#         matrix[:] = answer[:]

        # solution 2 : use zip built-in function
        matrix[:] = list(zip(*matrix[::-1]))