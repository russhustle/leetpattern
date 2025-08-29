---
comments: True
---

# Bit AND OR

## Table of Contents

- [ ] [2980. Check if Bitwise OR Has Trailing Zeros](https://leetcode.cn/problems/check-if-bitwise-or-has-trailing-zeros/) (Easy)
- [ ] [1318. Minimum Flips to Make a OR b Equal to c](https://leetcode.cn/problems/minimum-flips-to-make-a-or-b-equal-to-c/) (Medium)
- [ ] [2419. Longest Subarray With Maximum Bitwise AND](https://leetcode.cn/problems/longest-subarray-with-maximum-bitwise-and/) (Medium)
- [ ] [2871. Split Array Into Maximum Number of Subarrays](https://leetcode.cn/problems/split-array-into-maximum-number-of-subarrays/) (Medium)
- [ ] [2401. Longest Nice Subarray](https://leetcode.cn/problems/longest-nice-subarray/) (Medium)
- [x] [2680. Maximum OR](https://leetcode.cn/problems/maximum-or/) (Medium)
- [ ] [3133. Minimum Array End](https://leetcode.cn/problems/minimum-array-end/) (Medium)
- [ ] [3108. Minimum Cost Walk in Weighted Graph](https://leetcode.cn/problems/minimum-cost-walk-in-weighted-graph/) (Hard)
- [ ] [3117. Minimum Sum of Values by Dividing Array](https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/) (Hard)
- [ ] [3125. Maximum Number That Makes Result of Bitwise AND Zero](https://leetcode.cn/problems/maximum-number-that-makes-result-of-bitwise-and-zero/) (Medium) 👑

## 2980. Check if Bitwise OR Has Trailing Zeros

-   [LeetCode](https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/) | [LeetCode CH](https://leetcode.cn/problems/check-if-bitwise-or-has-trailing-zeros/) (Easy)

-   Tags: array, bit manipulation
## 1318. Minimum Flips to Make a OR b Equal to c

-   [LeetCode](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/) | [LeetCode CH](https://leetcode.cn/problems/minimum-flips-to-make-a-or-b-equal-to-c/) (Medium)

-   Tags: bit manipulation
## 2419. Longest Subarray With Maximum Bitwise AND

-   [LeetCode](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/) | [LeetCode CH](https://leetcode.cn/problems/longest-subarray-with-maximum-bitwise-and/) (Medium)

-   Tags: array, bit manipulation, brainteaser
## 2871. Split Array Into Maximum Number of Subarrays

-   [LeetCode](https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/split-array-into-maximum-number-of-subarrays/) (Medium)

-   Tags: array, greedy, bit manipulation
## 2401. Longest Nice Subarray

-   [LeetCode](https://leetcode.com/problems/longest-nice-subarray/) | [LeetCode CH](https://leetcode.cn/problems/longest-nice-subarray/) (Medium)

-   Tags: array, bit manipulation, sliding window
## 2680. Maximum OR

-   [LeetCode](https://leetcode.com/problems/maximum-or/) | [LeetCode CH](https://leetcode.cn/problems/maximum-or/) (Medium)

-   Tags: array, greedy, bit manipulation, prefix sum
```python title="2680. Maximum OR - Python Solution"
from typing import List


# Greedy
def maximumOr(nums: List[int], k: int) -> int:
    """Maximum OR of Array After k Operations

    Args:
        nums (List[int]): provided list of integers
        k (int): number of operations

    Returns:
        int: maximum OR of array after k operations
    """
    n = len(nums)
    suffix = [0 for _ in range(n)]

    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] | nums[i + 1]

    res, pre = 0, 0
    for num, suf in zip(nums, suffix):
        res = max(res, pre | (num << k) | suf)
        pre |= num

    return res


if __name__ == "__main__":
    print(maximumOr(nums=[8, 1, 2], k=2))  # 35

```

## 3133. Minimum Array End

-   [LeetCode](https://leetcode.com/problems/minimum-array-end/) | [LeetCode CH](https://leetcode.cn/problems/minimum-array-end/) (Medium)

-   Tags: bit manipulation
## 3108. Minimum Cost Walk in Weighted Graph

-   [LeetCode](https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-walk-in-weighted-graph/) (Hard)

-   Tags: array, bit manipulation, union find, graph
## 3117. Minimum Sum of Values by Dividing Array

-   [LeetCode](https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/) | [LeetCode CH](https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/) (Hard)

-   Tags: array, binary search, dynamic programming, bit manipulation, segment tree, queue
## 3125. Maximum Number That Makes Result of Bitwise AND Zero

-   [LeetCode](https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-that-makes-result-of-bitwise-and-zero/) (Medium)

-   Tags: string, greedy, sorting
