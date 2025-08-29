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
- Given an array of meeting time `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.

```python title="253. Meeting Rooms II - Python Solution"
import heapq
from typing import List


# Heap
def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    minHeap = [intervals[0][1]]

    for i in range(1, len(intervals)):
        if intervals[i][0] >= minHeap[0]:
            heapq.heappop(minHeap)
        heapq.heappush(minHeap, intervals[i][1])

    return len(minHeap)


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert minMeetingRooms(intervals) == 2

```
