---
comments: True
---

# Queue

## Table of Contents

- [x] [232. Implement Queue using Stacks](https://leetcode.cn/problems/implement-queue-using-stacks/) (Easy)
- [x] [225. Implement Stack using Queues](https://leetcode.cn/problems/implement-stack-using-queues/) (Easy)

## 232. Implement Queue using Stacks

-   [LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/) | [LeetCode CH](https://leetcode.cn/problems/implement-queue-using-stacks/) (Easy)

-   Tags: stack, design, queue
-   Implement the following operations of a queue using stacks.
    -   `push(x)` - Push element x to the back of queue.
    -   `pop()` - Removes the element from in front of queue.
    -   `peek()` - Get the front element.
    -   `empty()` - Return whether the queue is empty.

```python title="232. Implement Queue using Stacks - Python Solution"
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

```

## 225. Implement Stack using Queues

-   [LeetCode](https://leetcode.com/problems/implement-stack-using-queues/) | [LeetCode CH](https://leetcode.cn/problems/implement-stack-using-queues/) (Easy)

-   Tags: stack, design, queue
```python title="225. Implement Stack using Queues - Python Solution"
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

```
