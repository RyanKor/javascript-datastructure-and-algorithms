# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

          # solution 1 : swap the pair-nodes
#         cur = head
        
#         while cur and cur.next:
#             cur.val, cur.next.val = cur.next.val, cur.val
#             cur = cur.next.next
            
#         return head
        
        # solution 2 : use recursion
        if head and head.next:
            pointer = head.next
            
            head.next = self.swapPairs(pointer.next)
            
            pointer.next = head
            
            return pointer
        
        return head