class Solution:
    def trap(self, height: List[int]) -> int:
        sumOfNo = 0
        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                sumOfNo += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                sumOfNo += maxRight - height[right]
        return sumOfNo
        