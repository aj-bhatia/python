"""
Search a 2D Matrix
# 74

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ll = []
        for i in matrix:
            for j in i:
                ll.append(j)
        lo = 0
        hi = len(ll)-1
        
        print(ll)
        
        while lo <= hi:
            mid = (hi+lo)//2
            if ll[mid] == target:
                return True
            elif ll[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
        return False