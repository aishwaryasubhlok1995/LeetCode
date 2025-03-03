class MyQueue:

    def __init__(self):
        self.stack1 = []
        

    def push(self, x: int) -> None:
        stack2 = []
        for i in range(len(self.stack1)):
            stack2.append(self.stack1.pop())
        stack2.append(x)
        for i in range(len(stack2)):
            self.stack1.append(stack2.pop())
        

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        if len(self.stack1) > 0:
            return False
        return True 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()