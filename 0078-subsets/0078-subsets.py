class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
         
        def findSubsets(i, subArray):
            if i >= len(nums):
                final.append(subArray.copy())
                return final 
            
            subArray.append(nums[i])
            findSubsets(i+1, subArray)
            
            subArray.pop()
            findSubsets(i+1, subArray)
        
        findSubsets(0, [])
        return final
            
            
            
            
            
        