class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        initial = x
        reverse = 0
        if x < 0:
            return False
        while(x > 0):
            
            remainder = x%10
            x = x/10
            reverse = reverse*10 + remainder
        if reverse == initial:
            return True
        return False
                
        
        