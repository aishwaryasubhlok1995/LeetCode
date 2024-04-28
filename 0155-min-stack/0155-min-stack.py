import heapq
class MinStack:

    def __init__(self):
        self.arr = []
        self.minimum = math.inf

    def push(self, val: int) -> None:
        if len(self.arr) == 0:
            self.arr.append([val, val])
        else:
            if val < self.arr[-1][1]:
                 self.arr.append([val, val])
            else:
                self.arr.append([val, self.arr[-1][1]])

    def pop(self) -> None:
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