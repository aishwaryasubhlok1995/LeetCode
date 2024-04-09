class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minElement = math.inf
        maxDifference = -math.inf
        for i in range(len(prices)):
            minElement = min(prices[i], minElement)
            maxDifference = max(maxDifference, (prices[i]-minElement))
        return maxDifference
            
                
                
        
            
            
        