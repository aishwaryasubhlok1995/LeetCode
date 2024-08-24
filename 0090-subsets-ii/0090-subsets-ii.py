class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subArray = []
        final = []
        nums = sorted(nums)
        def findSubset(i):
            if i == len(nums):
                final.append(subArray.copy())
                return final 
            
            subArray.append(nums[i])
            findSubset(i+1)
            
            subArray.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            findSubset(i+1)
        
        findSubset(0)
        return final
            
            
        