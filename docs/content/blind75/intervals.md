---
comments: True
---

# Intervals

## Table of Contents

- [x] [57. Insert Interval](https://leetcode.cn/problems/insert-interval/) (Medium)
- [x] [56. Merge Intervals](https://leetcode.cn/problems/merge-intervals/) (Medium)
- [x] [252. Meeting Rooms](https://leetcode.cn/problems/meeting-rooms/) (Easy) 👑
- [x] [253. Meeting Rooms II](https://leetcode.cn/problems/meeting-rooms-ii/) (Medium) 👑
- [ ] [254. Factor Combinations](https://leetcode.cn/problems/factor-combinations/) (Medium) 👑

## 57. Insert Interval

-   [LeetCode](https://leetcode.com/problems/insert-interval/) | [LeetCode CH](https://leetcode.cn/problems/insert-interval/) (Medium)

-   Tags: array

```python title="57. Insert Interval - Python Solution"
from typing import List


# Interval
def insert(
    intervals: List[List[int]], newInterval: List[int]
) -> List[List[int]]:
    n = len(intervals)

    if n == 0:
        return [newInterval]

    if newInterval[1] < intervals[0][0]:
        return [newInterval] + intervals

    if newInterval[0] > intervals[-1][1]:
        return intervals + [newInterval]

    i = 0
    result = []

    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    while i < n:
        result.append(intervals[i])
        i += 1

    return result


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(insert(intervals, newInterval))  # [[1, 5], [6, 9]]

```

## 56. Merge Intervals

-   [LeetCode](https://leetcode.com/problems/merge-intervals/) | [LeetCode CH](https://leetcode.cn/problems/merge-intervals/) (Medium)

-   Tags: array, sorting
-   Merge all overlapping intervals.

<iframe width="560" height="315" src="https://www.youtube.com/embed/44H3cEC2fFM?si=J-Jr_Fg2eDse3-de" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


```python title="56. Merge Intervals - Python Solution"
from typing import List


# Intervals
def merge(intervals: List[List[int]]) -> List[List[int]]:
    n = len(intervals)
    if n <= 1:
        return intervals

    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]

    for i in range(1, n):
        if intervals[i][0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])

    return res


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# [[1, 6], [8, 10], [15, 18]]

```

```cpp title="56. Merge Intervals - C++ Solution"
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// Interval
vector<vector<int>> merge(vector<vector<int>>& intervals) {
    sort(intervals.begin(), intervals.end());
    vector<vector<int>> res;

    for (auto& range : intervals) {
        if (!res.empty() && range[0] <= res.back()[1]) {
            res.back()[1] = max(res.back()[1], range[1]);
        } else {
            res.emplace_back(range);
        }
    }
    return res;
}

int main() {
    vector<vector<int>> intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
    vector<vector<int>> res = merge(intervals);
    for (auto& range : res) {
        cout << range[0] << ", " << range[1] << endl;
    }
    return 0;
}

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

## 254. Factor Combinations

-   [LeetCode](https://leetcode.com/problems/factor-combinations/) | [LeetCode CH](https://leetcode.cn/problems/factor-combinations/) (Medium)

-   Tags: backtracking
