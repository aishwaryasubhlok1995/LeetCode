class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0] 
        largeNum = nums[0] 
        smallNum = nums[0]
        for i in range(1, len(nums)):
            temp_val = max(nums[i], largeNum*nums[i], smallNum*nums[i])
            smallNum = min(nums[i], largeNum*nums[i], smallNum*nums[i])
            largeNum = temp_val
            res  = max(res, largeNum)

        return res 
