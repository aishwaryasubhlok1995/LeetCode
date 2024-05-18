class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxCount = 0
        dict  = {}
        for i in nums:
            no = i-1
            count = 1
            while no in nums:
                if no in dict:
                    count += dict[no]
                    break
                else:
                    no = no -1
                    count += 1
            dict[i] = count 
            maxCount = max(count, maxCount)
        return maxCount
                
                
            
            
        