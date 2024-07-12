class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        curr = []
        def subset(i):
            if i == len(nums):
                final.append(curr.copy())
                return  
            
            curr.append(nums[i])
            subset(i+1)
            
            curr.pop()
            subset(i+1)
        subset(0)
        return final