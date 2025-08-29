---
comments: True
---

# Intervals

## Table of Contents

- [x] [55. Jump Game](https://leetcode.cn/problems/jump-game/) (Medium)
- [x] [45. Jump Game II](https://leetcode.cn/problems/jump-game-ii/) (Medium)
- [x] [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium)
- [x] [435. Non-overlapping Intervals](https://leetcode.cn/problems/non-overlapping-intervals/) (Medium)
- [x] [763. Partition Labels](https://leetcode.cn/problems/partition-labels/) (Medium)
- [x] [56. Merge Intervals](https://leetcode.cn/problems/merge-intervals/) (Medium)

## 55. Jump Game

-   [LeetCode](https://leetcode.com/problems/jump-game/) | [LeetCode CH](https://leetcode.cn/problems/jump-game/) (Medium)

-   Tags: array, dynamic programming, greedy
- Return `True` if you can reach the last index, otherwise `False`.

```python title="55. Jump Game - Python Solution"
from typing import List


# Greedy - Interval
def canJump(nums: List[int]) -> bool:
    n = len(nums)
    reach = 0
    i = 0

    while reach >= i:
        if reach >= n - 1:
            return True
        reach = max(reach, i + nums[i])
        i += 1

    return False


if __name__ == "__main__":
    assert canJump([2, 3, 1, 1, 4]) is True
    assert canJump([3, 2, 1, 0, 4]) is False

```

```cpp title="55. Jump Game - C++ Solution"
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
   public:
    bool canJump(vector<int>& nums) {
        int canReach = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            if (i > canReach) return false;
            canReach = max(canReach, i + nums[i]);
        }
        return true;
    }
};

int main() {
    Solution obj;
    vector<int> nums = {2, 3, 1, 1, 4};
    cout << obj.canJump(nums) << endl;
    return 0;
}
```

## 45. Jump Game II

-   [LeetCode](https://leetcode.com/problems/jump-game-ii/) | [LeetCode CH](https://leetcode.cn/problems/jump-game-ii/) (Medium)

-   Tags: array, dynamic programming, greedy
- Return the minimum number of jumps to reach the last index.

```python title="45. Jump Game II - Python Solution"
from typing import List


# Greedy - Interval
def jump(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0

    reach = 0
    left, right = 0, 0
    res = 0

    while right < n - 1:
        for i in range(left, right + 1):
            reach = max(reach, i + nums[i])

        left = right + 1
        right = reach
        res += 1

    return res


if __name__ == "__main__":
    assert jump([2, 3, 1, 1, 4]) == 2
    assert jump([2, 3, 0, 1, 4]) == 2

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

## 763. Partition Labels

-   [LeetCode](https://leetcode.com/problems/partition-labels/) | [LeetCode CH](https://leetcode.cn/problems/partition-labels/) (Medium)

-   Tags: hash table, two pointers, string, greedy
```python title="763. Partition Labels - Python Solution"
from typing import List


# 1. Hashmap
def partitionLabels1(s: str) -> List[int]:
    hashmap = {}

    for i, j in enumerate(s):
        if j not in hashmap:
            hashmap[j] = [i, i]
        else:
            hashmap[j][1] = i

    intervals = list(hashmap.values())
    intervals.sort(key=lambda x: x[0])

    if len(intervals) < 2:
        return len(intervals)

    res = []
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            intervals[i][1] = max(intervals[i][1], intervals[i - 1][1])
        else:
            res.append(intervals[i][0])

    res.append(intervals[-1][1] + 1)

    if len(res) == 1:
        return res
    else:
        for i in range(len(res) - 1, 0, -1):
            res[i] -= res[i - 1]
        return res


# Single Pass Partitioning
def partitionLabels2(s: str) -> List[int]:
    last = {c: i for i, c in enumerate(s)}
    res = []
    start, end = 0, 0

    for i, c in enumerate(s):
        end = max(end, last[c])
        if end == i:
            res.append(end - start + 1)
            start = i + 1

    return res


print(partitionLabels1("abaccd"))  # [3, 2, 1]
print(partitionLabels2("abaccd"))  # [3, 2, 1]

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

