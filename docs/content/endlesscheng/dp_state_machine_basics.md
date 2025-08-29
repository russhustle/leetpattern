---
comments: True
---

# DP State Machine Basics

## Table of Contents

- [ ] [3259. Maximum Energy Boost From Two Drinks](https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/) (Medium)
- [ ] [2222. Number of Ways to Select Buildings](https://leetcode.cn/problems/number-of-ways-to-select-buildings/) (Medium)
- [ ] [1567. Maximum Length of Subarray With Positive Product](https://leetcode.cn/problems/maximum-length-of-subarray-with-positive-product/) (Medium)
- [x] [2708. Maximum Strength of a Group](https://leetcode.cn/problems/maximum-strength-of-a-group/) (Medium)
- [x] [2826. Sorting Three Groups](https://leetcode.cn/problems/sorting-three-groups/) (Medium)
- [ ] [2786. Visit Array Positions to Maximize Score](https://leetcode.cn/problems/visit-array-positions-to-maximize-score/) (Medium)
- [ ] [1911. Maximum Alternating Subsequence Sum](https://leetcode.cn/problems/maximum-alternating-subsequence-sum/) (Medium)
- [x] [376. Wiggle Subsequence](https://leetcode.cn/problems/wiggle-subsequence/) (Medium)
- [x] [1186. Maximum Subarray Sum with One Deletion](https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/) (Medium)

## 3259. Maximum Energy Boost From Two Drinks

-   [LeetCode](https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/) | [LeetCode CH](https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/) (Medium)

-   Tags: array, dynamic programming
## 2222. Number of Ways to Select Buildings

-   [LeetCode](https://leetcode.com/problems/number-of-ways-to-select-buildings/) | [LeetCode CH](https://leetcode.cn/problems/number-of-ways-to-select-buildings/) (Medium)

-   Tags: string, dynamic programming, prefix sum
## 1567. Maximum Length of Subarray With Positive Product

-   [LeetCode](https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/) | [LeetCode CH](https://leetcode.cn/problems/maximum-length-of-subarray-with-positive-product/) (Medium)

-   Tags: array, dynamic programming, greedy
## 2708. Maximum Strength of a Group

-   [LeetCode](https://leetcode.com/problems/maximum-strength-of-a-group/) | [LeetCode CH](https://leetcode.cn/problems/maximum-strength-of-a-group/) (Medium)

-   Tags: array, dynamic programming, backtracking, greedy, bit manipulation, sorting, enumeration
```python title="2708. Maximum Strength of a Group - Python Solution"
from typing import List


# DP
def maxStrength(nums: List[int]) -> int:
    if not nums:
        return 0

    cur_min, cur_max = nums[0], nums[0]

    for i, num in enumerate(nums):
        if i == 0:
            continue

        temp_min = min(cur_min, num, num * cur_min, num * cur_max)
        temp_max = max(cur_max, num, num * cur_min, num * cur_max)
        cur_min, cur_max = temp_min, temp_max

    return cur_max


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |  DP        |  O(N)  |  O(1)   |
# |------------|--------|---------|


nums = [3, -1, -5, 2, 5, -9]
print(maxStrength(nums))  # 1350

```

## 2826. Sorting Three Groups

-   [LeetCode](https://leetcode.com/problems/sorting-three-groups/) | [LeetCode CH](https://leetcode.cn/problems/sorting-three-groups/) (Medium)

-   Tags: array, binary search, dynamic programming
```python title="2826. Sorting Three Groups - Python Solution"
from functools import cache
from typing import List


# DP - LIS
def minimumOperationsMemo(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    @cache
    def dfs(i):
        res = 0
        for j in range(i):
            if nums[i] >= nums[j]:
                res = max(res, dfs(j))
        return res + 1

    LIS = max(dfs(i) for i in range(n))

    return n - LIS


# DP - LIS
def minimumOperationsTable(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if nums[i] >= nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return n - max(dp)


# DP - LIS
def minimumOperationsTableOptimized(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    dp = [0 for _ in range(4)]

    for num in nums:
        dp[num] += 1
        dp[2] = max(dp[2], dp[1])
        dp[3] = max(dp[3], dp[2])

    return n - dp[3]


if __name__ == "__main__":
    assert minimumOperationsMemo([2, 1, 3, 2, 1]) == 3
    assert minimumOperationsTable([2, 1, 3, 2, 1]) == 3
    assert minimumOperationsTableOptimized([2, 1, 3, 2, 1]) == 3

```

## 2786. Visit Array Positions to Maximize Score

-   [LeetCode](https://leetcode.com/problems/visit-array-positions-to-maximize-score/) | [LeetCode CH](https://leetcode.cn/problems/visit-array-positions-to-maximize-score/) (Medium)

-   Tags: array, dynamic programming
## 1911. Maximum Alternating Subsequence Sum

-   [LeetCode](https://leetcode.com/problems/maximum-alternating-subsequence-sum/) | [LeetCode CH](https://leetcode.cn/problems/maximum-alternating-subsequence-sum/) (Medium)

-   Tags: array, dynamic programming
## 376. Wiggle Subsequence

-   [LeetCode](https://leetcode.com/problems/wiggle-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/wiggle-subsequence/) (Medium)

-   Tags: array, dynamic programming, greedy
-   Return the length of the longest wiggle subsequence.
-   `up[n]` stores the length of the longest wiggle subsequence ending at `n` with a rising wiggle.
-   `down[n]` stores the length of the longest wiggle subsequence ending at `n` with a falling wiggle.
-   Initialize `up[0] = 1` and `down[0] = 1`.
-   Example: `nums = [1, 7, 4, 9, 2, 5]`

| `nums[n]` | `nums[n-1]` | `up[n-1]` | `down[n-1]` | `up[n]` | `down[n]` |
| :-------: | :---------: | :-------: | :---------: | :-----: | :-------: |
|     1     |      -      |     -     |      -      |    1    |     1     |
|     7     |      1      |     1     |      1      |    2    |     1     |
|     4     |      7      |     2     |      1      |    2    |     3     |
|     9     |      4      |     2     |      3      |    4    |     3     |
|     2     |      9      |     4     |      3      |    4    |     5     |
|     5     |      2      |     4     |      5      |    6    |     5     |

```python title="376. Wiggle Subsequence - Python Solution"
from typing import List


# DP
def wiggleMaxLengthDP(nums: List[int]) -> int:
    if len(nums) <= 1:
        return len(nums)

    up = [0 for _ in range(len(nums))]
    down = [0 for _ in range(len(nums))]

    up[0], down[0] = 1, 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up[i] = down[i - 1] + 1
            down[i] = down[i - 1]
        elif nums[i] < nums[i - 1]:
            down[i] = up[i - 1] + 1
            up[i] = up[i - 1]
        else:
            up[i] = up[i - 1]
            down[i] = down[i - 1]

    return max(up[-1], down[-1])


# Greedy
def wiggleMaxLengthGreedy(nums: List[int]) -> int:
    if len(nums) < 2:
        return len(nums)

    prev_diff = nums[1] - nums[0]
    count = 2 if prev_diff != 0 else 1

    for i in range(2, len(nums)):
        diff = nums[i] - nums[i - 1]
        if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
            count += 1
            prev_diff = diff

    return count


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |    DP       |      O(n)       |     O(n)     |
# |  Greedy     |      O(n)       |     O(1)     |
# |-------------|-----------------|--------------|

nums = [1, 7, 4, 9, 2, 5]
print(wiggleMaxLengthDP(nums))  # 6
print(wiggleMaxLengthGreedy(nums))  # 6

```

## 1186. Maximum Subarray Sum with One Deletion

-   [LeetCode](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/) | [LeetCode CH](https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/) (Medium)

-   Tags: array, dynamic programming
- [灵神：教你一步步思考动态规划 - 从记忆化搜索到递推](https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/solutions/2321829/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-hzz6))

```python title="1186. Maximum Subarray Sum with One Deletion - Python Solution"
from functools import cache
from math import inf
from typing import List


# DP - Kadane
def maximumSum(arr: List[int]) -> int:
    dp0 = arr[0]
    dp1 = 0
    res = dp0

    for i in range(1, len(arr)):
        dp1 = max(dp1 + arr[i], dp0)  # delete previous element or not
        dp0 = max(dp0, 0) + arr[i]  # delete current element or not
        res = max(res, dp0, dp1)  # update result

    return res


# DP - Memoization
def maximumSumMemo(arr: List[int]) -> int:
    @cache
    def dfs(i: int, j: int) -> int:
        if i < 0:
            return -inf
        if j == 0:
            return max(dfs(i - 1, 0), 0) + arr[i]
        return max(dfs(i - 1, 1) + arr[i], dfs(i - 1, 0))

    return max(max(dfs(i, 0), dfs(i, 1)) for i in range(len(arr)))


if __name__ == "__main__":
    arr = [1, -2, 0, 3]
    assert maximumSum(arr) == 4
    assert maximumSumMemo(arr) == 4

```
