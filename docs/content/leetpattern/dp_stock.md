---
comments: True
---

# DP Stock

- [x] [121. Best Time to Buy and Sell Stock](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) (Easy)
- [x] [122. Best Time to Buy and Sell Stock II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) (Medium)
- [x] [123. Best Time to Buy and Sell Stock III](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/) (Hard)
- [x] [188. Best Time to Buy and Sell Stock IV](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/) (Hard)
- [x] [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/) (Medium)
- [x] [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) (Medium)

## 121. Best Time to Buy and Sell Stock

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) (Easy)

-   Tags: array, dynamic programming
-   Return the maximum profit that can be achieved from buying on one day and selling on another day.

```python title="121. Best Time to Buy and Sell Stock - Python Solution"
from typing import List


# Brute Force
def maxProfitBF(prices: List[int]) -> int:
    max_profit = 0
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            max_profit = max(max_profit, prices[j] - prices[i])

    return max_profit


# DP
def maxProfitDP(prices: List[int]) -> int:
    dp = [[0] * 2 for _ in range(len(prices))]
    dp[0][0] = -prices[0]  # buy
    dp[0][1] = 0  # sell

    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], -prices[i])  # the lowest price to buy
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

    return dp[-1][1]


# Greedy
def maxProfitGreedy(prices: List[int]) -> int:
    max_profit = 0
    seen_min = prices[0]

    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - seen_min)
        seen_min = min(seen_min, prices[i])

    return max_profit


# Fast Slow Pointers
def maxProfitFS(prices: List[int]) -> int:
    max_profit = 0
    slow, fast = 0, 1

    while fast < len(prices):
        if prices[fast] > prices[slow]:
            max_profit = max(max_profit, prices[fast] - prices[slow])
        else:
            slow = fast
        fast += 1

    return max_profit


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# | Brute Force|  O(n^2)|  O(1)   |
# | DP         |  O(n)  |  O(n)   |
# | Greedy     |  O(n)  |  O(1)   |
# | Fast Slow  |  O(n)  |  O(1)   |
# |------------|--------|---------|


prices = [7, 1, 5, 3, 6, 4]
print(maxProfitBF(prices))  # 5
print(maxProfitDP(prices))  # 5
print(maxProfitGreedy(prices))  # 5
print(maxProfitFS(prices))  # 5

```

```cpp title="121. Best Time to Buy and Sell Stock - C++ Solution"
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        if (prices.size() <= 1)
            return 0;

        int seen_min = prices[0];
        int res = 0;

        for (int &price : prices)
        {
            res = max(res, price - seen_min);
            seen_min = min(seen_min, price);
        }
        return res;
    }
};

int main()
{
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    Solution obj;
    cout << obj.maxProfit(prices) << endl;
    return 0;
}

```

## 122. Best Time to Buy and Sell Stock II

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) (Medium)

-   Tags: array, dynamic programming, greedy
-   Return the maximum profit you can achieve.

```python title="122. Best Time to Buy and Sell Stock II - Python Solution"
from typing import List


# DP
def maxProfitDP1(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = -prices[0]
    dp[0][1] = 0

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

    return dp[-1][1]


# DP - Optimized
def maxProfitDP2(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    hold = -prices[0]
    profit = 0

    for i in range(1, n):
        hold = max(hold, profit - prices[i])
        profit = max(profit, hold + prices[i])

    return profit


# Greedy
def maxProfitGreedy(prices: List[int]) -> int:
    profit = 0

    for i in range(1, len(prices)):
        profit += max(prices[i] - prices[i - 1], 0)

    return profit


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |     DP1    |  O(n)  |   O(n)  |
# |     DP2    |  O(n)  |   O(1)  |
# |   Greedy   |  O(n)  |   O(1)  |
# |------------|--------|---------|


prices = [7, 1, 5, 3, 6, 4]
print(maxProfitDP1(prices))  # 7
print(maxProfitDP2(prices))  # 7
print(maxProfitGreedy(prices))  # 7

```

## 123. Best Time to Buy and Sell Stock III

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/) (Hard)

-   Tags: array, dynamic programming

```python title="123. Best Time to Buy and Sell Stock III - Python Solution"
from typing import List


# 1. DP
def maxProfitDP1(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * 5 for _ in range(n)]

    dp[0][0] = 0  # no transaction
    dp[0][1] = -prices[0]  # buy 1
    dp[0][2] = 0  # sell 1
    dp[0][3] = -prices[0]  # buy 2
    dp[0][4] = 0  # sell 2

    for i in range(1, n):
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = max(dp[i - 1][1], -prices[i])
        dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
        dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
        dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])

    return dp[-1][4]


# 2. DP - Optimized
def maxProfitDP2(prices: List[int]) -> int:
    b1, b2 = float("inf"), float("inf")
    s1, s2 = 0, 0

    for price in prices:
        b1 = min(b1, price)
        s1 = max(s1, price - b1)
        b2 = min(b2, price - s1)
        s2 = max(s2, price - b2)

    return s2


prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(maxProfitDP1(prices))  # 6
print(maxProfitDP2(prices))  # 6

```

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

## 309. Best Time to Buy and Sell Stock with Cooldown

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/) (Medium)

-   Tags: array, dynamic programming

```python title="309. Best Time to Buy and Sell Stock with Cooldown - Python Solution"
from typing import List


# DP
def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * 4 for _ in range(n)]

    dp[0][0] = -prices[0]  # poessess
    dp[0][1] = 0  # stay sold
    dp[0][2] = 0  # sell
    dp[0][3] = 0  # cooldown

    for i in range(1, n):
        dp[i][0] = max(
            dp[i - 1][0],  # stay poessess
            dp[i - 1][1] - prices[i],  # buy after stay sold
            dp[i - 1][3] - prices[i],  # buy after cooldown
        )
        dp[i][1] = max(
            dp[i - 1][1],  # stay sold
            dp[i - 1][3],  # stay cooldown
        )
        dp[i][2] = dp[i - 1][0] + prices[i]
        dp[i][3] = dp[i - 1][2]

    return max(dp[-1])


prices = [1, 2, 3, 0, 2]
print(maxProfit(prices))  # 3

```

## 714. Best Time to Buy and Sell Stock with Transaction Fee

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) (Medium)

-   Tags: array, dynamic programming, greedy
-   Return the maximum profit you can achieve with the given transaction fee.

```python title="714. Best Time to Buy and Sell Stock with Transaction Fee - Python Solution"
from typing import List


# 1. DP
def maxProfitDP(prices: List[int], fee: int) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * 2 for _ in range(n)]

    dp[0][0] = -prices[0] - fee
    dp[0][1] = 0

    for i in range(1, n):
        dp[i][0] = max(
            dp[i - 1][0],  # hold
            dp[i - 1][1] - prices[i] - fee,  # buy
        )
        dp[i][1] = max(
            dp[i - 1][1],  # hold
            dp[i - 1][0] + prices[i],  # sell
        )

    return max(dp[-1])


# 2. Greedy
def maxProfitGreedy(prices: List[int], fee: int) -> int:
    n = len(prices)
    if n == 0:
        return 0

    buy = prices[0]
    profit = 0

    for i in range(1, n):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] > buy + fee:
            profit += prices[i] - buy - fee
            buy = prices[i] - fee

    return profit


prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(maxProfitDP(prices, fee))  # 8
print(maxProfitGreedy(prices, fee))  # 8

```
