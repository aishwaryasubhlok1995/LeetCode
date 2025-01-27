class Solution:
    def countSubstrings(self, s: str) -> int:
        res = ""
        maxLen = 0 
        count = 0
        for i in range(len(s)):
            left, right = i, i 
            ans = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:                
                count += 1
                left -= 1
                right += 1
            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                right += 1
                left -= 1
        return count