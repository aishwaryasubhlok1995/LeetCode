class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lenOfList = len(nums)
        if len(set(nums)) == lenOfList:
            return False
        return True
        