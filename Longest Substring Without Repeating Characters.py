"""
Longest Substring Without Repeating Characters
# 3

Given a string s, find the length of the longest substring without repeating characters.

"""

class Solution(object):
    def lengthOfLongestSubstring(self, str):
        """
        :type s: str
        :rtype: int
        """
        strMax = 0
        windowStart = 0
        dd = {}
  
        for windowEnd in range(len(str)):
            if str[windowEnd] not in dd:
                dd[str[windowEnd]] = 0
            dd[str[windowEnd]] += 1
    
            while dd[str[windowEnd]] > 1:
                dd[str[windowStart]] -= 1
                if dd[str[windowStart]] == 0:
                        del dd[str[windowStart]]
                windowStart += 1
            strMax = max(strMax, len(dd.keys()))
        return strMax