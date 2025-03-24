import random
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[::]
        self.temp = nums

    def reset(self) -> List[int]:
        return self.original 
        
    def shuffle(self) -> List[int]:
        for i in range(len(self.original)):
            idx = random.randint(i, len(self.temp)-1)
            self.temp[idx], self.temp[i] = self.temp[i], self.temp[idx]
        return self.temp
           
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()