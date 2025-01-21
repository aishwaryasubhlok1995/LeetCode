class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead. // Use this approach single pass
        """
        low = 0 
        high = len(nums) - 1
        middle = 0
        while middle <= high:
            if nums[middle] == 1:
                middle += 1
            elif nums[middle] == 0:
                nums[low], nums[middle] = nums[middle], nums[low] 
                low += 1
                middle += 1
            elif nums[middle] == 2:
                nums[high], nums[middle] = nums[middle], nums[high] 
                high -= 1
            





        