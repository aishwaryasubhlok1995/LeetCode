class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0]*len(height)
        righMax = [0]*len(height)
        maxleftVal = 0
        maxRightVal = 0
        sumVal = 0
        for i in range(1, len(height)):
            maxleftVal = max(maxleftVal, height[i-1])
            leftMax[i] = maxleftVal
        for j in range(len(height)-2, -1, -1):
            maxRightVal = max(maxRightVal, height[j+1])
            righMax[j] = maxRightVal
        for h in range(1, len(height)):
            value = min(leftMax[h], righMax[h]) - height[h]
            if value > 0:
                sumVal += value 
        return sumVal
        