class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []
        def backtrack(rem, curr):
            if len(curr) == len(nums):
                final.append(curr.copy())
                return 
            for i in range(len(rem)):
                curr.append(rem[i])
                val = rem[:i] + rem[i+1::]
                backtrack(val, curr)
                curr.pop()
        backtrack(nums, [])
        return final 
        
        
        
        