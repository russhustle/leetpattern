---
comments: True
---

# DP Unbounded Knapsack

## Table of Contents

- [x] [139. Word Break](https://leetcode.cn/problems/word-break/) (Medium)
- [x] [279. Perfect Squares](https://leetcode.cn/problems/perfect-squares/) (Medium)
- [x] [322. Coin Change](https://leetcode.cn/problems/coin-change/) (Medium)
- [x] [518. Coin Change II](https://leetcode.cn/problems/coin-change-ii/) (Medium)
- [x] [377. Combination Sum IV](https://leetcode.cn/problems/combination-sum-iv/) (Medium)

## 139. Word Break

-   [LeetCode](https://leetcode.com/problems/word-break/) | [LeetCode CH](https://leetcode.cn/problems/word-break/) (Medium)

-   Tags: array, hash table, string, dynamic programming, trie, memoization

```python title="139. Word Break - Python Solution"
from typing import List


# DP (Unbounded Knapsack)
def wordBreak(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [False for _ in range(n + 1)]
    dp[0] = True

    for i in range(1, n + 1):
        for word in wordDict:
            m = len(word)
            if s[i - m : i] == word and dp[i - m]:
                dp[i] = True
    return dp[-1]


s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))  # True

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

## 377. Combination Sum IV

-   [LeetCode](https://leetcode.com/problems/combination-sum-iv/) | [LeetCode CH](https://leetcode.cn/problems/combination-sum-iv/) (Medium)

-   Tags: array, dynamic programming

```python title="377. Combination Sum IV - Python Solution"
from typing import List


def combinationSum4(nums: List[int], target: int) -> int:
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1

    for i in range(1, target + 1):
        for j in range(len(nums)):
            if i - nums[j] >= 0:
                dp[i] += dp[i - nums[j]]

        return dp[target]


nums = [1, 2, 3]
target = 4
print(combinationSum4(nums, target))  # 7

```
