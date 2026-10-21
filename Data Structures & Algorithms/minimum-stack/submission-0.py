class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.smallest[-1] if self.smallest else val)
        self.smallest.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.smallest.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest[-1]
