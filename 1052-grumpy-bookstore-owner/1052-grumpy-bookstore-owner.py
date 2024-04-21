class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        i = 0 
        j = 0
        windowSize = minutes
        maxElement = 0
        ans = 0
        sumELements = 0
        counter = 1 
        while j < len(customers):
            if counter <= windowSize:
                if grumpy[j] != 0:
                    sumELements += customers[j]
                if counter == windowSize:
                    maxElement = max(maxElement, sumELements)
                j += 1
                counter += 1
            else:
                if grumpy[j] != 0:
                    sumELements += customers[j]
                if grumpy[i] != 0:
                    sumELements -= customers[i]
                maxElement = max(maxElement, sumELements)
                i = i + 1
                j += 1
        
        print(maxElement)
        for nums in range(len(grumpy)):
            if grumpy[nums] == 0:
                ans += customers[nums]
        print(ans)
        return ans+maxElement
            
                
                
                
                
            
        