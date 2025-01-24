class Solution:
    def rob(self, nums: List[int]) -> int:
        first = 0
        second = nums[0]
        for i in range(1, len(nums)):
            third = max((nums[i] + first), second)
            first= second
            second = third 
        return second