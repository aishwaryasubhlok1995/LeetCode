class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0 
        sSet = set()
        i = 0
        j = 0
        while j<len(s):
            if s[j] not in sSet:
                sSet.add(s[j])
                j += 1
                ans = max(ans, len(sSet))
            else:
                sSet.remove(s[i])
                i += 1
        return ans
        