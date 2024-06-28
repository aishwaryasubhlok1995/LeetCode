class Solution:
    '''sliding window but lot of tweak'''
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0 
        j = 0
        dictFruits = {}
        dictFruits[fruits[i]] = 1
        maxCount = 0
        while j < len(fruits)-1:
            j = j+1
            if fruits[j] not in dictFruits:
                dictFruits[fruits[j]] = 1
            else:
                dictFruits[fruits[j]] += 1
            if len(dictFruits) > 2:
                while len(dictFruits) > 2:
                    if dictFruits[fruits[i]] >= 1:
                        dictFruits[fruits[i]] -= 1
                    if dictFruits[fruits[i]] == 0:
                        del dictFruits[fruits[i]]
                    i = i+1
            maxCount = max(maxCount, len(fruits[i:j+1:]))
        if maxCount == 0:
            return 1
        return maxCount
            
            
                
                
            
            
    
        
                
                
                
            
        
            
                    
        
        