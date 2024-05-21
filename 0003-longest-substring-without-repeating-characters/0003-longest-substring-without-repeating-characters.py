class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slist = set()
        removeList = []
        count = 0
        maxSubString = 0
        i = 0
        while i < len(s):
            if s[i] not in slist:
                slist.add(s[i])
                removeList.append(s[i])
            else:
                count = len(slist)
                maxSubString = max(maxSubString, count)
                j = 0
                while removeList[0] != s[i]:
                    slist.remove(removeList[0])
                    removeList.pop(0) 
                removeList.pop(0) 
                removeList.append(s[i]) 
                count = 0
            i = i+1
        count = len(slist)
        maxSubString = max(maxSubString, count)
        return maxSubString
                
            
            
                