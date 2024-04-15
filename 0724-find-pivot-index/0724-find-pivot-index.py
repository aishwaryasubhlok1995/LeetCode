class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        sumOfNums = 0
        for i in range(len(nums)):
            sumOfNums += nums[i]
            if sumOfNums == total:
                return i
            else:
                total = total - nums[i]
        return -1 
            
        