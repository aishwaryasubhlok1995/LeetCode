class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        maxlen = 0 
        setOfItems = set()
        while j < len(s):
            if s[j] not in setOfItems:
                setOfItems.add(s[j])
                maxlen = max(maxlen, len(setOfItems))
                j = j + 1
            else: 
                if s[i] != s[j] :
                    setOfItems.remove(s[i])
                if s[i] == s[j]:
                    setOfItems.remove(s[i])
                i = i+1
        return maxlen
                    
                    
            
                