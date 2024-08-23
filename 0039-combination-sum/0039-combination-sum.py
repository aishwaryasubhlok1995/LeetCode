class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subArray = []
        final = []
        def calculateSum(i):
            if sum(subArray) == target:
                final.append(subArray.copy())
                return
        
            if sum(subArray) > target or i >= len(candidates):
                return 
            
            subArray.append(candidates[i])
            calculateSum(i)
            
            subArray.pop()
            calculateSum(i+1)
        
        calculateSum(0) 
        return final
        
        
        
        
            