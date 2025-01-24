class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        we can solve dp with recursionw which causes 2^n and recursion with memization(hm) which give O(n) but space is also O(n) so we go with bottom up .. but with first, second, third 
        '''
        memo = {}
        def helper(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return 1
            if n == 2:
                return 2 
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]

        return helper(n)

        

        