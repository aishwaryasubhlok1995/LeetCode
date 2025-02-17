class Solution:
    def validPalindrome(self, s: str) -> bool:     
        i = 0 
        j = len(s) - 1
        
        def checkPalindrome(i, j):
            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False 
            return True 
        
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if checkPalindrome(i, j-1) == True:
                    return True 
                elif checkPalindrome(i+1, j) == True:
                    return True
                else:
                    return False

        return True 

            

        