"""
Top K Frequent Elements
# 347

Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dd = {}
        
        for i in nums:
            if i not in dd:
                dd[i] = 0
            dd[i] += 1
        
        arr = []

        for i in range(k):
            x = max(dd, key = dd.get)
            arr.append(x)
            del dd[x]
        return arr