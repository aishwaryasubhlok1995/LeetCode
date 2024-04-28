import heapq
class MinStack:

    def __init__(self):
        self.arr = []
        self.minimum = math.inf

    def push(self, val: int) -> None:
        self.minimum = min(self.minimum, val)
        self.arr.append([val, self.minimum])

    def pop(self) -> None:
        if len(self.arr) == 1:
            self.minimum = math.inf
        else:
            self.minimum = self.arr[-2][1]
        return self.arr.pop(-1)
        
        

    def top(self) -> int:
        return self.arr[-1][0]
        

    def getMin(self) -> int:
        return self.arr[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()