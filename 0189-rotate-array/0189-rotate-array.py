class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0 
        start = 0
        while count != len(nums):
            i = start
            newValue = nums[i]
            while 1: 
                idx = (i+k)%len(nums)
                oldValue = nums[idx]
                nums[idx] = newValue
                newValue = oldValue
                i = idx
                count += 1
                if start == i:
                    break
            start = start+1
        return nums