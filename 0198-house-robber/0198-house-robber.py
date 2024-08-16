class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        arr = [0]*(len(nums))
        for i in range(2, len(arr)):
            if i == 2:
                arr[i] = nums[i-2]
            else:
                arr[i] = max((nums[i-2] + arr[i-2]), (nums[i-3] + arr[i-3]))
        return max(arr[-2]+nums[-2], arr[-1] +nums[-1])
            
            
            
            
        