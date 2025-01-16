import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.weight = []
        curr = 0
        for i in self.w:
            curr += i
            self.weight.append(curr)

    def pickIndex(self) -> int:
        value = random.randint(1, self.weight[-1])
        start = 0
        end = len(self.weight) - 1
        while start<end:
            mid = (start + end)//2
            if self.weight[mid] == value:
                return mid
            if value> self.weight[mid]:
                start = mid+1
            else:
                end = mid
        return end

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()