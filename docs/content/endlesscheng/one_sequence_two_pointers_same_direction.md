---
comments: True
---

# One Sequence Two Pointers Same Direction

## Table of Contents

- [ ] [1574. Shortest Subarray to be Removed to Make Array Sorted](https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/) (Medium)
- [ ] [2972. Count the Number of Incremovable Subarrays II](https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-ii/) (Hard)
- [ ] [2122. Recover the Original Array](https://leetcode.cn/problems/recover-the-original-array/) (Hard)
- [x] [2234. Maximum Total Beauty of the Gardens](https://leetcode.cn/problems/maximum-total-beauty-of-the-gardens/) (Hard)
- [ ] [3323. Minimize Connected Groups by Inserting Interval](https://leetcode.cn/problems/minimize-connected-groups-by-inserting-interval/) (Medium) 👑
- [ ] [581. Shortest Unsorted Continuous Subarray](https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/) (Medium)

## 1574. Shortest Subarray to be Removed to Make Array Sorted

-   [LeetCode](https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/) | [LeetCode CH](https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/) (Medium)

-   Tags: array, two pointers, binary search, stack, monotonic stack
## 2972. Count the Number of Incremovable Subarrays II

-   [LeetCode](https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/) | [LeetCode CH](https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-ii/) (Hard)

-   Tags: array, two pointers, binary search
## 2122. Recover the Original Array

-   [LeetCode](https://leetcode.com/problems/recover-the-original-array/) | [LeetCode CH](https://leetcode.cn/problems/recover-the-original-array/) (Hard)

-   Tags: array, hash table, two pointers, sorting, enumeration
## 2234. Maximum Total Beauty of the Gardens

-   [LeetCode](https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/) | [LeetCode CH](https://leetcode.cn/problems/maximum-total-beauty-of-the-gardens/) (Hard)

-   Tags: array, two pointers, binary search, greedy, sorting
```cpp title="2234. Maximum Total Beauty of the Gardens - C++ Solution"
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

long long maximumBeauty(vector<int>& flowers, long long newFlowers, int target,
                        int full, int partial) {
    int n = flowers.size();

    long long left = newFlowers - 1LL * target * n;
    for (int& flower : flowers) {
        flower = min(flower, target);
        left += flower;
    }

    if (left == newFlowers) return 1LL * full * n;

    if (left >= 0) {
        return max(1LL * (target - 1) * partial + 1LL * (n - 1) * full,
                   1LL * n * full);
    }

    sort(flowers.begin(), flowers.end());
    long long res = 0, pre_sum = 0;

    int j = 0;
    for (int i = 1; i <= n; i++) {
        left += target - flowers[i - 1];
        if (left < 0) {
            continue;
        }

        while (j < i && 1LL * flowers[j] * j <= pre_sum + left) {
            pre_sum += flowers[j];
            j++;
        }

        long long avg = (left + pre_sum) / j;
        long long total_beauty = avg * partial + 1LL * (n - i) * full;
        res = max(res, total_beauty);
    }

    return res;
}

int main() {
    vector<int> flowers = {1, 3, 1, 1};
    long long newFlowers = 7;
    int target = 6;
    int full = 12;
    int partial = 1;
    long long res = maximumBeauty(flowers, newFlowers, target, full, partial);
    cout << res << endl;  // 14
    return 0;
}

```

## 3323. Minimize Connected Groups by Inserting Interval

-   [LeetCode](https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/) | [LeetCode CH](https://leetcode.cn/problems/minimize-connected-groups-by-inserting-interval/) (Medium)

-   Tags: array, binary search, sliding window, sorting
## 581. Shortest Unsorted Continuous Subarray

-   [LeetCode](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) | [LeetCode CH](https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/) (Medium)

-   Tags: array, two pointers, stack, greedy, sorting, monotonic stack
