---
comments: True
---

# Queue

## Table of Contents

- [x] [346. Moving Average from Data Stream](https://leetcode.cn/problems/moving-average-from-data-stream/) (Easy) 👑
- [x] [1429. First Unique Number](https://leetcode.cn/problems/first-unique-number/) (Medium) 👑

## 346. Moving Average from Data Stream

-   [LeetCode](https://leetcode.com/problems/moving-average-from-data-stream/) | [LeetCode CH](https://leetcode.cn/problems/moving-average-from-data-stream/) (Easy)

-   Tags: array, design, queue, data stream
```python title="346. Moving Average from Data Stream - Python Solution"
from collections import deque


# Deque
class MovingAverage:
    def __init__(self, size: int):
        self.q = deque()
        self.cur = 0
        self.sum = 0
        self.size = size

    def next(self, val: int) -> float:
        if self.cur >= self.size:
            self.sum -= self.q.popleft()
            self.cur -= 1

        self.q.append(val)
        self.sum += val
        self.cur += 1

        return self.sum / self.cur


if __name__ == "__main__":
    ma = MovingAverage(3)
    assert ma.next(1) == 1.0
    assert ma.next(10) == 5.5
    assert ma.next(3) == 4.666666666666667
    assert ma.next(5) == 6.0

```

## 1429. First Unique Number

-   [LeetCode](https://leetcode.com/problems/first-unique-number/) | [LeetCode CH](https://leetcode.cn/problems/first-unique-number/) (Medium)

-   Tags: array, hash table, design, queue, data stream
```python title="1429. First Unique Number - Python Solution"
from collections import defaultdict, deque
from typing import List


# Deque
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.all = set()
        self.multi = set()

        for num in nums:
            if num in self.all:
                self.multi.add(num)
            self.all.add(num)

        self.q = deque([i for i in nums if i not in self.multi])

    def showFirstUnique(self) -> int:
        while self.q and self.q[0] in self.multi:
            self.q.popleft()
        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        if value not in self.all:
            self.all.add(value)
            self.q.append(value)
        elif value not in self.multi:
            self.multi.add(value)


if __name__ == "__main__":
    nums = [2, 3, 5]
    firstUnique = FirstUnique(nums)
    assert firstUnique.showFirstUnique() == 2
    firstUnique.add(5)
    assert firstUnique.showFirstUnique() == 2
    firstUnique.add(2)
    assert firstUnique.showFirstUnique() == 3
    firstUnique.add(3)
    assert firstUnique.showFirstUnique() == -1

```

