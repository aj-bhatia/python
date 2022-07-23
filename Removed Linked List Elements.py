"""
Remove Linked List Elements
# 203

Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
                
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        cur = dummy_head
        
        while cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next