class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = set()
        print(nums)
        for k in range(len(nums)-2):
            i = k+1
            j = len(nums)-1
            while(i<j):
                if nums[k]+nums[i]+nums[j] > 0:
                    j = j-1
                elif nums[k]+nums[i]+nums[j] < 0:
                    i = i+1
                elif nums[k]+nums[i]+nums[j] == 0:
                    res.add((nums[k],nums[i],nums[j]))
                    i = i+1
                    j = j-1
        return res