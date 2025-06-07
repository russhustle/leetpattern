---
comments: True
---

# Heap

## Table of Contents

- [x] [1086. High Five](https://leetcode.cn/problems/high-five/) (Easy) 👑
- [x] [1167. Minimum Cost to Connect Sticks](https://leetcode.cn/problems/minimum-cost-to-connect-sticks/) (Medium) 👑
- [x] [1057. Campus Bikes](https://leetcode.cn/problems/campus-bikes/) (Medium) 👑
- [ ] [358. Rearrange String k Distance Apart](https://leetcode.cn/problems/rearrange-string-k-distance-apart/) (Hard) 👑

## 1086. High Five

-   [LeetCode](https://leetcode.com/problems/high-five/) | [LeetCode CH](https://leetcode.cn/problems/high-five/) (Easy)

-   Tags: array, hash table, sorting, heap priority queue

```python title="1086. High Five - Python Solution"
from collections import defaultdict
from heapq import heappush, heappushpop
from typing import List


# Heap
def highFive(items: List[List[int]]) -> List[List[int]]:
    hashmap = defaultdict(list)  # id: scores

    for idx, score in items:
        if len(hashmap[idx]) < 5:
            heappush(hashmap[idx], score)
        else:
            heappushpop(hashmap[idx], score)

    res = []
    for idx in sorted(hashmap.keys()):
        res.append([idx, sum(hashmap[idx]) // 5])
    return res


if __name__ == "__main__":
    items = [
        [1, 91],
        [1, 92],
        [2, 93],
        [2, 97],
        [1, 60],
        [2, 77],
        [1, 65],
        [1, 87],
        [1, 100],
        [2, 100],
        [2, 76],
    ]
    assert highFive(items) == [[1, 87], [2, 88]]

```

## 1167. Minimum Cost to Connect Sticks

-   [LeetCode](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-to-connect-sticks/) (Medium)

-   Tags: array, greedy, heap priority queue

```python title="1167. Minimum Cost to Connect Sticks - Python Solution"
from heapq import heapify, heappop, heappush
from typing import List


# Heap
def connectSticks(sticks: List[int]) -> int:
    n = len(sticks)
    heapify(sticks)
    res = 0

    while n > 1:
        x = heappop(sticks)
        y = heappop(sticks)
        res += x + y
        heappush(sticks, x + y)
        n -= 1

    return res


if __name__ == "__main__":
    assert connectSticks([2, 4, 3]) == 14
    assert connectSticks([1, 8, 3, 5]) == 30
    assert connectSticks([5]) == 0
    assert connectSticks([1, 2, 3, 4, 5]) == 33
    assert connectSticks([1, 1, 1]) == 5

```

## 1057. Campus Bikes

-   [LeetCode](https://leetcode.com/problems/campus-bikes/) | [LeetCode CH](https://leetcode.cn/problems/campus-bikes/) (Medium)

-   Tags: array, greedy, sorting

```python title="1057. Campus Bikes - Python Solution"
from heapq import heappop, heappush
from typing import List


# Heap
def assignBikes(workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
    dist = []
    done1, done2 = set(), set()
    res = [0 for _ in range(len(workers))]

    for i, w in enumerate(workers):
        for j, b in enumerate(bikes):
            d = abs(w[0] - b[0]) + abs(w[1] - b[1])
            heappush(dist, (d, i, j))

    while dist:
        d, i, j = heappop(dist)
        if i not in done1 and j not in done2:
            res[i] = j
            done1.add(i)
            done2.add(j)

    return res


if __name__ == "__main__":
    workers = [[0, 0], [2, 1]]
    bikes = [[1, 2], [3, 3]]
    assert assignBikes(workers, bikes) == [1, 0]
    workers = [[0, 0], [1, 1], [2, 0]]
    bikes = [[1, 0], [2, 2], [2, 1]]
    assert assignBikes(workers, bikes) == [0, 2, 1]

```

## 358. Rearrange String k Distance Apart

-   [LeetCode](https://leetcode.com/problems/rearrange-string-k-distance-apart/) | [LeetCode CH](https://leetcode.cn/problems/rearrange-string-k-distance-apart/) (Hard)

-   Tags: hash table, string, greedy, sorting, heap priority queue, counting
