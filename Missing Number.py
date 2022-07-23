"""
Missing Number
# 268

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = max(nums)
        
        n = [x for x in range(maxNum+1)]
        
        for i in nums:
            n.remove(i)
        if len(n) == 0 :
            return maxNum+1
        return n[0]