---
comments: True
---

# DP LIS Advanced

## Table of Contents

- [x] [1626. Best Team With No Conflicts](https://leetcode.cn/problems/best-team-with-no-conflicts/) (Medium)
- [x] [673. Number of Longest Increasing Subsequence](https://leetcode.cn/problems/number-of-longest-increasing-subsequence/) (Medium)
- [x] [354. Russian Doll Envelopes](https://leetcode.cn/problems/russian-doll-envelopes/) (Hard)
- [ ] [1691. Maximum Height by Stacking Cuboids ](https://leetcode.cn/problems/maximum-height-by-stacking-cuboids/) (Hard)
- [x] [960. Delete Columns to Make Sorted III](https://leetcode.cn/problems/delete-columns-to-make-sorted-iii/) (Hard)
- [ ] [2407. Longest Increasing Subsequence II](https://leetcode.cn/problems/longest-increasing-subsequence-ii/) (Hard)
- [ ] [1187. Make Array Strictly Increasing](https://leetcode.cn/problems/make-array-strictly-increasing/) (Hard)
- [ ] [1713. Minimum Operations to Make a Subsequence](https://leetcode.cn/problems/minimum-operations-to-make-a-subsequence/) (Hard)
- [ ] [3288. Length of the Longest Increasing Path](https://leetcode.cn/problems/length-of-the-longest-increasing-path/) (Hard)
- [ ] [368. Largest Divisible Subset](https://leetcode.cn/problems/largest-divisible-subset/) (Medium)

## 1626. Best Team With No Conflicts

-   [LeetCode](https://leetcode.com/problems/best-team-with-no-conflicts/) | [LeetCode CH](https://leetcode.cn/problems/best-team-with-no-conflicts/) (Medium)

-   Tags: array, dynamic programming, sorting

```python title="1626. Best Team With No Conflicts - Python Solution"
from typing import List


# DP - LIS
def bestTeamScore(scores: List[int], ages: List[int]) -> int:
    n = len(scores)
    pairs = sorted(zip(scores, ages))  # sort
    dp = [0 for _ in range(n)]

    # LIS
    for i in range(n):
        for j in range(i):
            if pairs[i][1] >= pairs[j][1]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += pairs[i][0]

    return max(dp)


if __name__ == "__main__":
    assert bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]) == 34
    assert bestTeamScore([4, 5, 6, 5], [2, 1, 2, 1]) == 16

```

## 673. Number of Longest Increasing Subsequence

-   [LeetCode](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/number-of-longest-increasing-subsequence/) (Medium)

-   Tags: array, dynamic programming, binary indexed tree, segment tree

```python title="673. Number of Longest Increasing Subsequence - Python Solution"
from typing import List


# DP - LIS
def findNumberOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0

    n = len(nums)
    dp = [1 for _ in range(n)]
    counts = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    counts[i] = counts[j]
                elif dp[j] + 1 == dp[i]:
                    counts[i] += counts[j]

    longest = max(dp)
    return sum(c for i, c in enumerate(counts) if dp[i] == longest)


nums = [1, 3, 5, 4, 7]
print(findNumberOfLIS(nums))  # 2

```

## 354. Russian Doll Envelopes

-   [LeetCode](https://leetcode.com/problems/russian-doll-envelopes/) | [LeetCode CH](https://leetcode.cn/problems/russian-doll-envelopes/) (Hard)

-   Tags: array, binary search, dynamic programming, sorting

```python title="354. Russian Doll Envelopes - Python Solution"
from typing import List


# DP - LIS
def maxEnvelopes(envelopes: List[List[int]]) -> int:
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []

    for w, h in envelopes:
        left, right = 0, len(dp)
        while left < right:
            mid = left + (right - left) // 2
            if dp[mid][1] < h:
                left = mid + 1
            else:
                right = mid
        if right == len(dp):
            dp.append((w, h))
        else:
            dp[right] = (w, h)

    return len(dp)


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
print(maxEnvelopes(envelopes))  # 3

```

## 1691. Maximum Height by Stacking Cuboids

-   [LeetCode](https://leetcode.com/problems/maximum-height-by-stacking-cuboids/) | [LeetCode CH](https://leetcode.cn/problems/maximum-height-by-stacking-cuboids/) (Hard)

-   Tags: array, dynamic programming, sorting
## 960. Delete Columns to Make Sorted III

-   [LeetCode](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/) | [LeetCode CH](https://leetcode.cn/problems/delete-columns-to-make-sorted-iii/) (Hard)

-   Tags: array, string, dynamic programming

```python title="960. Delete Columns to Make Sorted III - Python Solution"
from typing import List


# DP - LIS
def minDeletionSize(strs: List[str]) -> int:
    if not strs:
        return 0

    n = len(strs[0])
    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if all(row[j] <= row[i] for row in strs):
                dp[i] = max(dp[i], dp[j] + 1)

    return n - max(dp)

```

## 2407. Longest Increasing Subsequence II

-   [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence-ii/) | [LeetCode CH](https://leetcode.cn/problems/longest-increasing-subsequence-ii/) (Hard)

-   Tags: array, divide and conquer, dynamic programming, binary indexed tree, segment tree, queue, monotonic queue
## 1187. Make Array Strictly Increasing

-   [LeetCode](https://leetcode.com/problems/make-array-strictly-increasing/) | [LeetCode CH](https://leetcode.cn/problems/make-array-strictly-increasing/) (Hard)

-   Tags: array, binary search, dynamic programming, sorting
## 1713. Minimum Operations to Make a Subsequence

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-make-a-subsequence/) (Hard)

-   Tags: array, hash table, binary search, greedy
## 3288. Length of the Longest Increasing Path

-   [LeetCode](https://leetcode.com/problems/length-of-the-longest-increasing-path/) | [LeetCode CH](https://leetcode.cn/problems/length-of-the-longest-increasing-path/) (Hard)

-   Tags: array, binary search, sorting
## 368. Largest Divisible Subset

-   [LeetCode](https://leetcode.com/problems/largest-divisible-subset/) | [LeetCode CH](https://leetcode.cn/problems/largest-divisible-subset/) (Medium)

-   Tags: array, math, dynamic programming, sorting
