class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict.keys():
                return [i, dict[nums[i]]] 
            else:
                dict[target - nums[i]] = i