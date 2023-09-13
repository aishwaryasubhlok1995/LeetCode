class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        arr = []
        while i < j:
            ans = numbers[i] + numbers[j]  
            if ans < target:
                i += 1
            if ans > target:
                j -= 1
            if ans == target:
                arr.append(i+1)
                arr.append(j+1)
                return arr
        return arr
                
            
            
        