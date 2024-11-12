class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        DP = [math.inf]*(amount+1)
        DP[0] = 0
        for i in range(1, amount+1):
            arr = []
            for coin in coins:
                if i - coin >= 0:
                    arr.append(1 + DP[i-coin])
            if len(arr) > 0:
                DP[i] = min(arr)
        if DP[amount] == math.inf:
            return -1
        return DP[amount]
            
        