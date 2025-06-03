---
comments: True
---

# Interval

## Table of Contents

- [x] [163. Missing Ranges](https://leetcode.cn/problems/missing-ranges/) (Easy) 👑
- [x] [252. Meeting Rooms](https://leetcode.cn/problems/meeting-rooms/) (Easy) 👑
- [x] [253. Meeting Rooms II](https://leetcode.cn/problems/meeting-rooms-ii/) (Medium) 👑
- [ ] [616. Add Bold Tag in String](https://leetcode.cn/problems/add-bold-tag-in-string/) (Medium) 👑
- [ ] [1272. Remove Interval](https://leetcode.cn/problems/remove-interval/) (Medium) 👑

## 163. Missing Ranges

-   [LeetCode](https://leetcode.com/problems/missing-ranges/) | [LeetCode CH](https://leetcode.cn/problems/missing-ranges/) (Easy)

-   Tags: array

```python title="163. Missing Ranges - Python Solution"
from typing import List


def findMissingRanges(
    nums: List[int], lower: int, upper: int
) -> List[List[int]]:
    n = len(nums)
    res = []
    if n == 0:
        return [[lower, upper]]

    # start
    if nums[0] > lower:
        res.append([lower, nums[0] - 1])

    # middle
    for i in range(n - 1):
        if nums[i] + 1 < nums[i + 1]:
            res.append([nums[i] + 1, nums[i + 1] - 1])

    # end
    if nums[-1] < upper:
        res.append([nums[-1] + 1, upper])

    return res


def findMissingRangesCompact(
    nums: List[int], lower: int, upper: int
) -> List[List[int]]:
    res = []

    for num in nums + [upper + 1]:
        if num > lower:
            res.append([lower, num - 1])
        lower = num + 1

    return res


if __name__ == "__main__":
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    assert findMissingRanges(nums, lower, upper) == [
        [2, 2],
        [4, 49],
        [51, 74],
        [76, 99],
    ]
    assert findMissingRangesCompact(nums, lower, upper) == [
        [2, 2],
        [4, 49],
        [51, 74],
        [76, 99],
    ]

```

## 252. Meeting Rooms

-   [LeetCode](https://leetcode.com/problems/meeting-rooms/) | [LeetCode CH](https://leetcode.cn/problems/meeting-rooms/) (Easy)

-   Tags: array, sorting

```python title="252. Meeting Rooms - Python Solution"
from typing import List


# Interval
def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    n = len(intervals)

    if n <= 1:
        return True

    for i in range(1, n):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert not canAttendMeetings(intervals)

```

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

## 616. Add Bold Tag in String

-   [LeetCode](https://leetcode.com/problems/add-bold-tag-in-string/) | [LeetCode CH](https://leetcode.cn/problems/add-bold-tag-in-string/) (Medium)

-   Tags: array, hash table, string, trie, string matching
## 1272. Remove Interval

-   [LeetCode](https://leetcode.com/problems/remove-interval/) | [LeetCode CH](https://leetcode.cn/problems/remove-interval/) (Medium)

-   Tags: array
