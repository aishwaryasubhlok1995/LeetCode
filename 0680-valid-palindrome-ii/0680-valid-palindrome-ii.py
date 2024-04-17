class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s)-1
        reverseStr = ''
        if s[::-1] == s:
            return True
        while i!=j:
            if s[i] == s[j]:
                i += 1
                j -=1
            else:
                temp = s[:i:] + s[i+1::] 
                temp1 = s[:j:] + s[j+1::]
                return temp == temp[::-1] or temp1 == temp1[::-1] 
        
        
                    
            
                
        