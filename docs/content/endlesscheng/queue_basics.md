---
comments: True
---

# Queue Basics

## Table of Contents

- [ ] [933. Number of Recent Calls](https://leetcode.cn/problems/number-of-recent-calls/) (Easy)
- [ ] [950. Reveal Cards In Increasing Order](https://leetcode.cn/problems/reveal-cards-in-increasing-order/) (Medium)
- [ ] [649. Dota2 Senate](https://leetcode.cn/problems/dota2-senate/) (Medium)
- [x] [346. Moving Average from Data Stream](https://leetcode.cn/problems/moving-average-from-data-stream/) (Easy) 👑
- [x] [362. Design Hit Counter](https://leetcode.cn/problems/design-hit-counter/) (Medium) 👑
- [ ] [379. Design Phone Directory](https://leetcode.cn/problems/design-phone-directory/) (Medium) 👑
- [x] [1429. First Unique Number](https://leetcode.cn/problems/first-unique-number/) (Medium) 👑
- [ ] [2534. Time Taken to Cross the Door](https://leetcode.cn/problems/time-taken-to-cross-the-door/) (Hard) 👑

## 933. Number of Recent Calls

-   [LeetCode](https://leetcode.com/problems/number-of-recent-calls/) | [LeetCode CH](https://leetcode.cn/problems/number-of-recent-calls/) (Easy)

-   Tags: design, queue, data stream
## 950. Reveal Cards In Increasing Order

-   [LeetCode](https://leetcode.com/problems/reveal-cards-in-increasing-order/) | [LeetCode CH](https://leetcode.cn/problems/reveal-cards-in-increasing-order/) (Medium)

-   Tags: array, queue, sorting, simulation
## 649. Dota2 Senate

-   [LeetCode](https://leetcode.com/problems/dota2-senate/) | [LeetCode CH](https://leetcode.cn/problems/dota2-senate/) (Medium)

-   Tags: string, greedy, queue
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

## 362. Design Hit Counter

-   [LeetCode](https://leetcode.com/problems/design-hit-counter/) | [LeetCode CH](https://leetcode.cn/problems/design-hit-counter/) (Medium)

-   Tags: array, binary search, design, queue, data stream

```python title="362. Design Hit Counter - Python Solution"
from collections import deque


class HitCounter:

    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # Remove hits that are older than 5 minutes (300 seconds)
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)


obj = HitCounter()
obj.hit(1)
obj.hit(2)
obj.hit(3)
print(obj.getHits(4))  # 3
obj.hit(300)
print(obj.getHits(300))  # 4
print(obj.getHits(301))  # 3

```

## 379. Design Phone Directory

-   [LeetCode](https://leetcode.com/problems/design-phone-directory/) | [LeetCode CH](https://leetcode.cn/problems/design-phone-directory/) (Medium)

-   Tags: array, hash table, linked list, design, queue
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

## 2534. Time Taken to Cross the Door

-   [LeetCode](https://leetcode.com/problems/time-taken-to-cross-the-door/) | [LeetCode CH](https://leetcode.cn/problems/time-taken-to-cross-the-door/) (Hard)

-   Tags: array, queue, simulation
