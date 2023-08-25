class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, r = 0, len(s)-1
        while(i<r):
            if(s[i]==s[r]):
                i = i+1
                r = r-1
            else:
                slicedString =  s[i:r] 
                slicedString1 =  s[i+1:r+1]
                return(slicedString == slicedString[::-1] or slicedString1 == slicedString1[::-1])
        if(i>=r):
            return True
                
                            
