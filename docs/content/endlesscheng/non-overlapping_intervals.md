---
comments: True
---

# Non-Overlapping Intervals

## Table of Contents

- [x] [435. Non-overlapping Intervals](https://leetcode.cn/problems/non-overlapping-intervals/) (Medium)
- [ ] [646. Maximum Length of Pair Chain](https://leetcode.cn/problems/maximum-length-of-pair-chain/) (Medium)
- [ ] [1520. Maximum Number of Non-Overlapping Substrings](https://leetcode.cn/problems/maximum-number-of-non-overlapping-substrings/) (Hard)
- [ ] [3458. Select K Disjoint Special Substrings](https://leetcode.cn/problems/select-k-disjoint-special-substrings/) (Medium)

## 435. Non-overlapping Intervals

-   [LeetCode](https://leetcode.com/problems/non-overlapping-intervals/) | [LeetCode CH](https://leetcode.cn/problems/non-overlapping-intervals/) (Medium)

-   Tags: array, dynamic programming, greedy, sorting
```python title="435. Non-overlapping Intervals - Python Solution"
from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    if len(intervals) <= 1:
        return 0

    intervals.sort(key=lambda x: x[0])
    result = 0

    for i in range(1, len(intervals)):
        if intervals[i][0] >= intervals[i - 1][1]:
            continue
        else:
            result += 1
            intervals[i][1] = min(intervals[i][1], intervals[i - 1][1])

    return result


print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # 1

```

## 646. Maximum Length of Pair Chain

-   [LeetCode](https://leetcode.com/problems/maximum-length-of-pair-chain/) | [LeetCode CH](https://leetcode.cn/problems/maximum-length-of-pair-chain/) (Medium)

-   Tags: array, dynamic programming, greedy, sorting
## 1520. Maximum Number of Non-Overlapping Substrings

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-non-overlapping-substrings/) (Hard)

-   Tags: string, greedy
## 3458. Select K Disjoint Special Substrings

-   [LeetCode](https://leetcode.com/problems/select-k-disjoint-special-substrings/) | [LeetCode CH](https://leetcode.cn/problems/select-k-disjoint-special-substrings/) (Medium)

-   Tags: hash table, string, dynamic programming, greedy, sorting
