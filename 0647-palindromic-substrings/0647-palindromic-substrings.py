class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 1 
        for i in range(1, len(s)):
            res += 1
            prev = i-1
            nextt = i + 1
            while prev >= 0 and nextt<len(s) and s[prev] == s[nextt]:
                res += 1
                prev -= 1
                nextt += 1
            prev = i-1
            nextt = i
            while prev >= 0 and nextt<len(s) and s[prev] == s[nextt]:
                res += 1
                prev -= 1
                nextt += 1
        return res
            
        