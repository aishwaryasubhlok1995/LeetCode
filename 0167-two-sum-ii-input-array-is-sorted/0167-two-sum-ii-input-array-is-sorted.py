class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i<j:
            sumOfNums = numbers[i] + numbers[j] 
            if sumOfNums == target:
                return [i+1, j+1]
            elif sumOfNums > target:
                j = j-1
            elif sumOfNums < target:
                i = i+1
           
            
                
                
            
        