class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minNo = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            minNo = min(minNo, prices[i])
            if prices[i] > minNo:
                maxProfit = max(maxProfit, prices[i]-minNo)
            
        return maxProfit
            
        