class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            if i == 0:
                right = right - nums[0]
                left = 0 
            else:
                left += nums[i-1]
                right = right - nums[i]
            if left == right:
                return i
        print(left, right)
        return -1
                
                
                    
                
        