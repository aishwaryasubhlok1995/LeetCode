class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        array = [math.inf]*(1+amount)
        array[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >= 0:
                    if i-coin == 0:
                        array[i] = 1
                    else:
                        array[i] = min(array[i], array[i-coin]+1)
        return -1 if array[-1] == math.inf else array[-1]
                    
        