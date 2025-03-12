---
comments: True
---

# Queue Basics

- [ ] [933. Number of Recent Calls](https://leetcode.cn/problems/number-of-recent-calls/) (Easy)
- [ ] [950. Reveal Cards In Increasing Order](https://leetcode.cn/problems/reveal-cards-in-increasing-order/) (Medium)
- [ ] [649. Dota2 Senate](https://leetcode.cn/problems/dota2-senate/) (Medium)
- [ ] [346. Moving Average from Data Stream](https://leetcode.cn/problems/moving-average-from-data-stream/) (Easy) 👑
- [x] [362. Design Hit Counter](https://leetcode.cn/problems/design-hit-counter/) (Medium) 👑
- [ ] [379. Design Phone Directory](https://leetcode.cn/problems/design-phone-directory/) (Medium) 👑
- [ ] [1429. First Unique Number](https://leetcode.cn/problems/first-unique-number/) (Medium) 👑
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

## 2534. Time Taken to Cross the Door

-   [LeetCode](https://leetcode.com/problems/time-taken-to-cross-the-door/) | [LeetCode CH](https://leetcode.cn/problems/time-taken-to-cross-the-door/) (Hard)

-   Tags: array, queue, simulation
