# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
#         odd = [chr(i) for i in range(ord("a"), ord('h')+1,2)]
#         even = [chr(i) for i in range(ord("b"), ord('h')+1,2)]
#         if coordinates[0] in odd and int(coordinates[1]) % 2 != 0:
#             return False
        
#         if coordinates[0] in even and int(coordinates[1]) % 2 == 0:
#             return False
        
#         return True
        return (ord(coordinates[0]) + int(coordinates[1])) % 2 != 0