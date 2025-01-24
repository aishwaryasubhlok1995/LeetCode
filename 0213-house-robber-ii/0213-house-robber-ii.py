class Solution:
    def rob(self, nums: List[int]) -> int: 
        if len(nums) == 1:
            return nums[0]
        def helper(initial, last):
            first = 0
            second = nums[initial]
            for i in range(initial+1, len(nums)-last):
                third = max(second, (nums[i]+ first))
                first = second
                second = third
            return second
        return max(helper(0, 1), helper(1, 0))
        