# https://leetcode.com/problems/univalued-binary-tree/

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        # solution1 : Using BFS
#         queue = deque([root])
        
#         while queue:
#             cur_root = queue.popleft()
            
#             if cur_root.left and cur_root.val == cur_root.left.val:
#                 queue.append(cur_root.left)
#             elif cur_root.left and cur_root.val != cur_root.left.val:
#                 return False
                
#             if cur_root.right and cur_root.val == cur_root.right.val:
#                 queue.append(cur_root.right)
#             elif cur_root.right and cur_root.val != cur_root.right.val:
#                 return False
        
#         return True

        # solution2 : Using DFS
    
        stack = deque([root])
        
        while stack:
            cur_root = stack.pop()
            
            if cur_root:
                if cur_root.left and (cur_root.val != cur_root.left.val):
                    return False
                
                if cur_root.right and (cur_root.val != cur_root.right.val):
                    return False
            
                stack.append(cur_root.left)
                stack.append(cur_root.right)
        return True
                
                    
            