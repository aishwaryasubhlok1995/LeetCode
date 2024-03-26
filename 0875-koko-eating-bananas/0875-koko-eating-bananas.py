class Solution:
    import math
    
    def calculatehours(self, mid, piles):
        total = 0
        if mid>0:
            for i in piles:
                total += math.ceil(i/mid)
        return total
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''the whole idea is to find k based on h and len of piles, have to develop a logic to return k, refer page 74 of the diary'''
        lenPiles = len(piles)
        maxElement = max(piles)
        if lenPiles == h:
            return maxElement
        if lenPiles < h:
            '''binary search'''
            first = 1
            last = maxElement
            while first<last:
                mid = (first + last)//2
                print(first)
                print(last)
                total = self.calculatehours(mid, piles)
                while self.calculatehours(mid-1, piles) == h:
                    total = self.calculatehours(mid-1, piles)
                    mid = mid -1 
                if total == h:
                    return mid
                if total < h:
                    last = mid - 1
                if total > h:
                    first = mid + 1
            while total > h:
                total = self.calculatehours(mid+1, piles)
                mid = mid + 1
            while total < h and self.calculatehours(mid-1, piles) < h and mid>1:
                total = self.calculatehours(mid+1, piles)
                mid = mid - 1
            return mid
                
                
            
        