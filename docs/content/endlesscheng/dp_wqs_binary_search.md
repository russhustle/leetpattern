---
comments: True
---

# DP WQS Binary Search

## Table of Contents

- [x] [188. Best Time to Buy and Sell Stock IV](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/) (Hard)
- [ ] [2209. Minimum White Tiles After Covering With Carpets](https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets/) (Hard)

## 188. Best Time to Buy and Sell Stock IV

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/) (Hard)

-   Tags: array, dynamic programming
```python title="188. Best Time to Buy and Sell Stock IV - Python Solution"
from typing import List


# DP
def maxProfit(k: int, prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * (2 * k + 1) for _ in range(n)]

    for j in range(1, 2 * k, 2):
        dp[0][j] = -prices[0]

    for i in range(1, n):
        for j in range(0, 2 * k - 1, 2):
            dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])
            dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])

    return dp[-1][2 * k]


k = 2
prices = [2, 4, 1]
print(maxProfit(k, prices))  # 2

```

## 2209. Minimum White Tiles After Covering With Carpets

-   [LeetCode](https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/) | [LeetCode CH](https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets/) (Hard)

-   Tags: string, dynamic programming, prefix sum
