class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxCount = 0
        for i in nums:
            if (i-1) in nums:
                continue
            nextNum = i+1
            count = 1
            while nextNum in nums:
                count += 1
                nextNum = nextNum+1
            maxCount = max(maxCount, count)
        return maxCount
                
            
                
                
            
            
        