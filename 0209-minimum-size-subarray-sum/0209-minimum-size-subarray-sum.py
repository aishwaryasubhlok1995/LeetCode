import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        minLength = math.inf
        lenCounter = 1
        sumOfNums = nums[i]
        while(j<len(nums)):
            if sumOfNums<target:
                j += 1
                if j < len(nums):
                    sumOfNums += nums[j]
            else:
                length = j-i+1
                minLength = min(length, minLength)
                sumOfNums -= nums[i]
                i += 1
        if minLength == math.inf:
            return 0
        return minLength
                
            
             
            
        
        
        