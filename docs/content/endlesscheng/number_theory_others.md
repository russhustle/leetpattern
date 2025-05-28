---
comments: True
---

# Number Theory Others

## Table of Contents

- [ ] [326. Power of Three](https://leetcode.cn/problems/power-of-three/) (Easy)
- [ ] [633. Sum of Square Numbers](https://leetcode.cn/problems/sum-of-square-numbers/) (Medium)
- [x] [279. Perfect Squares](https://leetcode.cn/problems/perfect-squares/) (Medium)
- [ ] [1015. Smallest Integer Divisible by K](https://leetcode.cn/problems/smallest-integer-divisible-by-k/) (Medium)
- [ ] [2240. Number of Ways to Buy Pens and Pencils](https://leetcode.cn/problems/number-of-ways-to-buy-pens-and-pencils/) (Medium)
- [ ] [2221. Find Triangular Sum of an Array](https://leetcode.cn/problems/find-triangular-sum-of-an-array/) (Medium)

## 326. Power of Three

-   [LeetCode](https://leetcode.com/problems/power-of-three/) | [LeetCode CH](https://leetcode.cn/problems/power-of-three/) (Easy)

-   Tags: math, recursion
## 633. Sum of Square Numbers

-   [LeetCode](https://leetcode.com/problems/sum-of-square-numbers/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-square-numbers/) (Medium)

-   Tags: math, two pointers, binary search
## 279. Perfect Squares

-   [LeetCode](https://leetcode.com/problems/perfect-squares/) | [LeetCode CH](https://leetcode.cn/problems/perfect-squares/) (Medium)

-   Tags: math, dynamic programming, breadth first search

```python title="279. Perfect Squares - Python Solution"
import math


# DP - Knapsack Unbounded
def numSquares(n: int) -> int:
    dp = [float("inf") for _ in range(n + 1)]
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(1, int(math.sqrt(n)) + 1):
            dp[i] = min(dp[i], dp[i - j**2] + 1)

    return dp[n]


n = 12
print(numSquares(n))  # 3

```

## 1015. Smallest Integer Divisible by K

-   [LeetCode](https://leetcode.com/problems/smallest-integer-divisible-by-k/) | [LeetCode CH](https://leetcode.cn/problems/smallest-integer-divisible-by-k/) (Medium)

-   Tags: hash table, math
## 2240. Number of Ways to Buy Pens and Pencils

-   [LeetCode](https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/) | [LeetCode CH](https://leetcode.cn/problems/number-of-ways-to-buy-pens-and-pencils/) (Medium)

-   Tags: math, enumeration
## 2221. Find Triangular Sum of an Array

-   [LeetCode](https://leetcode.com/problems/find-triangular-sum-of-an-array/) | [LeetCode CH](https://leetcode.cn/problems/find-triangular-sum-of-an-array/) (Medium)

-   Tags: array, math, simulation, combinatorics
