class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        jewelsSet = set(jewels)
        for i in stones:
            if i in jewelsSet:
                ans += 1
        return ans
        
        