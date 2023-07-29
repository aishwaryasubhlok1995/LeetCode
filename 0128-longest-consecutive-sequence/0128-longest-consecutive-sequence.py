class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        longNumber = 0
        if len(nums) == 0:
            return 0
        for i in nums:
            counter = 1
            number = i-1
            if number in nums:
                continue
            else:
                while i+1 in nums:
                    counter = counter + 1
                    i = i + 1
                longNumber = max(longNumber, counter)
        return longNumber
                    
        