"""
-   Implement a stack that supports push, pop, top, and retrieving the minimum element in constant time.
"""


# Stack
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append((val, min(val, self.getMin())))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


obj = MinStack()
obj.push(3)
obj.push(2)
obj.pop()
print(obj.top())  # 3
print(obj.getMin())  # 3
