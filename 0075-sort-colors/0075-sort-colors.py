class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        
        while j<len(nums):
            if nums[i] == 0:
                i = i+1
            else:
                if nums[j] == 0 and nums[i] != 0:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    i = i + 1
            j = j+1
        if nums[i] == 0:
            i = i+1
        j = i+1
        while j<len(nums) and i < len(nums):
            print(i, j, nums)

            if nums[i] == 1:
                 i = i+1
            else:
                if nums[j] == 1 and nums[i] != 1 and i<j:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    i = i+1
                j = j + 1
        print(nums)
                
                
            
                    
                