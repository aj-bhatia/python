"""
Intersection of Two Arrays II
# 350

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and 
you may return the result in any order.
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        dd = {}
        for i in nums1:
            if i not in dd:
                dd[i] = 0
            dd[i] += 1
            
        for i in nums2:
            if i in dd:
                ans.append(i)
                dd[i] -= 1
                if dd[i] == 0:
                    del dd[i]
        return ans