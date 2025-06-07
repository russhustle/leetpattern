---
comments: True
---

# Dynamic Programming

## Table of Contents

- [x] [70. Climbing Stairs](https://leetcode.cn/problems/climbing-stairs/) (Easy)
- [x] [118. Pascal's Triangle](https://leetcode.cn/problems/pascals-triangle/) (Easy)
- [x] [198. House Robber](https://leetcode.cn/problems/house-robber/) (Medium)
- [x] [279. Perfect Squares](https://leetcode.cn/problems/perfect-squares/) (Medium)
- [x] [322. Coin Change](https://leetcode.cn/problems/coin-change/) (Medium)
- [x] [139. Word Break](https://leetcode.cn/problems/word-break/) (Medium)
- [x] [300. Longest Increasing Subsequence](https://leetcode.cn/problems/longest-increasing-subsequence/) (Medium)
- [x] [152. Maximum Product Subarray](https://leetcode.cn/problems/maximum-product-subarray/) (Medium)
- [x] [416. Partition Equal Subset Sum](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)
- [x] [32. Longest Valid Parentheses](https://leetcode.cn/problems/longest-valid-parentheses/) (Hard)

## 70. Climbing Stairs

-   [LeetCode](https://leetcode.com/problems/climbing-stairs/) | [LeetCode CH](https://leetcode.cn/problems/climbing-stairs/) (Easy)

-   Tags: math, dynamic programming, memoization
- Return the number of distinct ways to reach the top of the stairs.
- `dp[n]` stores the number of distinct ways to reach the `n-th` stair.
- Formula: `dp[n] = dp[n - 1] + dp[n - 2]`.
- Initialize `dp[0] = 0`, `dp[1] = 1`, and `dp[2] = 2`.


```python title="70. Climbing Stairs - Python Solution"
from functools import cache


# DP
def climbStairsDP(n: int) -> int:
    if n <= 2:
        return n

    dp = [i for i in range(n + 1)]

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# DP (Optimized)
def climbStairsDPOptimized(n: int) -> int:
    if n <= 2:
        return n

    first, second = 1, 2

    for _ in range(3, n + 1):
        first, second = second, first + second

    return second


# Recursion
def climbStairsRecursion(n: int) -> int:
    @cache
    def dfs(i: int) -> int:
        if i <= 1:
            return 1
        return dfs(i - 1) + dfs(i - 2)

    return dfs(n)


# Greedy
def climbStairsGreedy(n: int) -> int:
    if n <= 2:
        return n

    p1, p2 = 1, 2

    for _ in range(3, n + 1):
        p1, p2 = p2, p1 + p2

    return p2


if __name__ == "__main__":
    assert climbStairsDP(10) == 89
    assert climbStairsDPOptimized(10) == 89
    assert climbStairsRecursion(10) == 89
    assert climbStairsGreedy(10) == 89

```

```cpp title="70. Climbing Stairs - C++ Solution"
#include <iostream>
using namespace std;

int climbStairs(int n) {
    if (n <= 2) return n;
    int f1 = 1, f2 = 2;
    int res;

    int i = 3;
    while (i <= n) {
        res = f1 + f2;
        f1 = f2;
        f2 = res;
        ++i;
    }
    return res;
}

int main() {
    cout << climbStairs(2) << endl;  // 2
    cout << climbStairs(3) << endl;  // 3
    cout << climbStairs(6) << endl;  // 13
    return 0;
}

```

## 118. Pascal's Triangle

-   [LeetCode](https://leetcode.com/problems/pascals-triangle/) | [LeetCode CH](https://leetcode.cn/problems/pascals-triangle/) (Easy)

-   Tags: array, dynamic programming
-   Generate the first `numRows` of Pascal's triangle.

```plaintext
                 numRows    index
     1              1         0
    1 1             2         1
   1 2 1            3         2
  1 3 3 1           4         3
 1 4 6 4 1          5         4
```


```python title="118. Pascal's Triangle - Python Solution"
from typing import List


def generate(numRows: int) -> List[List[int]]:
    dp = [[1] * i for i in range(1, numRows + 1)]

    if numRows <= 2:
        return dp

    for i in range(2, numRows):
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp


print(generate(numRows=5))
#     [[1],
#    [1, 1],
#   [1, 2, 1],
#  [1, 3, 3, 1],
# [1, 4, 6, 4, 1]]

```

## 198. House Robber

-   [LeetCode](https://leetcode.com/problems/house-robber/) | [LeetCode CH](https://leetcode.cn/problems/house-robber/) (Medium)

-   Tags: array, dynamic programming
-   Return the maximum amount of money that can be robbed from the houses. No two adjacent houses can be robbed.

-   `dp[n]` stores the maximum amount of money that can be robbed from the first `n` houses.
-   Formula: `dp[n] = max(dp[n - 1], dp[n - 2] + nums[n])`.
    -   Skip: `dp[n]` → `dp[n - 1]`
    -   Rob: `dp[n]` → `dp[n - 2] + nums[n]`
-   Initialize `dp[0] = nums[0]` and `dp[1] = max(nums[0], nums[1])`.
-   Return `dp[-1]`.
-   Example: `nums = [2, 7, 9, 3, 1]`

|  n  | `nums[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n-2] + nums[n]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----------------: | :-----: |
|  0  |     2     |     -     |     2     |          -          |    2    |
|  1  |     7     |     -     |     7     |          -          |    7    |
|  2  |     9     |     2     |     7     |         11          |   11    |
|  3  |     3     |     7     |    11     |         10          |   11    |
|  4  |     1     |    11     |    11     |         12          |   12    |


```python title="198. House Robber - Python Solution"
from typing import List


# DP (House Robber)
def rob1(nums: List[int]) -> int:
    if len(nums) < 3:
        return max(nums)

    dp = [0 for _ in range(len(nums))]
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]


# DP (House Robber) Optimized
def rob2(nums: List[int]) -> int:
    f0, f1 = 0, 0

    for num in nums:
        f0, f1 = f1, max(f1, f0 + num)

    return f1


nums = [2, 7, 9, 3, 1]
print(rob1(nums))  # 12
print(rob2(nums))  # 12

```

```cpp title="198. House Robber - C++ Solution"
#include <iostream>
#include <vector>
using namespace std;

int rob(vector<int> &nums) {
    int prev = 0, cur = 0, temp = 0;

    for (int num : nums) {
        temp = cur;
        cur = max(cur, prev + num);
        prev = temp;
    }
    return cur;
}

int main() {
    vector<int> nums = {2, 7, 9, 3, 1};
    cout << rob(nums) << endl;  // 12
    return 0;
}

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

## 300. Longest Increasing Subsequence

-   [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/longest-increasing-subsequence/) (Medium)

-   Tags: array, binary search, dynamic programming

```python title="300. Longest Increasing Subsequence - Python Solution"
from functools import cache
from typing import List


# DP - LIS
def lengthOfLISMemo(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return n

    @cache
    def dfs(i: int) -> int:
        res = 0
        for j in range(i):
            if nums[j] < nums[i]:
                res = max(res, dfs(j))
        return res + 1

    return max(dfs(i) for i in range(n))


# DP - LIS
def lengthOfLISTable(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return n

    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


if __name__ == "__main__":
    assert lengthOfLISMemo([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lengthOfLISTable([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lengthOfLISMemo([0, 1, 0, 3, 2, 3]) == 4
    assert lengthOfLISTable([0, 1, 0, 3, 2, 3]) == 4
    assert lengthOfLISMemo([7, 7, 7, 7]) == 1
    assert lengthOfLISTable([7, 7, 7, 7]) == 1

```

## 152. Maximum Product Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-product-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-product-subarray/) (Medium)

-   Tags: array, dynamic programming

```python title="152. Maximum Product Subarray - Python Solution"
from typing import List


# DP - Kadane
def maxProduct(nums: List[int]) -> int:
    n = len(nums)
    dp_max = [0 for _ in range(n)]
    dp_min = [0 for _ in range(n)]

    dp_max[0] = nums[0]
    dp_min[0] = nums[0]
    max_product = nums[0]

    for i in range(1, n):
        dp_max[i] = max(
            nums[i],
            nums[i] * dp_max[i - 1],
            nums[i] * dp_min[i - 1],
        )
        dp_min[i] = min(
            nums[i],
            nums[i] * dp_max[i - 1],
            nums[i] * dp_min[i - 1],
        )

        max_product = max(max_product, dp_max[i])

    return max_product


nums = [2, 3, -2, 4]
print(maxProduct(nums))  # 6

```

## 416. Partition Equal Subset Sum

-   [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/) | [LeetCode CH](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)

-   Tags: array, dynamic programming

```python title="416. Partition Equal Subset Sum - Python Solution"
from functools import cache
from typing import List

from template import knapsack01


# Memoization
def canPartitionMemoization(nums: List[int]) -> bool:
    total = sum(nums)
    n = len(nums)

    if total % 2 == 1 or n <= 1:
        return False

    @cache
    def dfs(i, j):
        if i < 0:
            return j == 0
        return j >= nums[i] and dfs(i - 1, j - nums[i]) or dfs(i - 1, j)

    return dfs(n - 1, total // 2)


# DP - Knapsack 01
def canPartitionTemplate(nums: List[int]) -> bool:
    total = sum(nums)

    if total % 2 == 1 or len(nums) < 2:
        return False

    target = total // 2

    return knapsack01(nums, nums, target) == target


# DP - Knapsack 01
def canPartition(nums: List[int]) -> bool:
    total = sum(nums)

    if total % 2 == 1 or len(nums) < 2:
        return False

    target = total // 2

    dp = [0 for _ in range(target + 1)]

    for i in range(len(nums)):
        for j in range(target, nums[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

    return dp[target] == target


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print(canPartitionTemplate(nums))  # True
    print(canPartition(nums))  # True
    print(canPartitionMemoization(nums))  # True

```

## 32. Longest Valid Parentheses

-   [LeetCode](https://leetcode.com/problems/longest-valid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/longest-valid-parentheses/) (Hard)

-   Tags: string, dynamic programming, stack

```python title="32. Longest Valid Parentheses - Python Solution"
# Stack
def longestValidParentheses(s: str) -> int:
    stack = [-1]
    res = 0

    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)
        elif ch == ")":
            stack.pop()
            if stack:
                res = max(res, i - stack[-1])
            else:
                stack.append(i)

    return res


if __name__ == "__main__":
    print(longestValidParentheses("(()"))  # 2
    print(longestValidParentheses(")()())"))  # 4

```
