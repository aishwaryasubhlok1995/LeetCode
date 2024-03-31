class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dictCount = {}
        start = {}
        end = {}
        for i in range(len(nums)):
            if nums[i] not in dictCount:
                dictCount[nums[i]] = 1
                start[nums[i]]  = i
                end[nums[i]]  = i
            else:
                dictCount[nums[i]] += 1
                end[nums[i]]  = i
        maxFrequency = max(dictCount.values())
        minLength = math.inf
        print(maxFrequency)
        for i in dictCount.keys():
            if dictCount.get(i) == maxFrequency:
                length = end[i] - start[i] + 1
                print(length)
                minLength = min(length, minLength)
        return minLength
        
        