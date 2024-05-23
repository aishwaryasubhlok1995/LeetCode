class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0 
        j = len(nums) - 1
        while i<=j:
            mid = (i+j)//2
            if nums[mid] == min(nums):
                return nums[mid]
            elif nums[mid] > nums[j]:
                i = mid+1
            elif nums[mid] < nums[j]:
                j = mid                 
        return 0
        