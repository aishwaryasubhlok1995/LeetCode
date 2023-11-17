class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0 
        while j<=len(s)-1 and i<=len(t)-1:
            if s[j] == t[i]:
                j += 1
            i += 1
            
        if j == len(s):
            return True
        else:
            return False
        
            