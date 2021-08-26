# https://leetcode.com/problems/invert-binary-tree/

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # solution 1 : pythonic solution
#         if root:
#             root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            
#             return root
        
#         return None
    
    
        # solution 2: BFS with Deque
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node:
                node.left, node.right = node.right, node.left
                
                queue.append(node.left)
                queue.append(node.right)
                
        return root


        # solution 3: DFS
    
#         stack = deque([root])
        
#         while stack:
#             node = stack.pop()
#             if node:
#                 node.left, node.right = node.right, node.left
                
#                 stack.append(node.left)
#                 stack.append(node.right)
#         return root


        # solution 4: DFS Postorder Traversal
    
#         stack = deque([root])
        
#         while stack:
#             node = stack.pop()
#             if node:
#                 stack.append(node.left)
#                 stack.append(node.right)
#                 node.left, node.right = node.right, node.left
            
#         return root