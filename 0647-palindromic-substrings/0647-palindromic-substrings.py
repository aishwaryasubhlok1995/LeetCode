class Solution:
    def countSubstrings(self, s: str) -> int:
        res = ""
        maxLen = 0 
        count = 0
        for i in range(len(s)):
            left, right = i, i 
            ans = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:                
                if (right - left + 1) > maxLen:
                    res = s[left:right+1]
                    maxLen = len(res)
                count += 1
                left -= 1
                right += 1
            
            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > maxLen:
                    res = s[left:right+1]
                    maxLen = len(res)
                count += 1
                right += 1
                left -= 1
        return count