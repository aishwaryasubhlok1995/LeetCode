class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #watch neetcode for explanation like we are taking base case 0 
        hm = {}
        hm[0] = 1
        currSum = 0
        count = 0
        for i in nums:
            currSum += i 
            if (currSum - k) in hm.keys():
                count += hm[currSum - k]
            if currSum in hm:
                hm[currSum] += 1
            else:
                hm[currSum] = 1
            
        return count 
                
            
        