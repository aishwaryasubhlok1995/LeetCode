class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        arr = [math.inf]*(1+n)
        for i in range(1, n+1):
            if i == 1 or i == 2:
                arr[i] = cost[i-1] 
            else:
                arr[i] =  cost[i-1] + min(arr[i-1], arr[i-2])
        return min(arr[n], arr[n-1])
            
        