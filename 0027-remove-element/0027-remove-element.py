class Solution(object):
    def removeElement(self, nums, val):
        l = 0
        r = 0
        k = 0
        while r<len(nums):
            if nums[r]==val:
                r += 1 
            else:
                temp = nums[l]   
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r += 1
                k += 1
        return k  
                