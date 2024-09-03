class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxString = s[0]
        for i in range(len(s)):
            newString = s[i]
            for j in range(i+1, len(s)):
                newString += s[j]
                if newString == newString[::-1] and len(newString) >= len(maxString):
                    maxString = newString
        return maxString
                    
                
        