---
comments: True
---

# Offline Algorithm

- [ ] [2343. Query Kth Smallest Trimmed Number](https://leetcode.cn/problems/query-kth-smallest-trimmed-number/) (Medium)
- [x] [2070. Most Beautiful Item for Each Query](https://leetcode.cn/problems/most-beautiful-item-for-each-query/) (Medium)
- [ ] [1847. Closest Room](https://leetcode.cn/problems/closest-room/) (Hard)
- [ ] [2503. Maximum Number of Points From Grid Queries](https://leetcode.cn/problems/maximum-number-of-points-from-grid-queries/) (Hard)
- [ ] [1851. Minimum Interval to Include Each Query](https://leetcode.cn/problems/minimum-interval-to-include-each-query/) (Hard)
- [ ] [1697. Checking Existence of Edge Length Limited Paths](https://leetcode.cn/problems/checking-existence-of-edge-length-limited-paths/) (Hard)
- [ ] [2940. Find Building Where Alice and Bob Can Meet](https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/) (Hard)
- [ ] [2747. Count Zero Request Servers](https://leetcode.cn/problems/count-zero-request-servers/) (Medium)
- [ ] [1938. Maximum Genetic Difference Query](https://leetcode.cn/problems/maximum-genetic-difference-query/) (Hard)
- [ ] [2736. Maximum Sum Queries](https://leetcode.cn/problems/maximum-sum-queries/) (Hard)
- [ ] [3382. Maximum Area Rectangle With Point Constraints II](https://leetcode.cn/problems/maximum-area-rectangle-with-point-constraints-ii/) (Hard)

## 2343. Query Kth Smallest Trimmed Number

-   [LeetCode](https://leetcode.com/problems/query-kth-smallest-trimmed-number/) | [LeetCode CH](https://leetcode.cn/problems/query-kth-smallest-trimmed-number/) (Medium)

-   Tags: array, string, divide and conquer, sorting, heap priority queue, radix sort, quickselect

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

## 1847. Closest Room

-   [LeetCode](https://leetcode.com/problems/closest-room/) | [LeetCode CH](https://leetcode.cn/problems/closest-room/) (Hard)

-   Tags: array, binary search, sorting, ordered set

## 2503. Maximum Number of Points From Grid Queries

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-points-from-grid-queries/) (Hard)

-   Tags: array, two pointers, breadth first search, union find, sorting, heap priority queue, matrix

## 1851. Minimum Interval to Include Each Query

-   [LeetCode](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | [LeetCode CH](https://leetcode.cn/problems/minimum-interval-to-include-each-query/) (Hard)

-   Tags: array, binary search, line sweep, sorting, heap priority queue

## 1697. Checking Existence of Edge Length Limited Paths

-   [LeetCode](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/) | [LeetCode CH](https://leetcode.cn/problems/checking-existence-of-edge-length-limited-paths/) (Hard)

-   Tags: array, two pointers, union find, graph, sorting

## 2940. Find Building Where Alice and Bob Can Meet

-   [LeetCode](https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/) | [LeetCode CH](https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/) (Hard)

-   Tags: array, binary search, stack, binary indexed tree, segment tree, heap priority queue, monotonic stack

## 2747. Count Zero Request Servers

-   [LeetCode](https://leetcode.com/problems/count-zero-request-servers/) | [LeetCode CH](https://leetcode.cn/problems/count-zero-request-servers/) (Medium)

-   Tags: array, hash table, sliding window, sorting

## 1938. Maximum Genetic Difference Query

-   [LeetCode](https://leetcode.com/problems/maximum-genetic-difference-query/) | [LeetCode CH](https://leetcode.cn/problems/maximum-genetic-difference-query/) (Hard)

-   Tags: array, hash table, bit manipulation, depth first search, trie

## 2736. Maximum Sum Queries

-   [LeetCode](https://leetcode.com/problems/maximum-sum-queries/) | [LeetCode CH](https://leetcode.cn/problems/maximum-sum-queries/) (Hard)

-   Tags: array, binary search, stack, binary indexed tree, segment tree, sorting, monotonic stack

## 3382. Maximum Area Rectangle With Point Constraints II

-   [LeetCode](https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/) | [LeetCode CH](https://leetcode.cn/problems/maximum-area-rectangle-with-point-constraints-ii/) (Hard)

-   Tags: array, math, binary indexed tree, segment tree, geometry, sorting
