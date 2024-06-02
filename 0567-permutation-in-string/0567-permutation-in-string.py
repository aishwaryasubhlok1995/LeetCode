# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         dictS1 = {}
#         for i in s1:
#             if i not in dictS1:
#                 dictS1[i]  = 1
#             else:
#                 dictS1[i] += 1
#         tempDict = dictS1.copy()
#         for i in range(len(s2)):
#             if s2[i] in tempDict:
#                 for k in range(len(s1)):
#                     tempDict[s2[i]] -= 1
#                     if tempDict[s2[i]] == 0:
#                         del tempDict[s2[i]]
#                     if tempDict == {}:
#                         return True 
#                     if i+1 <len(s2) and s2[i+1] in tempDict:
#                         i = i+1
#                     else:
#                         tempDict = dictS1.copy()
#                         break
#         return False 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dictS1 = {}
        for i in s1:
            if i not in dictS1:
                dictS1[i]  = 1
            else:
                dictS1[i] += 1
        tempDict = dictS1.copy()
        for i in range(len(s2)-len(s1)+1):
            for k in range(len(s1)):
                if s2[i+k] in tempDict:
                    tempDict[s2[i+k]] -= 1
                    if tempDict[s2[i+k]] == 0:
                        del tempDict[s2[i+k]]
                    if tempDict == {}:
                        return True 
                else:
                    tempDict = dictS1.copy()
                    break
        return False 
            
        
        