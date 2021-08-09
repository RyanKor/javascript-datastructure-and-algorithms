# https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [[0] * i for i in range(1,rowIndex+2)]
        
        for i in range(len(answer)):
            for j in range(i+1):
                if j == 0 or j == i:
                    answer[i][j] = 1
                else:
                    answer[i][j] = answer[i-1][j-1] + answer[i-1][j]
                    
        return answer[rowIndex]