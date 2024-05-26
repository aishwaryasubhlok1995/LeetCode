class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        dictChar = {s[0]:1}
        maxLen = 1
        while j <len(s)-1 :
            if (j-i+1-max(dictChar.values())) <= k:
                j = j+1
                if s[j] not in dictChar:
                    dictChar[s[j]] = 1
                else:
                    dictChar[s[j]] += 1 
            else:
                if dictChar[s[i]] > 0:
                    dictChar[s[i]] = dictChar[s[i]] - 1
                else:
                    del dictChar[s[i]]
                i += 1
            if (j-i+1-max(dictChar.values())) <= k:
                maxLen = max(j-i+1, maxLen)
        return maxLen
                
                
            
                
            