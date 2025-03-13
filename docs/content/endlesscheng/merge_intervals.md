---
comments: True
---

# Merge Intervals

- [x] [56. Merge Intervals](https://leetcode.cn/problems/merge-intervals/) (Medium)
- [x] [57. Insert Interval](https://leetcode.cn/problems/insert-interval/) (Medium)
- [x] [55. Jump Game](https://leetcode.cn/problems/jump-game/) (Medium)
- [x] [763. Partition Labels](https://leetcode.cn/problems/partition-labels/) (Medium)
- [ ] [3169. Count Days Without Meetings](https://leetcode.cn/problems/count-days-without-meetings/) (Medium)
- [ ] [2580. Count Ways to Group Overlapping Ranges](https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/) (Medium)
- [ ] [3394. Check if Grid can be Cut into Sections](https://leetcode.cn/problems/check-if-grid-can-be-cut-into-sections/) (Medium)
- [ ] [2963. Count the Number of Good Partitions](https://leetcode.cn/problems/count-the-number-of-good-partitions/) (Hard)
- [ ] [2584. Split the Array to Make Coprime Products](https://leetcode.cn/problems/split-the-array-to-make-coprime-products/) (Hard)
- [ ] [616. Add Bold Tag in String](https://leetcode.cn/problems/add-bold-tag-in-string/) (Medium) 👑
- [ ] [758. Bold Words in String](https://leetcode.cn/problems/bold-words-in-string/) (Medium) 👑
- [ ] [3323. Minimize Connected Groups by Inserting Interval](https://leetcode.cn/problems/minimize-connected-groups-by-inserting-interval/) (Medium) 👑
- [ ] [759. Employee Free Time](https://leetcode.cn/problems/employee-free-time/) (Hard) 👑
- [ ] [2655. Find Maximal Uncovered Ranges](https://leetcode.cn/problems/find-maximal-uncovered-ranges/) (Medium) 👑

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

## 55. Jump Game

-   [LeetCode](https://leetcode.com/problems/jump-game/) | [LeetCode CH](https://leetcode.cn/problems/jump-game/) (Medium)

-   Tags: array, dynamic programming, greedy
-   Return `True` if you can reach the last index, otherwise `False`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Yan0cv2cLy8?si=musT5NViPicljg7x" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

-   Example: `[2, 3, 1, 1, 4, 1, 2, 0, 0]`

| Index | Value | Index + Value | Max Reach | Max Reach >= Last Index |
| :---: | :---: | :-----------: | :-------: | :---------------------: |
|   0   |   2   |       2       |     2     |          False          |
|   1   |   3   |       4       |     4     |          False          |
|   2   |   1   |       3       |     4     |          False          |
|   3   |   1   |       4       |     4     |          False          |
|   4   |   4   |       8       |     8     |          True           |
|   5   |   1   |       6       |     8     |          True           |
|   6   |   2   |       8       |     8     |          True           |
|   7   |   0   |       7       |     8     |          True           |
|   8   |   0   |       8       |     8     |          True           |

```python title="55. Jump Game - Python Solution"
from typing import List


# Greedy - Interval
def canJump(nums: List[int]) -> bool:
    maxReach = 0
    i = 0
    n = len(nums)

    while i <= maxReach:
        maxReach = max(maxReach, i + nums[i])
        if maxReach >= n - 1:
            return True
        i += 1

    return False


print(canJump([2, 3, 1, 1, 4, 1, 2, 0, 0]))  # True

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

## 763. Partition Labels

-   [LeetCode](https://leetcode.com/problems/partition-labels/) | [LeetCode CH](https://leetcode.cn/problems/partition-labels/) (Medium)

-   Tags: hash table, two pointers, string, greedy

```python title="763. Partition Labels - Python Solution"
from typing import List


# 1. Hashmap
def partitionLabels1(s: str) -> List[int]:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
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

    result = []
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            intervals[i][1] = max(intervals[i][1], intervals[i - 1][1])
        else:
            result.append(intervals[i][0])

    result.append(intervals[-1][1] + 1)

    if len(result) == 1:
        return result
    else:
        for i in range(len(result) - 1, 0, -1):
            result[i] -= result[i - 1]
        return result


# 2. Single Pass Partitioning
def partitionLabels2(s: str) -> List[int]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    last = {c: i for i, c in enumerate(s)}

    start, end = 0, 0
    result = []

    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result


print(partitionLabels1("abaccd"))  # [3, 2, 1]
print(partitionLabels2("abaccd"))  # [3, 2, 1]

```

## 3169. Count Days Without Meetings

-   [LeetCode](https://leetcode.com/problems/count-days-without-meetings/) | [LeetCode CH](https://leetcode.cn/problems/count-days-without-meetings/) (Medium)

-   Tags: array, sorting

## 2580. Count Ways to Group Overlapping Ranges

-   [LeetCode](https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/) | [LeetCode CH](https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/) (Medium)

-   Tags: array, sorting

## 3394. Check if Grid can be Cut into Sections

-   [LeetCode](https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/) | [LeetCode CH](https://leetcode.cn/problems/check-if-grid-can-be-cut-into-sections/) (Medium)

-   Tags: array, sorting

## 2963. Count the Number of Good Partitions

-   [LeetCode](https://leetcode.com/problems/count-the-number-of-good-partitions/) | [LeetCode CH](https://leetcode.cn/problems/count-the-number-of-good-partitions/) (Hard)

-   Tags: array, hash table, math, combinatorics

## 2584. Split the Array to Make Coprime Products

-   [LeetCode](https://leetcode.com/problems/split-the-array-to-make-coprime-products/) | [LeetCode CH](https://leetcode.cn/problems/split-the-array-to-make-coprime-products/) (Hard)

-   Tags: array, hash table, math, number theory

## 616. Add Bold Tag in String

-   [LeetCode](https://leetcode.com/problems/add-bold-tag-in-string/) | [LeetCode CH](https://leetcode.cn/problems/add-bold-tag-in-string/) (Medium)

-   Tags: array, hash table, string, trie, string matching

## 758. Bold Words in String

-   [LeetCode](https://leetcode.com/problems/bold-words-in-string/) | [LeetCode CH](https://leetcode.cn/problems/bold-words-in-string/) (Medium)

-   Tags: array, hash table, string, trie, string matching

## 3323. Minimize Connected Groups by Inserting Interval

-   [LeetCode](https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/) | [LeetCode CH](https://leetcode.cn/problems/minimize-connected-groups-by-inserting-interval/) (Medium)

-   Tags: array, binary search, sliding window, sorting

## 759. Employee Free Time

-   [LeetCode](https://leetcode.com/problems/employee-free-time/) | [LeetCode CH](https://leetcode.cn/problems/employee-free-time/) (Hard)

-   Tags: array, sorting, heap priority queue

## 2655. Find Maximal Uncovered Ranges

-   [LeetCode](https://leetcode.com/problems/find-maximal-uncovered-ranges/) | [LeetCode CH](https://leetcode.cn/problems/find-maximal-uncovered-ranges/) (Medium)

-   Tags: array, sorting
