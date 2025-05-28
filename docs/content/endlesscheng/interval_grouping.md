---
comments: True
---

# Interval Grouping

## Table of Contents

- [ ] [2406. Divide Intervals Into Minimum Number of Groups](https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups/) (Medium)
- [x] [253. Meeting Rooms II](https://leetcode.cn/problems/meeting-rooms-ii/) (Medium) 👑

## 2406. Divide Intervals Into Minimum Number of Groups

-   [LeetCode](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/) | [LeetCode CH](https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups/) (Medium)

-   Tags: array, two pointers, greedy, sorting, heap priority queue, prefix sum
## 253. Meeting Rooms II

-   [LeetCode](https://leetcode.com/problems/meeting-rooms-ii/) | [LeetCode CH](https://leetcode.cn/problems/meeting-rooms-ii/) (Medium)

-   Tags: array, two pointers, greedy, sorting, heap priority queue, prefix sum

```python title="253. Meeting Rooms II - Python Solution"
import heapq
from typing import List


# Heap
def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    heap = [intervals[0][1]]

    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])

    return len(heap)


intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals))  # 2

```
