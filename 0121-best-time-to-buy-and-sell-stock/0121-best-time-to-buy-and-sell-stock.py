class Solution(object):
    def maxProfit(self, prices):
        """
        maxProfit = 0
        for i in range(len(prices)-1):
            price = max(prices[i+1::]) - prices[i]
            maxProfit = max(price, maxProfit)
        return maxProfit
        """
        maxProfit = 0
        minElement = prices[0]
        for i in range(len(prices)):
            minElement = min(prices[i], minElement)
            maxProfit = max(maxProfit, (prices[i]-minElement))
        return maxProfit


        


