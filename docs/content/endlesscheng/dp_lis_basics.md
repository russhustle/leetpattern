---
comments: True
---

# DP LIS Basics

## Table of Contents

- [x] [300. Longest Increasing Subsequence](https://leetcode.cn/problems/longest-increasing-subsequence/) (Medium)
- [x] [2826. Sorting Three Groups](https://leetcode.cn/problems/sorting-three-groups/) (Medium)
- [x] [1671. Minimum Number of Removals to Make Mountain Array](https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/) (Hard)
- [ ] [1964. Find the Longest Valid Obstacle Course at Each Position](https://leetcode.cn/problems/find-the-longest-valid-obstacle-course-at-each-position/) (Hard)
- [ ] [2111. Minimum Operations to Make the Array K-Increasing](https://leetcode.cn/problems/minimum-operations-to-make-the-array-k-increasing/) (Hard)

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

## 1671. Minimum Number of Removals to Make Mountain Array

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/) (Hard)

-   Tags: array, binary search, dynamic programming, greedy
```python title="1671. Minimum Number of Removals to Make Mountain Array - Python Solution"
from typing import List


# DP - LIS
def minimumMountainRemovals(nums: List[int]) -> int:
    n = len(nums)
    lis = [1 for _ in range(n)]
    lds = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] > nums[j]:
                lds[i] = max(lds[i], lds[j] + 1)

    maxLen = 0
    for i in range(1, n - 1):
        if lis[i] > 1 and lds[i] > 1:
            maxLen = max(maxLen, lis[i] + lds[i] - 1)

    return n - maxLen


nums = [2, 1, 1, 5, 6, 2, 3, 1]
print(minimumMountainRemovals(nums))  # 3

```

## 1964. Find the Longest Valid Obstacle Course at Each Position

-   [LeetCode](https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/) | [LeetCode CH](https://leetcode.cn/problems/find-the-longest-valid-obstacle-course-at-each-position/) (Hard)

-   Tags: array, binary search, binary indexed tree
## 2111. Minimum Operations to Make the Array K-Increasing

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-make-the-array-k-increasing/) (Hard)

-   Tags: array, binary search
