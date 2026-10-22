class MinStack:

    def __init__(self):
        self.stack = []
        self.currentMin = float("inf")
        self.backupMin = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.currentMin:
            self.backupMin = self.currentMin
            self.currentMin = val
            

    def pop(self) -> None:
        if self.stack:
            removed = self.top()
            if removed == self.currentMin:
                self.currentMin = self.backupMin
            self.stack = self.stack[:-1]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.currentMin
