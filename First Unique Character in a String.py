"""
First Unique Character in a String
# 387

Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dd = {}
        seen = set()
        for i in range(len(s)):
            if s[i] not in dd:
                dd[s[i]] = i
            
            if s[i] in seen:
                dd[s[i]] = 0
                del dd[s[i]]
            else:
                seen.add(s[i])
            
        if len(dd) == 0:
            return -1
        else:
            return min(dd.values())