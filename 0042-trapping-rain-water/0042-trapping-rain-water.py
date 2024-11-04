class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = height[0]
        maxRight = height[-1]
        L = 0
        R = len(height) - 1
        sumOfNo = 0
        while L<R:
            if maxLeft < maxRight:
                L += 1
                value = min(maxLeft, maxRight) - height[L]
                maxLeft = max(maxLeft, height[L])
            else:
                R -= 1
                value = min(maxLeft, maxRight) - height[R]
                maxRight = max(maxRight, height[R])
            if value > 0:
                sumOfNo += value
        
        return sumOfNo
        