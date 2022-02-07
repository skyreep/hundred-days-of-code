class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for ch in t:
            if s.count(ch) != t.count(ch):
                return ch