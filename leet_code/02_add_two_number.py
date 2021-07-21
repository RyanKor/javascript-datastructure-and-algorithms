# Definition for singly-linked list.
# https://leetcode.com/problems/add-two-numbers/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = curr = ListNode(
            0
        )  #we need two varibles because if only one variable is used we might loose reference to the head
        carry = 0
        while l1 or l2 or carry:  # not none
            if l1:
                carry += l1.val
                l1 = l1.next  #increase value of l1
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)  #retur remainder of division
            curr = curr.next
            carry = carry // 10  #returns floor value of division

        return result.next