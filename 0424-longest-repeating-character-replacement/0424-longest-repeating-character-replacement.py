class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        dictChar = {s[j]:1}
        maxLen = 1
        sumOccurence = 0
        while j<len(s)-1:
            if sumOccurence <= k:
                maxLen = max(maxLen, (j -i +1))
                j += 1
                if s[j] not in dictChar:
                    dictChar[s[j]] = 1
                else:
                    dictChar[s[j]] += 1
            else:
                print(dictChar[s[i]])
                if dictChar[s[i]] > 0:
                    dictChar[s[i]] =dictChar[s[i]] -1
                else:
                    del dictChar[s[i]]
                i += 1 
            maxaVal = max(dictChar.values())
            sumOccurence = j -i +1-maxaVal
        if sumOccurence <= k:
            maxLen = max(maxLen, (j -i +1))
        return maxLen
                
                
                
            
                
            