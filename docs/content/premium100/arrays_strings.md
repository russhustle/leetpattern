---
comments: True
---

# Arrays Strings

- [x] [624. Maximum Distance in Arrays](https://leetcode.cn/problems/maximum-distance-in-arrays/) (Medium)
- [x] [280. Wiggle Sort](https://leetcode.cn/problems/wiggle-sort/) (Medium) 👑
- [ ] [1056. Confusing Number](https://leetcode.cn/problems/confusing-number/) (Easy) 👑
- [ ] [1427. Perform String Shifts](https://leetcode.cn/problems/perform-string-shifts/) (Easy) 👑
- [ ] [161. One Edit Distance](https://leetcode.cn/problems/one-edit-distance/) (Medium) 👑
- [ ] [186. Reverse Words in a String II](https://leetcode.cn/problems/reverse-words-in-a-string-ii/) (Medium) 👑
- [ ] [1055. Shortest Way to Form String](https://leetcode.cn/problems/shortest-way-to-form-string/) (Medium) 👑

## 624. Maximum Distance in Arrays

-   [LeetCode](https://leetcode.com/problems/maximum-distance-in-arrays/) | [LeetCode CH](https://leetcode.cn/problems/maximum-distance-in-arrays/) (Medium)

-   Tags: array, greedy

```python title="624. Maximum Distance in Arrays - Python Solution"
from typing import List


# Array
def maxDistance(arrays: List[List[int]]) -> int:
    mn, mx = float("inf"), float("-inf")
    res = 0

    for arr in arrays:
        res = max(res, arr[-1] - mn, mx - arr[0])
        mn = min(mn, arr[0])
        mx = max(mx, arr[-1])

    return res


arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
print(maxDistance(arrays))  # 4

```

## 280. Wiggle Sort

-   [LeetCode](https://leetcode.com/problems/wiggle-sort/) | [LeetCode CH](https://leetcode.cn/problems/wiggle-sort/) (Medium)

-   Tags: array, greedy, sorting

```cpp title="280. Wiggle Sort - C++ Solution"
#include <iostream>
#include <vector>
using namespace std;

void wiggleSort(vector<int>& nums) {
    int n = nums.size();

    for (int i = 0; i < n - 1; i++) {
        if (i % 2 == 0) {
            if (nums[i] > nums[i + 1]) swap(nums[i], nums[i + 1]);
        } else {
            if (nums[i] < nums[i + 1]) swap(nums[i], nums[i + 1]);
        }
    }
}

int main() {
    vector<int> nums = {3, 5, 2, 1, 6, 4};
    wiggleSort(nums);
    // 3 5 1 6 2 4
    for (size_t i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}

```

## 1056. Confusing Number

-   [LeetCode](https://leetcode.com/problems/confusing-number/) | [LeetCode CH](https://leetcode.cn/problems/confusing-number/) (Easy)

-   Tags: math

## 1427. Perform String Shifts

-   [LeetCode](https://leetcode.com/problems/perform-string-shifts/) | [LeetCode CH](https://leetcode.cn/problems/perform-string-shifts/) (Easy)

-   Tags: array, math, string

## 161. One Edit Distance

-   [LeetCode](https://leetcode.com/problems/one-edit-distance/) | [LeetCode CH](https://leetcode.cn/problems/one-edit-distance/) (Medium)

-   Tags: two pointers, string

## 186. Reverse Words in a String II

-   [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string-ii/) | [LeetCode CH](https://leetcode.cn/problems/reverse-words-in-a-string-ii/) (Medium)

-   Tags: two pointers, string

## 1055. Shortest Way to Form String

-   [LeetCode](https://leetcode.com/problems/shortest-way-to-form-string/) | [LeetCode CH](https://leetcode.cn/problems/shortest-way-to-form-string/) (Medium)

-   Tags: two pointers, string, binary search, greedy
