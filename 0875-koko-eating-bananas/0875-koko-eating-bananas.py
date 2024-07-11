class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        if h == len(piles):
            return k
        i = 1
        j = k
        minRate = math.inf
        while i<=j:
            bananaRate = 0
            mid = (i+j)//2
            for pile in range(len(piles)):
                if piles[pile] > mid:
                    bananaRate += (piles[pile])//mid 
                    if (piles[pile])%mid > 0:
                        bananaRate += 1
                elif piles[pile] <= mid:
                    bananaRate += 1
            if bananaRate > h:
                i = mid +1
            else:
                j = mid -1
                minRate = min(minRate, mid)
        return minRate
            
            
            