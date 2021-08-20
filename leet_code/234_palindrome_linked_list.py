# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         q:Deque = collections.deque()
#         # q:List = []
#         if not head:
#             return True
        
#         node = head
        
#         while node != None:
#             q.append(node.val)
#             node = node.next
            
#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False
#         return True
#         # return q == q[::-1]

        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        if fast:
            slow = slow.next
            
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        
        return not rev