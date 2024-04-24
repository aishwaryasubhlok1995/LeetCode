class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sumOfElements = 0
        maxSum = 0
        for i in range(minutes):
            if grumpy[i] != 0:
                sumOfElements += customers[i]
        maxSum = max(sumOfElements, maxSum)
        for i in range(minutes, len(customers)):
            if grumpy[i] != 0:
                sumOfElements += customers[i]
            if grumpy[i-minutes] != 0:
                sumOfElements -= customers[(i-minutes)]
            maxSum = max(sumOfElements, maxSum)
        
        for nums in range(len(grumpy)):
            if grumpy[nums] == 0:
                maxSum += customers[nums]
        return maxSum
            
                
                
                
                
            
        