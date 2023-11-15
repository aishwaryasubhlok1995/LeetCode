class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict.keys():   
                if target - nums[i] in nums:
                    dict[target - nums[i]] = i
            else:
                return [i,dict[nums[i]]]
        return 0
    
        