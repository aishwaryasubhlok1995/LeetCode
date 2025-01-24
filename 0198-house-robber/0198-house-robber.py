class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = [0]*(len(nums)+1)
        for i in range(1, len(nums)+1):
            if i == 1:
                arr[i] = nums[i-1]
            else:
                arr[i] = max((nums[i-1] +arr[i-2]), arr[i-1])
        return arr[-1]