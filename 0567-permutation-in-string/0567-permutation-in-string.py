class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dictS1 = {}
        for char in s1:
            if char in dictS1:
                dictS1[char] += 1
            else:
                dictS1[char] = 1
        i = 0
        j = 0
        dictS2 = {s2[i]:1}
        if dictS2 == dictS1:
            return True
        while j<len(s2):
            if j-i+1 == len(s1):
                 if dictS2 == dictS1:
                    return True
                 else:
                    dictS2[s2[i]] -= 1
                    if dictS2[s2[i]] == 0:
                        del dictS2[s2[i]]
                    i += 1
            else:
                    j += 1
                    if j <len(s2):
                        if s2[j] not in dictS2:
                            dictS2[s2[j]] = 1
                        else:
                             dictS2[s2[j]] += 1

        
                
                
        
        
            
        