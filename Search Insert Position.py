"""
Search Insert Position
# 35

Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if target < nums[mid]:
                hi = mid-1
            elif target > nums[mid]:
                lo = mid+1
            else:
                return mid
        return lo