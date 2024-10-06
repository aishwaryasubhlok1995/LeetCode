class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        counter = 0
        nums = set(nums)
        for i in range(len(nums)):
            if counter in nums: 
                counter += 1
            else:
                return counter
        return counter
            
            
        
        
        