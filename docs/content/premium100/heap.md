---
comments: True
---

# Heap

## Table of Contents

- [x] [1086. High Five](https://leetcode.cn/problems/high-five/) (Easy) 👑
- [ ] [1167. Minimum Cost to Connect Sticks](https://leetcode.cn/problems/minimum-cost-to-connect-sticks/) (Medium) 👑
- [ ] [1057. Campus Bikes](https://leetcode.cn/problems/campus-bikes/) (Medium) 👑
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
## 1057. Campus Bikes

-   [LeetCode](https://leetcode.com/problems/campus-bikes/) | [LeetCode CH](https://leetcode.cn/problems/campus-bikes/) (Medium)

-   Tags: array, greedy, sorting
## 358. Rearrange String k Distance Apart

-   [LeetCode](https://leetcode.com/problems/rearrange-string-k-distance-apart/) | [LeetCode CH](https://leetcode.cn/problems/rearrange-string-k-distance-apart/) (Hard)

-   Tags: hash table, string, greedy, sorting, heap priority queue, counting
