class MinStack:
    def __init__(self):
        self.heap = []
        self.min = []
        return

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.min.append(min(val, self.min[-1] if self.min else val))

        return

    def pop(self) -> None:
        self.min.pop(-1)
        self.heap.pop(-1)
        return

    def top(self) -> int:
        return self.heap[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
