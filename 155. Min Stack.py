class MinStack:
    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, val: int) -> None:
        if not self.stack or self.min_values[-1] >= val:
            self.min_values.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        if self.min_values[-1] == self.stack[-1]:
            self.min_values.pop()
        
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]   

    def getMin(self) -> int:
        return self.min_values[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()