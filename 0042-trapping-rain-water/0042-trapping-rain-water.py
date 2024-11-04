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
                maxLeft = max(maxLeft, height[L])
                value =  maxLeft- height[L]
                
            else:
                R -= 1
                maxRight = max(maxRight, height[R])
                value = maxRight - height[R]
                
            sumOfNo += value
        
        return sumOfNo
        