"""
Merge Two Sorted Lists
# 21

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummy1 = ListNode(-1)
        dummy1.next = l1
        cur1 = dummy1
        
        dummy2 = ListNode(-1)
        dummy2.next = l2
        cur2 = dummy2
        
        dummy3 = ListNode(-1)
        cur3 = dummy3
        
        while cur1.next and cur2.next:
            if cur1.next.val < cur2.next.val:
                cur3.next = ListNode(cur1.next.val)
                cur1 = cur1.next
            else:
                cur3.next = ListNode(cur2.next.val)
                cur2 = cur2.next
            cur3 = cur3.next
                
        while cur1.next:
            cur3.next = ListNode(cur1.next.val)
            cur1 = cur1.next
            cur3 = cur3.next
        while cur2.next:
            cur3.next = ListNode(cur2.next.val)
            cur2 = cur2.next
            cur3 = cur3.next           
            
                
        return dummy3.next