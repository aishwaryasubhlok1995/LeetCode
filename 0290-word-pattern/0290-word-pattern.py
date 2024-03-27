class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        listOfStrings = s.split(' ')
        listOfStrings1 = set(listOfStrings)
        pattern1 = set(pattern)
        dict = {}
        finalString = ''
        if len(pattern1) != len(listOfStrings1) or len(list(pattern)) != len(listOfStrings) :
            return False
        for i in range(len(listOfStrings)):
            if listOfStrings[i] not in dict:
                dict[listOfStrings[i]]  = pattern[i]
            finalString += dict.get(listOfStrings[i]) 
        if finalString != pattern:
            return False
        else:
            return True
            
        
        
        