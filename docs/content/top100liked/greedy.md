---
comments: True
---

# Greedy

## Table of Contents

- [x] [121. Best Time to Buy and Sell Stock](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) (Easy)
- [x] [55. Jump Game](https://leetcode.cn/problems/jump-game/) (Medium)
- [x] [45. Jump Game II](https://leetcode.cn/problems/jump-game-ii/) (Medium)
- [x] [763. Partition Labels](https://leetcode.cn/problems/partition-labels/) (Medium)

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

## 55. Jump Game

-   [LeetCode](https://leetcode.com/problems/jump-game/) | [LeetCode CH](https://leetcode.cn/problems/jump-game/) (Medium)

-   Tags: array, dynamic programming, greedy
-   Return `True` if you can reach the last index, otherwise `False`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Yan0cv2cLy8?si=musT5NViPicljg7x" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

-   Example: `[2, 3, 1, 1, 4, 1, 2, 0, 0]`

| Index | Value | Index + Value | Max Reach | Max Reach >= Last Index |
| :---: | :---: | :-----------: | :-------: | :---------------------: |
|   0   |   2   |       2       |     2     |          False          |
|   1   |   3   |       4       |     4     |          False          |
|   2   |   1   |       3       |     4     |          False          |
|   3   |   1   |       4       |     4     |          False          |
|   4   |   4   |       8       |     8     |          True           |
|   5   |   1   |       6       |     8     |          True           |
|   6   |   2   |       8       |     8     |          True           |
|   7   |   0   |       7       |     8     |          True           |
|   8   |   0   |       8       |     8     |          True           |


```python title="55. Jump Game - Python Solution"
from typing import List


# Greedy - Interval
def canJump(nums: List[int]) -> bool:
    maxReach = 0
    i = 0
    n = len(nums)

    while i <= maxReach:
        maxReach = max(maxReach, i + nums[i])
        if maxReach >= n - 1:
            return True
        i += 1

    return False


print(canJump([2, 3, 1, 1, 4, 1, 2, 0, 0]))  # True

```

```cpp title="55. Jump Game - C++ Solution"
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
   public:
    bool canJump(vector<int>& nums) {
        int canReach = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            if (i > canReach) return false;
            canReach = max(canReach, i + nums[i]);
        }
        return true;
    }
};

int main() {
    Solution obj;
    vector<int> nums = {2, 3, 1, 1, 4};
    cout << obj.canJump(nums) << endl;
    return 0;
}

```

## 45. Jump Game II

-   [LeetCode](https://leetcode.com/problems/jump-game-ii/) | [LeetCode CH](https://leetcode.cn/problems/jump-game-ii/) (Medium)

-   Tags: array, dynamic programming, greedy
-   Return the minimum number of jumps to reach the last index.

<iframe width="560" height="315" src="https://www.youtube.com/embed/dJ7sWiOoK7g?si=3kc-pp4rs3Dk7Jqk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


```python title="45. Jump Game II - Python Solution"
from typing import List


# Greedy (Interval)
def jump(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0

    maxReach = 0
    left, right = 0, 0
    res = 0

    while right < n - 1:
        for i in range(left, right + 1):
            maxReach = max(maxReach, i + nums[i])

        left = right + 1
        right = maxReach
        res += 1

    return res


print(jump([2, 3, 1, 1, 4, 2, 1]))  # 3

```

## 763. Partition Labels

-   [LeetCode](https://leetcode.com/problems/partition-labels/) | [LeetCode CH](https://leetcode.cn/problems/partition-labels/) (Medium)

-   Tags: hash table, two pointers, string, greedy

```python title="763. Partition Labels - Python Solution"
from typing import List


# 1. Hashmap
def partitionLabels1(s: str) -> List[int]:
    hashmap = {}

    for i, j in enumerate(s):
        if j not in hashmap:
            hashmap[j] = [i, i]
        else:
            hashmap[j][1] = i

    intervals = list(hashmap.values())
    intervals.sort(key=lambda x: x[0])

    if len(intervals) < 2:
        return len(intervals)

    res = []
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            intervals[i][1] = max(intervals[i][1], intervals[i - 1][1])
        else:
            res.append(intervals[i][0])

    res.append(intervals[-1][1] + 1)

    if len(res) == 1:
        return res
    else:
        for i in range(len(res) - 1, 0, -1):
            res[i] -= res[i - 1]
        return res


# Single Pass Partitioning
def partitionLabels2(s: str) -> List[int]:
    last = {c: i for i, c in enumerate(s)}
    res = []
    start, end = 0, 0

    for i, c in enumerate(s):
        end = max(end, last[c])
        if end == i:
            res.append(end - start + 1)
            start = i + 1

    return res


print(partitionLabels1("abaccd"))  # [3, 2, 1]
print(partitionLabels2("abaccd"))  # [3, 2, 1]

```
