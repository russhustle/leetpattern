---
comments: True
---

# Randomized Algorithms

## Table of Contents

- [ ] [398. Random Pick Index](https://leetcode.cn/problems/random-pick-index/) (Medium)
- [ ] [382. Linked List Random Node](https://leetcode.cn/problems/linked-list-random-node/) (Medium)
- [ ] [384. Shuffle an Array](https://leetcode.cn/problems/shuffle-an-array/) (Medium)
- [ ] [470. Implement Rand10() Using Rand7()](https://leetcode.cn/problems/implement-rand10-using-rand7/) (Medium)
- [ ] [528. Random Pick with Weight](https://leetcode.cn/problems/random-pick-with-weight/) (Medium)
- [ ] [710. Random Pick with Blacklist](https://leetcode.cn/problems/random-pick-with-blacklist/) (Hard)
- [ ] [478. Generate Random Point in a Circle](https://leetcode.cn/problems/generate-random-point-in-a-circle/) (Medium)
- [ ] [497. Random Point in Non-overlapping Rectangles](https://leetcode.cn/problems/random-point-in-non-overlapping-rectangles/) (Medium)
- [ ] [519. Random Flip Matrix](https://leetcode.cn/problems/random-flip-matrix/) (Medium)
- [x] [380. Insert Delete GetRandom O(1)](https://leetcode.cn/problems/insert-delete-getrandom-o1/) (Medium)
- [ ] [381. Insert Delete GetRandom O(1) - Duplicates allowed](https://leetcode.cn/problems/insert-delete-getrandom-o1-duplicates-allowed/) (Hard)
- [ ] [1515. Best Position for a Service Centre](https://leetcode.cn/problems/best-position-for-a-service-centre/) (Hard)
- [ ] [1968. Array With Elements Not Equal to Average of Neighbors](https://leetcode.cn/problems/array-with-elements-not-equal-to-average-of-neighbors/) (Medium)

## 398. Random Pick Index

-   [LeetCode](https://leetcode.com/problems/random-pick-index/) | [LeetCode CH](https://leetcode.cn/problems/random-pick-index/) (Medium)

-   Tags: hash table, math, reservoir sampling, randomized
## 382. Linked List Random Node

-   [LeetCode](https://leetcode.com/problems/linked-list-random-node/) | [LeetCode CH](https://leetcode.cn/problems/linked-list-random-node/) (Medium)

-   Tags: linked list, math, reservoir sampling, randomized
## 384. Shuffle an Array

-   [LeetCode](https://leetcode.com/problems/shuffle-an-array/) | [LeetCode CH](https://leetcode.cn/problems/shuffle-an-array/) (Medium)

-   Tags: array, math, design, randomized
## 470. Implement Rand10() Using Rand7()

-   [LeetCode](https://leetcode.com/problems/implement-rand10-using-rand7/) | [LeetCode CH](https://leetcode.cn/problems/implement-rand10-using-rand7/) (Medium)

-   Tags: math, rejection sampling, randomized, probability and statistics
## 528. Random Pick with Weight

-   [LeetCode](https://leetcode.com/problems/random-pick-with-weight/) | [LeetCode CH](https://leetcode.cn/problems/random-pick-with-weight/) (Medium)

-   Tags: array, math, binary search, prefix sum, randomized
## 710. Random Pick with Blacklist

-   [LeetCode](https://leetcode.com/problems/random-pick-with-blacklist/) | [LeetCode CH](https://leetcode.cn/problems/random-pick-with-blacklist/) (Hard)

-   Tags: array, hash table, math, binary search, sorting, randomized
## 478. Generate Random Point in a Circle

-   [LeetCode](https://leetcode.com/problems/generate-random-point-in-a-circle/) | [LeetCode CH](https://leetcode.cn/problems/generate-random-point-in-a-circle/) (Medium)

-   Tags: math, geometry, rejection sampling, randomized
## 497. Random Point in Non-overlapping Rectangles

-   [LeetCode](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/) | [LeetCode CH](https://leetcode.cn/problems/random-point-in-non-overlapping-rectangles/) (Medium)

-   Tags: array, math, binary search, reservoir sampling, prefix sum, ordered set, randomized
## 519. Random Flip Matrix

-   [LeetCode](https://leetcode.com/problems/random-flip-matrix/) | [LeetCode CH](https://leetcode.cn/problems/random-flip-matrix/) (Medium)

-   Tags: hash table, math, reservoir sampling, randomized
## 380. Insert Delete GetRandom O(1)

-   [LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1/) | [LeetCode CH](https://leetcode.cn/problems/insert-delete-getrandom-o1/) (Medium)

-   Tags: array, hash table, math, design, randomized

```python title="380. Insert Delete GetRandom O(1) - Python Solution"
import random


class RandomizedSet:
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        last_element = self.list[-1]
        idx = self.dict[val]
        self.list[idx] = last_element
        self.dict[last_element] = idx
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


obj = RandomizedSet()
print(obj.insert(1))  # True
print(obj.remove(2))  # False
print(obj.insert(2))  # True
print(obj.getRandom())  # 1 or 2
print(obj.remove(1))  # True

```

## 381. Insert Delete GetRandom O(1) - Duplicates allowed

-   [LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/) | [LeetCode CH](https://leetcode.cn/problems/insert-delete-getrandom-o1-duplicates-allowed/) (Hard)

-   Tags: array, hash table, math, design, randomized
## 1515. Best Position for a Service Centre

-   [LeetCode](https://leetcode.com/problems/best-position-for-a-service-centre/) | [LeetCode CH](https://leetcode.cn/problems/best-position-for-a-service-centre/) (Hard)

-   Tags: array, math, geometry, randomized
## 1968. Array With Elements Not Equal to Average of Neighbors

-   [LeetCode](https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/) | [LeetCode CH](https://leetcode.cn/problems/array-with-elements-not-equal-to-average-of-neighbors/) (Medium)

-   Tags: array, greedy, sorting
