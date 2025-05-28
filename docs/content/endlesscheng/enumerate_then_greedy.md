---
comments: True
---

# Enumerate then Greedy

## Table of Contents

- [ ] [2171. Removing Minimum Number of Magic Beans](https://leetcode.cn/problems/removing-minimum-number-of-magic-beans/) (Medium)
- [ ] [3085. Minimum Deletions to Make String K-Special](https://leetcode.cn/problems/minimum-deletions-to-make-string-k-special/) (Medium)
- [ ] [1727. Largest Submatrix With Rearrangements](https://leetcode.cn/problems/largest-submatrix-with-rearrangements/) (Medium)
- [ ] [2749. Minimum Operations to Make the Integer Zero](https://leetcode.cn/problems/minimum-operations-to-make-the-integer-zero/) (Medium)
- [ ] [2910. Minimum Number of Groups to Create a Valid Assignment](https://leetcode.cn/problems/minimum-number-of-groups-to-create-a-valid-assignment/) (Medium)
- [x] [2234. Maximum Total Beauty of the Gardens](https://leetcode.cn/problems/maximum-total-beauty-of-the-gardens/) (Hard)

## 2171. Removing Minimum Number of Magic Beans

-   [LeetCode](https://leetcode.com/problems/removing-minimum-number-of-magic-beans/) | [LeetCode CH](https://leetcode.cn/problems/removing-minimum-number-of-magic-beans/) (Medium)

-   Tags: array, greedy, sorting, enumeration, prefix sum
## 3085. Minimum Deletions to Make String K-Special

-   [LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/) | [LeetCode CH](https://leetcode.cn/problems/minimum-deletions-to-make-string-k-special/) (Medium)

-   Tags: hash table, string, greedy, sorting, counting
## 1727. Largest Submatrix With Rearrangements

-   [LeetCode](https://leetcode.com/problems/largest-submatrix-with-rearrangements/) | [LeetCode CH](https://leetcode.cn/problems/largest-submatrix-with-rearrangements/) (Medium)

-   Tags: array, greedy, sorting, matrix
## 2749. Minimum Operations to Make the Integer Zero

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-make-the-integer-zero/) (Medium)

-   Tags: bit manipulation, brainteaser, enumeration
## 2910. Minimum Number of Groups to Create a Valid Assignment

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-groups-to-create-a-valid-assignment/) (Medium)

-   Tags: array, hash table, greedy
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
