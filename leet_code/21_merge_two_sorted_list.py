# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
            
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        
        return l1
        # if not l1: return l2
        # if not l2: return l1

        # curr = ListNode(0)  # dummy node to avoid checking for null case
        # head = None
        # curr1, curr2 = l1, l2

        # while curr1 and curr2:
        #     if curr1.val < curr2.val:
        #         curr.next = ListNode(curr1.val)
        #         curr1 = curr1.next

        #     else:
        #         curr.next = ListNode(curr2.val)
        #         curr2 = curr2.next

        #     if not head:
        #         head = curr.next
        #     curr = curr.next

        # if not curr1: curr.next = curr2
        # if not curr2: curr.next = curr1

        # return head


