class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subArray = []
        final = []
        def calculateSum(i, total):
            if total == target:
                final.append(subArray.copy())
                return
        
            if total > target or i >= len(candidates):
                return 
            
            subArray.append(candidates[i])
            calculateSum(i, total + candidates[i])
            
            subArray.pop()
            calculateSum(i+1 ,total)
        
        calculateSum(0, 0) 
        return final
        
        
        
        
            