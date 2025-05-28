---
comments: True
---

# DP Complete Knapsack

## Table of Contents

- [x] [322. Coin Change](https://leetcode.cn/problems/coin-change/) (Medium)
- [x] [518. Coin Change II](https://leetcode.cn/problems/coin-change-ii/) (Medium)
- [x] [279. Perfect Squares](https://leetcode.cn/problems/perfect-squares/) (Medium)
- [ ] [1449. Form Largest Integer With Digits That Add up to Target](https://leetcode.cn/problems/form-largest-integer-with-digits-that-add-up-to-target/) (Hard)
- [ ] [3183. The Number of Ways to Make the Sum](https://leetcode.cn/problems/the-number-of-ways-to-make-the-sum/) (Medium) 👑

## 322. Coin Change

-   [LeetCode](https://leetcode.com/problems/coin-change/) | [LeetCode CH](https://leetcode.cn/problems/coin-change/) (Medium)

-   Tags: array, dynamic programming, breadth first search

```python title="322. Coin Change - Python Solution"
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    dp = [float("inf") for _ in range(amount + 1)]

    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], 1 + dp[i - c])

    return dp[amount] if dp[amount] != float("inf") else -1


coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))  # 3

```

## 518. Coin Change II

-   [LeetCode](https://leetcode.com/problems/coin-change-ii/) | [LeetCode CH](https://leetcode.cn/problems/coin-change-ii/) (Medium)

-   Tags: array, dynamic programming

```python title="518. Coin Change II - Python Solution"
from typing import List


def change(amount: int, coins: List[int]) -> int:
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1

    for i in range(len(coins)):
        for j in range(coins[i], amount + 1):
            dp[j] += dp[j - coins[i]]

    return dp[-1]


amount = 5
coins = [1, 2, 5]
print(change(amount, coins))  # 4

```

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

## 1449. Form Largest Integer With Digits That Add up to Target

-   [LeetCode](https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/) | [LeetCode CH](https://leetcode.cn/problems/form-largest-integer-with-digits-that-add-up-to-target/) (Hard)

-   Tags: array, dynamic programming
## 3183. The Number of Ways to Make the Sum

-   [LeetCode](https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/) | [LeetCode CH](https://leetcode.cn/problems/the-number-of-ways-to-make-the-sum/) (Medium)

-   Tags: array, dynamic programming
