class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minElement = prices[0]
        maxDifference = 0
        for i in range(len(prices)):
            minElement = min(prices[i], minElement)
            maxDifference = max(maxDifference, (prices[i]-minElement))
        return maxDifference
            
                
                
        
            
            
        