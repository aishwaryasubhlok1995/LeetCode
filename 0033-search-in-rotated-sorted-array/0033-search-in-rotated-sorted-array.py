class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) -1 
        if len(nums) == 1 and nums[0] == target:
            return 0
        while left < right:
            middle = (left + right)//2 
            if nums[middle] == target:
                return middle
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle 

        if target >= nums[left] and target <= nums[len(nums) -1]:
            right = len(nums) -1
        elif target >= nums[len(nums) -1]:
            right = left - 1
            left = 0
        while left <= right:
            mid = (left + right) //2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else: 
                left = mid + 1
        return -1