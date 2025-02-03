class Solution:
    '''only question where we consider both remaining and curr'''
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        final = []
        curr = []
        def backtracking( remaining):
            if len(remaining) == 0:
                final.append(curr.copy())
                return 
            for i in range(len(remaining)):
                curr.append(remaining[i])
                element =  remaining[:i] +  remaining[i+1::] 
                backtracking( element)
                curr.pop()
        
        backtracking(nums)
        return final 
