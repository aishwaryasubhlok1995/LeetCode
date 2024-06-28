class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dictMap = {}
        for i in range(len(nums)):
            if nums[i] not in dictMap:
                dictMap[nums[i]] = 1
            else:
                dictMap[nums[i]] += 1
        i = 0
        while i < len(nums):
            if 0 in dictMap:
                dictMap[0] -= 1 
                nums[i] = 0
                if dictMap[0] == 0:
                    del dictMap[0]
            elif 1 in dictMap:
                dictMap[1] -= 1 
                nums[i] = 1
                if dictMap[1] == 0:
                    del dictMap[1]
            elif 2 in dictMap:
                dictMap[2] -= 1 
                nums[i] = 2
                if dictMap[2] == 0:
                    del dictMap[2]
            i = i+1
            print(nums)
            
                
                
                
            
                    
                