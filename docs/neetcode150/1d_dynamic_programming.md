---
comments: True
---

# 1D Dynamic Programming

- [x] [70. Climbing Stairs](https://leetcode.cn/problems/climbing-stairs/) (Easy)
- [x] [746. Min Cost Climbing Stairs](https://leetcode.cn/problems/min-cost-climbing-stairs/) (Easy)
- [x] [198. House Robber](https://leetcode.cn/problems/house-robber/) (Medium)
- [x] [213. House Robber II](https://leetcode.cn/problems/house-robber-ii/) (Medium)
- [x] [5. Longest Palindromic Substring](https://leetcode.cn/problems/longest-palindromic-substring/) (Medium)
- [x] [647. Palindromic Substrings](https://leetcode.cn/problems/palindromic-substrings/) (Medium)
- [x] [91. Decode Ways](https://leetcode.cn/problems/decode-ways/) (Medium)
- [x] [322. Coin Change](https://leetcode.cn/problems/coin-change/) (Medium)
- [x] [152. Maximum Product Subarray](https://leetcode.cn/problems/maximum-product-subarray/) (Medium)
- [x] [139. Word Break](https://leetcode.cn/problems/word-break/) (Medium)
- [x] [300. Longest Increasing Subsequence](https://leetcode.cn/problems/longest-increasing-subsequence/) (Medium)
- [x] [416. Partition Equal Subset Sum](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)

## 70. Climbing Stairs

-   [LeetCode](https://leetcode.com/problems/climbing-stairs/) | [LeetCode CH](https://leetcode.cn/problems/climbing-stairs/) (Easy)

-   Tags: math, dynamic programming, memoization
-   Return the number of distinct ways to reach the top of the stairs.
-   `dp[n]` stores the number of distinct ways to reach the `n-th` stair.
-   Formula: `dp[n] = dp[n - 1] + dp[n - 2]`.
-   Initialize `dp[0] = 0`, `dp[1] = 1`, and `dp[2] = 2`.

|  n  | `dp[n-2]` | `dp[n-1]` | `dp[n]` |
| :-: | :-------: | :-------: | :-----: |
|  0  |     -     |     -     |    0    |
|  1  |     -     |     -     |    1    |
|  2  |     -     |     1     |    2    |
|  3  |     1     |     2     |    3    |
|  4  |     2     |     3     |    5    |
|  5  |     3     |     5     |    8    |
|  6  |     5     |     8     |   13    |
|  7  |     8     |    13     |   21    |
|  8  |    13     |    21     |   34    |
|  9  |    21     |    34     |   55    |
| 10  |    34     |    55     |   89    |

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


print(climbStairsDP(10))  # 89
print(climbStairsDPOptimized(10))  # 89
print(climbStairsRecursion(10))  # 89

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

## 746. Min Cost Climbing Stairs

-   [LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/) | [LeetCode CH](https://leetcode.cn/problems/min-cost-climbing-stairs/) (Easy)

-   Tags: array, dynamic programming
-   Return the minimum cost to reach the top of the stairs.

-   `dp[n]` stores the <u>minimum cost</u> to reach the `n-th` stair.
-   Formula: `dp[n] = cost[n] + min(dp[n - 1], dp[n - 2])`.
-   Initialize `dp[0] = cost[0]` and `dp[1] = cost[1]`.
-   Return `min(dp[-1], dp[-2])`.

-   Example: `cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]`

|  n  | `cost[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----: |
|  0  |     1     |     -     |     -     |    1    |
|  1  |    100    |     -     |     1     |   100   |
|  2  |     1     |     1     |    100    |    2    |
|  3  |     1     |    100    |     2     |    3    |
|  4  |     1     |     2     |     3     |    3    |
|  5  |    100    |     3     |     3     |   103   |
|  6  |     1     |     3     |    103    |    4    |
|  7  |     1     |    103    |     4     |    5    |
|  8  |    100    |     4     |     5     |   104   |
|  9  |     1     |     5     |    104    |    6    |

```python title="746. Min Cost Climbing Stairs - Python Solution"
from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    dp = [0 for _ in range(len(cost))]

    dp[0], dp[1] = cost[0], cost[1]

    for i in range(2, len(cost)):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    print(dp)
    return min(dp[-1], dp[-2])


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))  # 6

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

## 213. House Robber II

-   [LeetCode](https://leetcode.com/problems/house-robber-ii/) | [LeetCode CH](https://leetcode.cn/problems/house-robber-ii/) (Medium)

-   Tags: array, dynamic programming
-   Return the maximum amount of money that can be robbed from the houses arranged in a circle.
-   Circular → Linear: `nums[0]` and `nums[-1]` cannot be robbed together.
-   Rob from `0` to `n - 2`

|  n  | `nums[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n-2] + nums[n]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----------------: | :-----: |
|  0  |     2     |     -     |     2     |          -          |    2    |
|  1  |     7     |     -     |     7     |          -          |    7    |
|  2  |     9     |     2     |     7     |         11          |   11    |
|  3  |     3     |     7     |    11     |         10          |   11    |

-   Rob from `1` to `n - 1`

|  n  | `nums[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n-2] + nums[n]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----------------: | :-----: |
|  1  |     7     |     -     |     -     |          -          |    7    |
|  2  |     9     |     -     |     7     |          -          |    9    |
|  3  |     3     |     7     |     9     |         10          |   10    |
|  4  |     1     |     9     |    10     |         10          |   10    |

```python title="213. House Robber II - Python Solution"
from typing import List


# DP
def rob(nums: List[int]) -> int:
    if len(nums) <= 3:
        return max(nums)

    def robLinear(nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    # circle -> linear
    a = robLinear(nums[1:])  # 2nd house to the last house
    b = robLinear(nums[:-1])  # 1st house to the 2nd last house

    return max(a, b)


nums = [2, 7, 9, 3, 1]
print(rob(nums))  # 11

```

```cpp title="213. House Robber II - C++ Solution"
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// DP
int robDP(vector<int>& nums) {
    int n = nums.size();
    if (n <= 3) return *max_element(nums.begin(), nums.end());

    vector<int> dp1(n, 0), dp2(n, 0);

    dp1[0] = nums[0];
    dp2[1] = max(nums[0], nums[1]);
    for (int i = 2; i < n - 1; i++) {
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i]);
    }

    dp2[1] = nums[1];
    dp2[2] = max(nums[1], nums[2]);
    for (int i = 3; i < n; i++) {
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i]);
    }

    return max(dp1[n - 2], dp2[n - 1]);
}

// DP (Space Optimized)
int robDPOptimized(vector<int>& nums) {
    int n = nums.size();
    if (n <= 3) return *max_element(nums.begin(), nums.end());

    int f1 = nums[0];
    int f2 = max(nums[0], nums[1]);
    int res1;
    for (int i = 2; i < n - 1; i++) {
        res1 = max(f2, f1 + nums[i]);
        f1 = f2;
        f2 = res1;
    }

    f1 = nums[1];
    f2 = max(nums[1], nums[2]);
    int res2;
    for (int i = 3; i < n; i++) {
        res2 = max(f2, f1 + nums[i]);
        f1 = f2;
        f2 = res2;
    }

    return max(res1, res2);
}

int main() {
    vector<int> nums = {2, 3, 2};
    cout << robDP(nums) << endl;           // 3
    cout << robDPOptimized(nums) << endl;  // 3

    nums = {1, 2, 3, 1};
    cout << robDP(nums) << endl;           // 4
    cout << robDPOptimized(nums) << endl;  // 4

    return 0;
}

```

## 5. Longest Palindromic Substring

-   [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/) | [LeetCode CH](https://leetcode.cn/problems/longest-palindromic-substring/) (Medium)

-   Tags: two pointers, string, dynamic programming
-   Return the longest palindromic substring in `s`.

```python title="5. Longest Palindromic Substring - Python Solution"
# DP - Interval
def longestPalindromeDP(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    start, maxLen = 0, 1

    # Init
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for j in range(1, n):
        for i in range(j):
            if s[i] == s[j]:
                if j - i <= 2:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    start = i

    return s[start : start + maxLen]


# Expand Around Center
def longestPalindromeCenter(s: str) -> str:
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    if len(s) <= 1:
        return s

    start, end = 0, 0
    for i in range(len(s)):
        len1 = expand_around_center(i, i)  # odd
        len2 = expand_around_center(i, i + 1)  # even

        maxLen = max(len1, len2)
        if maxLen > end - start:
            start = i - (maxLen - 1) // 2
            end = i + maxLen // 2

    return s[start : end + 1]


s = "babad"
print(longestPalindromeDP(s))  # "bab"
print(longestPalindromeCenter(s))  # "aba"

```

## 647. Palindromic Substrings

-   [LeetCode](https://leetcode.com/problems/palindromic-substrings/) | [LeetCode CH](https://leetcode.cn/problems/palindromic-substrings/) (Medium)

-   Tags: two pointers, string, dynamic programming
-   Return the number of palindromic substrings in `s`.
-   Bottom-up DP table

|  dp   |  a  |  b  |  b  |  a  |  e  |
| :---: | :-: | :-: | :-: | :-: | :-: |
| **a** |  1  |  0  |  0  |  1  |  0  |
| **b** |  0  |  1  |  1  |  0  |  0  |
| **b** |  0  |  0  |  1  |  0  |  0  |
| **a** |  0  |  0  |  0  |  1  |  0  |
| **e** |  0  |  0  |  0  |  0  |  1  |

```python title="647. Palindromic Substrings - Python Solution"
def countSubstrings(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    res = 0

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i <= 1:
                    dp[i][j] = 1
                    res += 1
                elif dp[i + 1][j - 1]:
                    dp[i][j] = 1
                    res += 1

    return res


print(countSubstrings("abbae"))  # 7

```

## 91. Decode Ways

-   [LeetCode](https://leetcode.com/problems/decode-ways/) | [LeetCode CH](https://leetcode.cn/problems/decode-ways/) (Medium)

-   Tags: string, dynamic programming

```python title="91. Decode Ways - Python Solution"
# DP
def numDecodingsDP(s: str) -> int:
    if not s or s[0] == "0":
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        # Check single digit decode
        if s[i - 1] != "0":
            dp[i] += dp[i - 1]

        # Check two digit decode
        if i > 1 and "10" <= s[i - 2 : i] <= "26":
            dp[i] += dp[i - 2]

    return dp[n]


# DFS
def numDecodingsDFS(s: str) -> int:
    memo = {}

    def dfs(i):
        if i == len(s):
            return 1

        if s[i] == "0":
            return 0

        if i in memo:
            return memo[i]

        # Single digit decode
        ways = dfs(i + 1)

        # Two digits decode
        if i + 1 < len(s) and "10" <= s[i : i + 2] <= "26":
            ways += dfs(i + 2)

        memo[i] = ways

        return ways

    return dfs(0)


s = "226"
print(numDecodingsDP(s))  # 3
print(numDecodingsDFS(s))  # 3

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

## 139. Word Break

-   [LeetCode](https://leetcode.com/problems/word-break/) | [LeetCode CH](https://leetcode.cn/problems/word-break/) (Medium)

-   Tags: array, hash table, string, dynamic programming, trie, memoization

```python title="139. Word Break - Python Solution"
from typing import List


# DP - Knapsack Unbounded
def wordBreak(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    wordSet = set(wordDict)
    dp = [False for _ in range(n + 1)]
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break

    return dp[n]


s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))  # True

```

## 300. Longest Increasing Subsequence

-   [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/longest-increasing-subsequence/) (Medium)

-   Tags: array, binary search, dynamic programming

```python title="300. Longest Increasing Subsequence - Python Solution"
from typing import List


# DP - LIS
def lengthOfLIS(nums: List[int]) -> int:
    # TC: O(n^2)
    # SC: O(n)
    n = len(nums)
    if n <= 1:
        return n

    dp = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))  # 4

```

## 416. Partition Equal Subset Sum

-   [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/) | [LeetCode CH](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)

-   Tags: array, dynamic programming

```python title="416. Partition Equal Subset Sum - Python Solution"
from typing import List

from template import knapsack01


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


nums = [1, 5, 11, 5]
print(canPartitionTemplate(nums))  # True
print(canPartition(nums))  # True

```
