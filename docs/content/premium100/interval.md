---
comments: True
---

# Interval

## Table of Contents

- [ ] [163. Missing Ranges](https://leetcode.cn/problems/missing-ranges/) (Easy) 👑
- [x] [252. Meeting Rooms](https://leetcode.cn/problems/meeting-rooms/) (Easy) 👑
- [x] [253. Meeting Rooms II](https://leetcode.cn/problems/meeting-rooms-ii/) (Medium) 👑
- [ ] [616. Add Bold Tag in String](https://leetcode.cn/problems/add-bold-tag-in-string/) (Medium) 👑
- [ ] [1272. Remove Interval](https://leetcode.cn/problems/remove-interval/) (Medium) 👑

## 163. Missing Ranges

-   [LeetCode](https://leetcode.com/problems/missing-ranges/) | [LeetCode CH](https://leetcode.cn/problems/missing-ranges/) (Easy)

-   Tags: array

## 252. Meeting Rooms

-   [LeetCode](https://leetcode.com/problems/meeting-rooms/) | [LeetCode CH](https://leetcode.cn/problems/meeting-rooms/) (Easy)

-   Tags: array, sorting

```python title="252. Meeting Rooms - Python Solution"
from typing import List


# Interval
def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True


intervals = [[0, 30], [5, 10], [15, 20]]
print(canAttendMeetings(intervals))  # False

```

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

## 616. Add Bold Tag in String

-   [LeetCode](https://leetcode.com/problems/add-bold-tag-in-string/) | [LeetCode CH](https://leetcode.cn/problems/add-bold-tag-in-string/) (Medium)

-   Tags: array, hash table, string, trie, string matching

## 1272. Remove Interval

-   [LeetCode](https://leetcode.com/problems/remove-interval/) | [LeetCode CH](https://leetcode.cn/problems/remove-interval/) (Medium)

-   Tags: array
