"""
Maximum Subarray
# 53

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        windowStart, maxSub, total = 0, float('-inf'), 0
        for windowEnd in range(len(nums)):
            total += nums[windowEnd]
            maxSub = max(maxSub, total)
            while total < 0:
                total -= nums[windowStart]
                windowStart += 1
        
        return maxSub
        