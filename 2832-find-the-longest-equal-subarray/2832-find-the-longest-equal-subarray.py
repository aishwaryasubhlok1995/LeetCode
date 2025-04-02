class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        i = 0 
        j = 0
        maxLen = 1 
        mapOfElements = {nums[i] : 1}
        while j <len(nums):
            length = j-i+1
            if length - maxLen <= k:
                j += 1
                if j<len(nums):
                    if nums[j] not in mapOfElements:
                        mapOfElements[nums[j]] = 1
                    else:
                        mapOfElements[nums[j]] += 1
                    maxLen = max(maxLen, mapOfElements[nums[j]])
            else:
                if i < len(nums):
                    mapOfElements[nums[i]] -= 1
                if mapOfElements[nums[i]]  == 0:
                    del mapOfElements[nums[i]]
                i += 1
        return maxLen


        