class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height)-1
        maxArea = (j-i)*min(height[i], height[j]) 
        while i<j:
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
            length = min( height[i], height[j])
            breadth = j-i 
            maxArea = max(maxArea, (length*breadth))
        return maxArea
        