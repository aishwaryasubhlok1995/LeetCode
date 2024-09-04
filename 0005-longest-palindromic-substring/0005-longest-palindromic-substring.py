class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for curr in range(1, len(s)):
            prev = curr-1
            nextt = curr+1
            while prev >= 0 and nextt < len(s):
                if s[prev] == s[nextt]:
                    if len(res) < nextt-prev+1:
                        res = s[prev:nextt+1]
                    prev = prev-1
                    nextt = nextt +1
                else:
                    break
            prev = curr-1
            nextt = curr
            while prev >= 0 and nextt < len(s):
                if s[prev] == s[nextt]:
                    if len(res) < nextt-prev+1:
                        res = s[prev:nextt+1]
                    prev = prev-1
                    nextt = nextt +1
                else:
                    break
               
        return res




        