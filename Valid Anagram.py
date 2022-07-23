"""
Valid Anagram
# 242

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dd1 = {}
        dd2 = {}
        for i in range(len(s)):
            if s[i] not in dd1:
                dd1[s[i]] = 0
            dd1[s[i]] += 1
            if t[i] not in dd2:
                dd2[t[i]] = 0
            dd2[t[i]] += 1
        return True if dd1 == dd2 else False