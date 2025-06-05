---
comments: True
---

# Intervals

## Table of Contents

- [x] [228. Summary Ranges](https://leetcode.cn/problems/summary-ranges/) (Easy)
- [x] [56. Merge Intervals](https://leetcode.cn/problems/merge-intervals/) (Medium)
- [x] [57. Insert Interval](https://leetcode.cn/problems/insert-interval/) (Medium)
- [x] [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium)

## 228. Summary Ranges

-   [LeetCode](https://leetcode.com/problems/summary-ranges/) | [LeetCode CH](https://leetcode.cn/problems/summary-ranges/) (Easy)

-   Tags: array

```python title="228. Summary Ranges - Python Solution"
from typing import List


# Variable Sliding Window
def summaryRanges(nums: List[int]) -> List[str]:
    left, right = 0, 0
    n = len(nums)
    res = []

    while left < n:
        while right + 1 < n and nums[right] + 1 == nums[right + 1]:
            right += 1

        if left == right:
            res.append(f"{nums[left]}")
        else:
            res.append(f"{nums[left]}->{nums[right]}")

        right += 1
        left = right

    return res


if __name__ == "__main__":
    print(summaryRanges([0, 1, 2, 4, 5, 7]))
    # ["0->2", "4->5", "7"]
    print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))
    # ["0", "2->4", "6", "8->9"]

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

## 452. Minimum Number of Arrows to Burst Balloons

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium)

-   Tags: array, greedy, sorting
-   Return the minimum number of arrows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/lPmkKnvNPrw?si=P0rkcvTOxRGoFpkG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

-   Differece between two versions
    1. Start from 1: if there is no overlap, we add one more arrow.
    2. Start from the number of balloons: if there is overlap, we need to reduce one arrow.


```python title="452. Minimum Number of Arrows to Burst Balloons - Python Solution"
from typing import List

import matplotlib.pyplot as plt


# Greedy - Interval
def findMinArrowShotsGreedy1(points: List[List[int]]) -> int:
    n = len(points)
    if n <= 1:
        return n

    res = 1
    points.sort(key=lambda x: x[0])

    for i in range(1, n):
        if points[i][0] > points[i - 1][1]:
            res += 1
        else:
            points[i][1] = min(points[i][1], points[i - 1][1])
    return res


# Greedy - Interval (Neetcode's version)
def findMinArrowShotsGreedy2(points: List[List[int]]) -> int:
    res = len(points)
    if res == 0:
        return 0

    points.sort()
    prev = points[0]

    for i in range(1, len(points)):
        cur = points[i]
        if cur[0] <= prev[1]:
            res -= 1
            prev = [cur[0], min(prev[1], cur[1])]
        else:
            prev = cur

    return res


# Greedy - Interval
def findMinArrowShotsGreedy3(points: List[List[int]]) -> int:
    if not points:
        return 0

    points.sort(key=lambda x: x[1])

    res = 1
    cur_end = points[0][1]

    for i in range(1, len(points)):
        if points[i][0] > cur_end:
            res += 1
            cur_end = points[i][1]

    return res


# Utility
def plot(points, i=None):
    plt.figure(figsize=(8, 4))
    for idx in range(len(points)):
        color = "b" if idx == i else "k"
        plt.plot(
            [points[idx][0], points[idx][1]],
            [idx + 1, idx + 1],
            f"{color}o-",
            label=f"Line {idx + 1}",
        )

    plt.title("Find Min Arrow Shots")
    plt.xlabel("X-axis")
    plt.xlim(0, 17)
    plt.grid(True)
    plt.savefig(f"find_min_arrow_shots_{i}.png")
    plt.show()


# |------------|-----------|---------|
# |  Approach  |  Time     |  Space  |
# |------------|-----------|---------|
# |  Greedy    |  O(NlogN) |  O(1)   |
# |------------|-----------|---------|


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(findMinArrowShotsGreedy1(points))  # 2
print(findMinArrowShotsGreedy2(points))  # 2

```
