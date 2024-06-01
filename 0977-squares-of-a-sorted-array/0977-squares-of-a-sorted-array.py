class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        random = []
        for i in nums:
            random.append(i*i)
        return sorted(random)
            
        
        