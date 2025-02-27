class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checkForAllPackages(capacity):
            count = 0 
            sumOfWeights = 0 
            for weight in weights: 
                if sumOfWeights + weight <= capacity:
                    sumOfWeights = sumOfWeights + weight
                else:
                    count += 1
                    sumOfWeights = weight 
            return count + 1

        high = sum(weights)
        low = max(weights) 
        while low < high:
            middle = (low + high) // 2
            noOfDays = checkForAllPackages(middle)
            if noOfDays <= days:
                high = middle
            else:
                low = middle + 1
        return high




   








        