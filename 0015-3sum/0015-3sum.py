class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        finalAns = []
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
                    arr = [nums[i],nums[j],nums[k]]
                    if arr not in finalAns:
                        finalAns.append(arr)
                    j += 1
        return finalAns
        
                    
                
            
            
        