class Solution:
    #this question is bit tricky but imagine, you have a branch and removal of some portion from it will give you K so we are checking how many occurrences of removal/wastage are there 
    def subarraySum(self, nums: List[int], k: int) -> int:
        #base case hm = {0:1}
        hm = {0:1}
        runningSum = 0
        count = 0
        for num in nums:
            runningSum += num
            if (runningSum - k) in hm:
                count += hm[runningSum - k]
            if runningSum not in hm:
                hm[runningSum] = 1
            else:
                hm[runningSum] += 1
        return count
            
        