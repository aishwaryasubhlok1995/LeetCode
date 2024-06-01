class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        k = len(nums)-1
        i = 0
        j = len(nums) - 1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                ans[k] = nums[i]*nums[i]
                i = i+1
            else:
                ans[k] = nums[j]*nums[j]
                j = j-1
            k = k -1
        return ans
                
            
        
        