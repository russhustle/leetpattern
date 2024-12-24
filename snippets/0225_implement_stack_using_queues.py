from collections import deque


# Queue
class MyStack:

    def __init__(self):
        self.q1 = deque()  # main queue
        self.q2 = deque()  # auxiliary queue

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return res

    def empty(self) -> bool:
        return not self.q1


obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())  # 4
print(obj.top())  # 3
print(obj.empty())  # False
print(obj.pop())  # 3
