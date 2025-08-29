---
comments: True
---

# DP LIS

## Table of Contents

- [x] [300. Longest Increasing Subsequence](https://leetcode.cn/problems/longest-increasing-subsequence/) (Medium)
- [x] [673. Number of Longest Increasing Subsequence](https://leetcode.cn/problems/number-of-longest-increasing-subsequence/) (Medium)
- [x] [354. Russian Doll Envelopes](https://leetcode.cn/problems/russian-doll-envelopes/) (Hard)
- [x] [960. Delete Columns to Make Sorted III](https://leetcode.cn/problems/delete-columns-to-make-sorted-iii/) (Hard)
- [x] [1671. Minimum Number of Removals to Make Mountain Array](https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/) (Hard)
- [x] [941. Valid Mountain Array](https://leetcode.cn/problems/valid-mountain-array/) (Easy)
- [x] [845. Longest Mountain in Array](https://leetcode.cn/problems/longest-mountain-in-array/) (Medium)

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

## 941. Valid Mountain Array

-   [LeetCode](https://leetcode.com/problems/valid-mountain-array/) | [LeetCode CH](https://leetcode.cn/problems/valid-mountain-array/) (Easy)

-   Tags: array
```python title="941. Valid Mountain Array - Python Solution"
from typing import List


# Array
def validMountainArray(arr: List[int]) -> bool:
    n = len(arr)
    i = 0

    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        return False

    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1


# Left Right Pointers
def validMountainArrayLP(arr: List[int]) -> bool:
    n = len(arr)

    if n < 3:
        return False

    left, right = 0, n - 1

    while left < n - 1 and arr[left] < arr[left + 1]:
        left += 1

    while right > 0 and arr[right] < arr[right - 1]:
        right -= 1

    return 0 < left == right < n - 1


arr = [0, 3, 2, 1]
print(validMountainArray(arr))  # True
print(validMountainArrayLP(arr))  # True

```

## 845. Longest Mountain in Array

-   [LeetCode](https://leetcode.com/problems/longest-mountain-in-array/) | [LeetCode CH](https://leetcode.cn/problems/longest-mountain-in-array/) (Medium)

-   Tags: array, two pointers, dynamic programming, enumeration
```python title="845. Longest Mountain in Array - Python Solution"
from typing import List


# Left Right Pointers
def longestMountain(arr: List[int]) -> int:
    n = len(arr)
    res = 0
    left = 0

    while left < n:
        right = left

        if right < n - 1 and arr[right] < arr[right + 1]:
            while right < n - 1 and arr[right] < arr[right + 1]:
                right += 1

            if right < n - 1 and arr[right] > arr[right + 1]:
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                res = max(res, right - left + 1)

        left = max(right, left + 1)

    return res


arr = [2, 1, 4, 7, 3, 2, 5]
print(longestMountain(arr))  # 5

```
