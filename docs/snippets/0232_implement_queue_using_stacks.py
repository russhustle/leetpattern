class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        if self.stack_out:
            return self.stack_out.pop()
        else:
            for _ in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        answer = self.pop()
        self.stack_out.append(answer)
        return answer

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)


obj = MyQueue()
obj.push(1)
print(obj.pop())  # 1
print(obj.peek())  # None
print(obj.empty())  # False
