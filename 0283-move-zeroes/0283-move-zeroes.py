class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
      
        while i<len(nums) and j < len(nums):
            if nums[i] != 0:
                i = i+1
            elif j<=i or nums[j] == 0:
                j = j + 1
            else:
                if nums[i] == 0 and nums[j] != 0:
                    nums[i] = nums[j]
                    nums[j] = 0
                
            
            
            
            
        
            
        
                