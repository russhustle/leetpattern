---
comments: True
---

# 1D Prefix Sum

- [ ] [1310. XOR Queries of a Subarray](https://leetcode.cn/problems/xor-queries-of-a-subarray/) (Medium)
- [ ] [2438. Range Product Queries of Powers](https://leetcode.cn/problems/range-product-queries-of-powers/) (Medium)
- [ ] [1895. Largest Magic Square](https://leetcode.cn/problems/largest-magic-square/) (Medium)
- [ ] [1878. Get Biggest Three Rhombus Sums in a Grid](https://leetcode.cn/problems/get-biggest-three-rhombus-sums-in-a-grid/) (Medium)
- [ ] [1031. Maximum Sum of Two Non-Overlapping Subarrays](https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/) (Medium)
- [ ] [2245. Maximum Trailing Zeros in a Cornered Path](https://leetcode.cn/problems/maximum-trailing-zeros-in-a-cornered-path/) (Medium)
- [ ] [1712. Ways to Split Array Into Three Subarrays](https://leetcode.cn/problems/ways-to-split-array-into-three-subarrays/) (Medium)
- [ ] [1862. Sum of Floored Pairs](https://leetcode.cn/problems/sum-of-floored-pairs/) (Hard)
- [ ] [363. Max Sum of Rectangle No Larger Than K](https://leetcode.cn/problems/max-sum-of-rectangle-no-larger-than-k/) (Hard)
- [x] [2281. Sum of Total Strength of Wizards](https://leetcode.cn/problems/sum-of-total-strength-of-wizards/) (Hard)
- [ ] [3445. Maximum Difference Between Even and Odd Frequency II](https://leetcode.cn/problems/maximum-difference-between-even-and-odd-frequency-ii/) (Hard)
- [ ] [2983. Palindrome Rearrangement Queries](https://leetcode.cn/problems/palindrome-rearrangement-queries/) (Hard)
- [ ] [2955. Number of Same-End Substrings](https://leetcode.cn/problems/number-of-same-end-substrings/) (Medium) 👑
- [ ] [1788. Maximize the Beauty of the Garden](https://leetcode.cn/problems/maximize-the-beauty-of-the-garden/) (Hard) 👑
- [ ] [2819. Minimum Relative Loss After Buying Chocolates](https://leetcode.cn/problems/minimum-relative-loss-after-buying-chocolates/) (Hard) 👑

## 1310. XOR Queries of a Subarray

-   [LeetCode](https://leetcode.com/problems/xor-queries-of-a-subarray/) | [LeetCode CH](https://leetcode.cn/problems/xor-queries-of-a-subarray/) (Medium)

-   Tags: array, bit manipulation, prefix sum

## 2438. Range Product Queries of Powers

-   [LeetCode](https://leetcode.com/problems/range-product-queries-of-powers/) | [LeetCode CH](https://leetcode.cn/problems/range-product-queries-of-powers/) (Medium)

-   Tags: array, bit manipulation, prefix sum

## 1895. Largest Magic Square

-   [LeetCode](https://leetcode.com/problems/largest-magic-square/) | [LeetCode CH](https://leetcode.cn/problems/largest-magic-square/) (Medium)

-   Tags: array, matrix, prefix sum

## 1878. Get Biggest Three Rhombus Sums in a Grid

-   [LeetCode](https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/get-biggest-three-rhombus-sums-in-a-grid/) (Medium)

-   Tags: array, math, sorting, heap priority queue, matrix, prefix sum

## 1031. Maximum Sum of Two Non-Overlapping Subarrays

-   [LeetCode](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/) (Medium)

-   Tags: array, dynamic programming, sliding window

## 2245. Maximum Trailing Zeros in a Cornered Path

-   [LeetCode](https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/) | [LeetCode CH](https://leetcode.cn/problems/maximum-trailing-zeros-in-a-cornered-path/) (Medium)

-   Tags: array, matrix, prefix sum

## 1712. Ways to Split Array Into Three Subarrays

-   [LeetCode](https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/ways-to-split-array-into-three-subarrays/) (Medium)

-   Tags: array, two pointers, binary search, prefix sum

## 1862. Sum of Floored Pairs

-   [LeetCode](https://leetcode.com/problems/sum-of-floored-pairs/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-floored-pairs/) (Hard)

-   Tags: array, math, binary search, prefix sum

## 363. Max Sum of Rectangle No Larger Than K

-   [LeetCode](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/) | [LeetCode CH](https://leetcode.cn/problems/max-sum-of-rectangle-no-larger-than-k/) (Hard)

-   Tags: array, binary search, matrix, prefix sum, ordered set

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
        tot = (i - l + 1) * (prefix_sum[r + 2] - prefix_sum[i + 1]) - (r - i + 1) * (
            prefix_sum[i + 1] - prefix_sum[l]
        )
        ans += v * tot

    return ans % (10**9 + 7)


strength = [1, 3, 1, 2]
print(totalStrength(strength))  # 44

```

## 3445. Maximum Difference Between Even and Odd Frequency II

-   [LeetCode](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/) | [LeetCode CH](https://leetcode.cn/problems/maximum-difference-between-even-and-odd-frequency-ii/) (Hard)

-   Tags: string, sliding window, enumeration, prefix sum

## 2983. Palindrome Rearrangement Queries

-   [LeetCode](https://leetcode.com/problems/palindrome-rearrangement-queries/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-rearrangement-queries/) (Hard)

-   Tags: hash table, string, prefix sum

## 2955. Number of Same-End Substrings

-   [LeetCode](https://leetcode.com/problems/number-of-same-end-substrings/) | [LeetCode CH](https://leetcode.cn/problems/number-of-same-end-substrings/) (Medium)

-   Tags: array, hash table, string, counting, prefix sum

## 1788. Maximize the Beauty of the Garden

-   [LeetCode](https://leetcode.com/problems/maximize-the-beauty-of-the-garden/) | [LeetCode CH](https://leetcode.cn/problems/maximize-the-beauty-of-the-garden/) (Hard)

-   Tags: array, hash table, greedy, prefix sum

## 2819. Minimum Relative Loss After Buying Chocolates

-   [LeetCode](https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/) | [LeetCode CH](https://leetcode.cn/problems/minimum-relative-loss-after-buying-chocolates/) (Hard)

-   Tags: array, binary search, sorting, prefix sum
