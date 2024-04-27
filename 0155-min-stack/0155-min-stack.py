import heapq
class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        return self.arr.append(val)

    def pop(self) -> None:
        return self.arr.pop(-1)
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return heapq.nsmallest(1,  self.arr)[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()