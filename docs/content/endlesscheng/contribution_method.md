---
comments: True
---

# Contribution Method

## Table of Contents

- [ ] [907. Sum of Subarray Minimums](https://leetcode.cn/problems/sum-of-subarray-minimums/) (Medium)
- [ ] [2104. Sum of Subarray Ranges](https://leetcode.cn/problems/sum-of-subarray-ranges/) (Medium)
- [ ] [1856. Maximum Subarray Min-Product](https://leetcode.cn/problems/maximum-subarray-min-product/) (Medium)
- [ ] [2818. Apply Operations to Maximize Score](https://leetcode.cn/problems/apply-operations-to-maximize-score/) (Hard)
- [x] [2281. Sum of Total Strength of Wizards](https://leetcode.cn/problems/sum-of-total-strength-of-wizards/) (Hard)
- [ ] [3359. Find Sorted Submatrices With Maximum Element at Most K](https://leetcode.cn/problems/find-sorted-submatrices-with-maximum-element-at-most-k/) (Hard) 👑
- [ ] [2334. Subarray With Elements Greater Than Varying Threshold](https://leetcode.cn/problems/subarray-with-elements-greater-than-varying-threshold/) (Hard)

## 907. Sum of Subarray Minimums

-   [LeetCode](https://leetcode.com/problems/sum-of-subarray-minimums/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-subarray-minimums/) (Medium)

-   Tags: array, dynamic programming, stack, monotonic stack

## 2104. Sum of Subarray Ranges

-   [LeetCode](https://leetcode.com/problems/sum-of-subarray-ranges/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-subarray-ranges/) (Medium)

-   Tags: array, stack, monotonic stack

## 1856. Maximum Subarray Min-Product

-   [LeetCode](https://leetcode.com/problems/maximum-subarray-min-product/) | [LeetCode CH](https://leetcode.cn/problems/maximum-subarray-min-product/) (Medium)

-   Tags: array, stack, monotonic stack, prefix sum

## 2818. Apply Operations to Maximize Score

-   [LeetCode](https://leetcode.com/problems/apply-operations-to-maximize-score/) | [LeetCode CH](https://leetcode.cn/problems/apply-operations-to-maximize-score/) (Hard)

-   Tags: array, math, stack, greedy, sorting, monotonic stack, number theory

## 2281. Sum of Total Strength of Wizards

-   [LeetCode](https://leetcode.com/problems/sum-of-total-strength-of-wizards/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-total-strength-of-wizards/) (Hard)

-   Tags: array, stack, monotonic stack, prefix sum

```python title="2281. Sum of Total Strength of Wizards - Python Solution"
from itertools import accumulate
from typing import List


# Monotonic Stack
def totalStrength(strength: List[int]) -> int:
    n = len(strength)
    left = [-1 for _ in range(n)]
    right = [n for _ in range(n)]
    stack = []

    for i, v in enumerate(strength):
        while stack and strength[stack[-1]] >= v:
            right[stack.pop()] = i
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    prefix_sum = list(accumulate(accumulate(strength, initial=0), initial=0))

    ans = 0
    for i, v in enumerate(strength):
        l, r = left[i] + 1, right[i] - 1
        tot = (i - l + 1) * (prefix_sum[r + 2] - prefix_sum[i + 1]) - (
            r - i + 1
        ) * (prefix_sum[i + 1] - prefix_sum[l])
        ans += v * tot

    return ans % (10**9 + 7)


strength = [1, 3, 1, 2]
print(totalStrength(strength))  # 44

```

## 3359. Find Sorted Submatrices With Maximum Element at Most K

-   [LeetCode](https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/) | [LeetCode CH](https://leetcode.cn/problems/find-sorted-submatrices-with-maximum-element-at-most-k/) (Hard)

-   Tags: array, stack, matrix, monotonic stack

## 2334. Subarray With Elements Greater Than Varying Threshold

-   [LeetCode](https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/) | [LeetCode CH](https://leetcode.cn/problems/subarray-with-elements-greater-than-varying-threshold/) (Hard)

-   Tags: array, stack, union find, monotonic stack
