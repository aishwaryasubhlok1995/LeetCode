class Solution:
    def calculateFromPiles(self, piles, k):
        count = 0 
        for i in range(len(piles)):
            count += ceil(piles[i]/k)
        return count
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimumKElement = math.inf
        piles = sorted(piles)
        if len(piles) == h:
            return max(piles)
#         Apply binary search 
        i = 1
        j = max(piles)
        while i<=j:
            mid = (i+j)//2
            if self.calculateFromPiles(piles, mid) <= h:
                minimumKElement = min(mid, minimumKElement)
                j =  mid-1
            else:
                i = mid+1
        return minimumKElement
            
            
            
        
        