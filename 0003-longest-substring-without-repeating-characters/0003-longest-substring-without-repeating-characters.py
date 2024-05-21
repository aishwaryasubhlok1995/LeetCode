class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slist = set()
        maxCount = 0
        i = 0
        j = 0
        while j < len(s):
            if s[j] not in slist:
                slist.add(s[j])
                maxCount = max(maxCount, len(slist))
                j = j+1
            else:
                if s[i] != s[j] or s[i] == s[j]:
                    slist.remove(s[i])
                i = i+1
        return maxCount
                
                
            
            
                