"""
Add Two Numbers
# 2

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = dummy = ListNode(-1)
        cur2 = dummy2 = ListNode(-1)
        dummy.next = l1
        dummy2.next = l2
        newN = head = ListNode(-1)
        c = 0
        while cur and cur2:
            x = cur.val + cur2.val + c
            if x > 9:
                x -= 10
                c = 1
            else:
                c = 0
            new = ListNode(x)
            newN.next = new
            newN = newN.next
            cur = cur.next
            cur2 = cur2.next
        while cur:
            x = cur.val + c
            if x > 9:
                x -= 10
                c = 1
            else:
                c = 0
            new = ListNode(x)
            newN.next = new
            newN = newN.next
            cur = cur.next
        while cur2:
            x = cur2.val + c
            if x > 9:
                x -= 10
                c = 1
            else:
                c = 0
            new = ListNode(x)
            newN.next = new
            newN = newN.next
            cur2 = cur2.next
        if c:
            new = ListNode(c)
            newN.next = new
            newN = newN.next
        return head.next.next
            