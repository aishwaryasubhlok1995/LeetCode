class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0] 
        largeNum = nums[0] 
        smallNum = nums[0]
        for i in range(1, len(nums)):
            print(nums[i],largeNum,  smallNum)
            largeValue = max(nums[i], largeNum*nums[i], smallNum*nums[i])
            smallValue = min(nums[i], largeNum*nums[i], smallNum*nums[i])
            largeNum = largeValue
            smallNum = smallValue
            res  = max(res, largeNum)

        return res 
