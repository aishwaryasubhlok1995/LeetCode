class Solution:
# you are onl capturing when there is positive elevation, you don't need the day to sell, but if tday is #greater than yesterday it means u need to capture that, if there is deep then ignore, draw  graph , u  wull #understand 
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minNo = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans




        