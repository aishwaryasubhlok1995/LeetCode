class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums);
        length = len(nums)
        for i in range(length):
            if i != nums[i]:
                return i 
        return length