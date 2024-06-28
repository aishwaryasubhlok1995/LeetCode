class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dictMap = {0:0, 1:0, 2:0}
        for i in nums:
            dictMap[i] += 1
        for i in range(len(nums)):
            if i < dictMap[0]:
                nums[i] = 0
            elif i < dictMap[1] + dictMap[0]:
                nums[i] = 1
            elif i < dictMap[2] + dictMap[1] + dictMap[0]:
                nums[i] = 2
        
                
            
            
                
                
                
            
                    
                