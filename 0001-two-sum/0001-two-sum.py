class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict.keys():
                return [i,dict[nums[i]]]  
            else:
                dict[target - nums[i]] = i
                
    
        