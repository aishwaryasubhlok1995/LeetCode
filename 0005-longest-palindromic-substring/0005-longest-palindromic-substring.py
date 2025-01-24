class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLen = 0 
        for i in range(len(s)):
            left, right = i, i 
            ans = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > maxLen:
                    res = s[left:right+1]
                    maxLen = len(res)
                left -= 1
                right += 1
            
            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > maxLen:
                    res = s[left:right+1]
                    maxLen = len(res)
                right += 1
                left -= 1
        return res
            

            


        