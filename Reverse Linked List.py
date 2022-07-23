"""
Reverse Linked List
# 206

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = dummy = ListNode(-1)
        dummy.next = head
        
        cur2 = dummy2 = ListNode(-1)
        
        while cur.next:
            temp = ListNode(cur.next.val)
            temp.next = cur2.next
            cur2.next = temp
            cur = cur.next
        return dummy2.next