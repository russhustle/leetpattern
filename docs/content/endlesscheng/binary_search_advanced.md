---
comments: True
---

# Binary Search Advanced

- [x] [2300. Successful Pairs of Spells and Potions](https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/) (Medium)
- [x] [1385. Find the Distance Value Between Two Arrays](https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/) (Easy)
- [ ] [2389. Longest Subsequence With Limited Sum](https://leetcode.cn/problems/longest-subsequence-with-limited-sum/) (Easy)
- [ ] [1170. Compare Strings by Frequency of the Smallest Character](https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/) (Medium)
- [x] [2080. Range Frequency Queries](https://leetcode.cn/problems/range-frequency-queries/) (Medium)
- [ ] [2563. Count the Number of Fair Pairs](https://leetcode.cn/problems/count-the-number-of-fair-pairs/) (Medium)
- [x] [2070. Most Beautiful Item for Each Query](https://leetcode.cn/problems/most-beautiful-item-for-each-query/) (Medium)
- [x] [981. Time Based Key-Value Store](https://leetcode.cn/problems/time-based-key-value-store/) (Medium)
- [ ] [1146. Snapshot Array](https://leetcode.cn/problems/snapshot-array/) (Medium)
- [ ] [658. Find K Closest Elements](https://leetcode.cn/problems/find-k-closest-elements/) (Medium)
- [ ] [1818. Minimum Absolute Sum Difference](https://leetcode.cn/problems/minimum-absolute-sum-difference/) (Medium)
- [ ] [911. Online Election](https://leetcode.cn/problems/online-election/) (Medium)
- [ ] [1182. Shortest Distance to Target Color](https://leetcode.cn/problems/shortest-distance-to-target-color/) (Medium) 👑
- [ ] [2819. Minimum Relative Loss After Buying Chocolates](https://leetcode.cn/problems/minimum-relative-loss-after-buying-chocolates/) (Hard) 👑
- [x] [1287. Element Appearing More Than 25% In Sorted Array](https://leetcode.cn/problems/element-appearing-more-than-25-in-sorted-array/) (Easy)
- [ ] [1150. Check If a Number Is Majority Element in a Sorted Array](https://leetcode.cn/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) (Easy) 👑

## 2300. Successful Pairs of Spells and Potions

-   [LeetCode](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/) | [LeetCode CH](https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/) (Medium)

-   Tags: array, two pointers, binary search, sorting

```python title="2300. Successful Pairs of Spells and Potions - Python Solution"
import bisect
from typing import List


# Binary Search
def successfulPairs(
    spells: List[int], potions: List[int], success: int
) -> List[int]:
    potions.sort()
    res = []
    n = len(potions)

    for spell in spells:
        target = (success + spell - 1) // spell
        index = bisect.bisect_left(potions, target)
        res.append(n - index)

    return res


spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(successfulPairs(spells, potions, success))  # [4, 0, 3]

```

## 1385. Find the Distance Value Between Two Arrays

-   [LeetCode](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/) | [LeetCode CH](https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/) (Easy)

-   Tags: array, two pointers, binary search, sorting

```python title="1385. Find the Distance Value Between Two Arrays - Python Solution"
from bisect import bisect_left
from typing import List


# Binary Search
def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
    arr2.sort()
    res = 0

    for x in arr1:
        i = bisect_left(arr2, x - d)
        if i == len(arr2) or arr2[i] > x + d:
            res += 1

    return res


arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
print(findTheDistanceValue(arr1, arr2, d))  # 2

```

## 2389. Longest Subsequence With Limited Sum

-   [LeetCode](https://leetcode.com/problems/longest-subsequence-with-limited-sum/) | [LeetCode CH](https://leetcode.cn/problems/longest-subsequence-with-limited-sum/) (Easy)

-   Tags: array, binary search, greedy, sorting, prefix sum

## 1170. Compare Strings by Frequency of the Smallest Character

-   [LeetCode](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/) | [LeetCode CH](https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/) (Medium)

-   Tags: array, hash table, string, binary search, sorting

## 2080. Range Frequency Queries

-   [LeetCode](https://leetcode.com/problems/range-frequency-queries/) | [LeetCode CH](https://leetcode.cn/problems/range-frequency-queries/) (Medium)

-   Tags: array, hash table, binary search, design, segment tree

```python title="2080. Range Frequency Queries - Python Solution"
from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


# Binary Search
class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.freq = defaultdict(list)
        for idx, val in enumerate(arr):
            self.freq[val].append(idx)

    def query(self, left: int, right: int, value: int) -> int:
        idxs = self.freq[value]
        return bisect_right(idxs, right) - bisect_left(idxs, left)


arr = [1, 3, 1, 2, 4, 1, 3, 2, 1]
rfq = RangeFreqQuery(arr)
print(rfq.query(0, 4, 1))  # 2
print(rfq.query(2, 8, 1))  # 3
print(rfq.query(0, 8, 3))  # 2
print(rfq.query(4, 7, 2))  # 1

```

## 2563. Count the Number of Fair Pairs

-   [LeetCode](https://leetcode.com/problems/count-the-number-of-fair-pairs/) | [LeetCode CH](https://leetcode.cn/problems/count-the-number-of-fair-pairs/) (Medium)

-   Tags: array, two pointers, binary search, sorting

## 2070. Most Beautiful Item for Each Query

-   [LeetCode](https://leetcode.com/problems/most-beautiful-item-for-each-query/) | [LeetCode CH](https://leetcode.cn/problems/most-beautiful-item-for-each-query/) (Medium)

-   Tags: array, binary search, sorting

```cpp title="2070. Most Beautiful Item for Each Query - C++ Solution"
#include <algorithm>
#include <iostream>
#include <numeric>
#include <ranges>
#include <vector>
using namespace std;

vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
    ranges::sort(items, {}, [](auto& item) { return item[0]; });
    vector<int> idx(queries.size());
    iota(idx.begin(), idx.end(), 0);
    ranges::sort(idx, {}, [&](int i) { return queries[i]; });

    vector<int> res(queries.size());
    int max_beauty = 0, j = 0;
    for (int i : idx) {
        int q = queries[i];
        while (j < items.size() && items[j][0] <= q) {
            max_beauty = max(max_beauty, items[j][1]);
            j++;
        }
        res[i] = max_beauty;
    }
    return res;
}

int main() {
    vector<vector<int>> items = {{1, 2}, {2, 4}, {3, 2}, {5, 6}, {3, 5}};
    vector<int> queries = {1, 2, 3, 4, 5, 6};
    vector<int> res = maximumBeauty(items, queries);
    // 2 4 5 5 6 6
    for (int i : res) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}

```

## 981. Time Based Key-Value Store

-   [LeetCode](https://leetcode.com/problems/time-based-key-value-store/) | [LeetCode CH](https://leetcode.cn/problems/time-based-key-value-store/) (Medium)

-   Tags: hash table, string, binary search, design

```python title="981. Time Based Key-Value Store - Python Solution"
from collections import defaultdict


# Binary Search
class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)
        self.times = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append(timestamp)
        self.times[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        tmp = self.keys[key]

        left, right = 0, len(tmp) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if tmp[mid] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        return self.times[tmp[right]] if right >= 0 else ""


obj = TimeMap()
obj.set("foo", "bar", 1)
print(obj.get("foo", 1))  # bar
print(obj.get("foo", 3))  # bar
obj.set("foo", "bar2", 4)
print(obj.get("foo", 4))  # bar2
print(obj.get("foo", 5))  # bar2

```

## 1146. Snapshot Array

-   [LeetCode](https://leetcode.com/problems/snapshot-array/) | [LeetCode CH](https://leetcode.cn/problems/snapshot-array/) (Medium)

-   Tags: array, hash table, binary search, design

## 658. Find K Closest Elements

-   [LeetCode](https://leetcode.com/problems/find-k-closest-elements/) | [LeetCode CH](https://leetcode.cn/problems/find-k-closest-elements/) (Medium)

-   Tags: array, two pointers, binary search, sliding window, sorting, heap priority queue

## 1818. Minimum Absolute Sum Difference

-   [LeetCode](https://leetcode.com/problems/minimum-absolute-sum-difference/) | [LeetCode CH](https://leetcode.cn/problems/minimum-absolute-sum-difference/) (Medium)

-   Tags: array, binary search, sorting, ordered set

## 911. Online Election

-   [LeetCode](https://leetcode.com/problems/online-election/) | [LeetCode CH](https://leetcode.cn/problems/online-election/) (Medium)

-   Tags: array, hash table, binary search, design

## 1182. Shortest Distance to Target Color

-   [LeetCode](https://leetcode.com/problems/shortest-distance-to-target-color/) | [LeetCode CH](https://leetcode.cn/problems/shortest-distance-to-target-color/) (Medium)

-   Tags: array, binary search, dynamic programming

## 2819. Minimum Relative Loss After Buying Chocolates

-   [LeetCode](https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/) | [LeetCode CH](https://leetcode.cn/problems/minimum-relative-loss-after-buying-chocolates/) (Hard)

-   Tags: array, binary search, sorting, prefix sum

## 1287. Element Appearing More Than 25% In Sorted Array

-   [LeetCode](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/element-appearing-more-than-25-in-sorted-array/) (Easy)

-   Tags: array

```python title="1287. Element Appearing More Than 25% In Sorted Array - Python Solution"
from bisect import bisect_left, bisect_right
from typing import List


# Binary Search
def findSpecialInteger(arr: List[int]) -> int:
    n = len(arr)
    span = n // 4 + 1

    for i in range(0, n, span):
        left = bisect_left(arr, arr[i])
        right = bisect_right(arr, arr[i])
        if right - left >= span:
            return arr[i]

    return -1

```

## 1150. Check If a Number Is Majority Element in a Sorted Array

-   [LeetCode](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) (Easy)

-   Tags: array, binary search
