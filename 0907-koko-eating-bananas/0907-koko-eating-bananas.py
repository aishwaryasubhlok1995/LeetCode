class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        heighest = max(piles)
        if h == len(piles):
            return heighest
        lowest = 1
        while lowest <= heighest:
            middle = (lowest + heighest)//2
            sumNo = 0 
            for i in range(len(piles)):
                sumNo  += math.ceil(piles[i]/middle)
                if  sumNo > h:
                    break 
            if sumNo <= h:
                heighest = middle - 1
            elif sumNo > h:
                lowest = middle + 1 
        return lowest

            
