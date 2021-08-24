# https://leetcode.com/problems/triangle/
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # Wrong Answer
#         min_path = [triangle[0][0]]
        
#         for i in range(1, len(triangle)):
#             if triangle[i-1].index(min_path[-1]) == 0:
#                 min_path.append(min(triangle[i][0],triangle[i][1]))
#             else:
#                 min_path.append(min(triangle[i][triangle[i-1].index(min_path[-1])], triangle[i][triangle[i-1].index(min_path[-1]) + 1]))
#             # print(min_path)
#         return sum(min_path)

        # right answer
        row = triangle[-1]
        print(row)
        for i in reversed( range(len(triangle)-1) ):
            print(i)
            row = [ num + min(row[idx],row[idx+1]) for idx,num in enumerate(triangle[i])]
            print(row)
        return row[0]