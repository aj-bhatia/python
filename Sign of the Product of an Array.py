"""
Sign of the Product of an Array
# 1822

There is a function signFunc(x) that returns:
    1 if x is positive.
    -1 if x is negative.
    0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.
Return signFunc(product).
"""

class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 1
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                x *= -1

        return -1 if x < 0 else 1