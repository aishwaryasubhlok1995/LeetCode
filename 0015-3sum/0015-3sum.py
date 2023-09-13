class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        finalAns = []
        arr = set()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j<k:
                ans = nums[i]+nums[j]+nums[k]
                if ans>0:
                    k -= 1
                if ans<0:
                    j += 1
                if ans == 0:
                    arr.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
        return arr
        
                    
                
            
            
        