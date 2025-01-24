class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLen = 0 
        for i in range(len(s)):
            left, right = i, i 
            ans = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            ans = s[left+1:right]
            right = i
            left = i-1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                right += 1
                left -= 1
            if len(ans) < (right - left):
                ans = s[left+1:right] 
            if len(ans) > maxLen:
                maxLen = len(ans)
                res = ans
        return res
            

            


        