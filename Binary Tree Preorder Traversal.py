"""
Binary Tree Preorder Traversal
# 144

Given the root of a binary tree, return the preorder traversal of its nodes' values.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        self.recruse(root, arr)
        return arr
        
    def recruse(self, root, arr):
        if root:
            arr.append(root.val)
            self.recruse(root.left, arr)
            self.recruse(root.right, arr)