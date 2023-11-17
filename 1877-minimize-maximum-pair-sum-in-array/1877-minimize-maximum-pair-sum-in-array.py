class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums  = sorted(nums)
        i = 0 
        j = len(nums)-1
        res = []
        while i<j:
            res.append(nums[i]+nums[j])
            i += 1
            j -= 1
        return max(res)
        