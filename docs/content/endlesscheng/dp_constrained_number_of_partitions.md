---
comments: True
---

# DP Constrained Number of Partitions

- [ ] [410. Split Array Largest Sum](https://leetcode.cn/problems/split-array-largest-sum/) (Hard)
- [ ] [813. Largest Sum of Averages](https://leetcode.cn/problems/largest-sum-of-averages/) (Medium)
- [x] [1278. Palindrome Partitioning III](https://leetcode.cn/problems/palindrome-partitioning-iii/) (Hard)
- [x] [1745. Palindrome Partitioning IV](https://leetcode.cn/problems/palindrome-partitioning-iv/) (Hard)
- [ ] [1335. Minimum Difficulty of a Job Schedule](https://leetcode.cn/problems/minimum-difficulty-of-a-job-schedule/) (Hard)
- [ ] [1473. Paint House III](https://leetcode.cn/problems/paint-house-iii/) (Hard)
- [ ] [2209. Minimum White Tiles After Covering With Carpets](https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets/) (Hard)
- [ ] [1478. Allocate Mailboxes](https://leetcode.cn/problems/allocate-mailboxes/) (Hard)
- [ ] [1959. Minimum Total Space Wasted With K Resizing Operations](https://leetcode.cn/problems/minimum-total-space-wasted-with-k-resizing-operations/) (Medium)
- [ ] [2478. Number of Beautiful Partitions](https://leetcode.cn/problems/number-of-beautiful-partitions/) (Hard)
- [ ] [3077. Maximum Strength of K Disjoint Subarrays](https://leetcode.cn/problems/maximum-strength-of-k-disjoint-subarrays/) (Hard)
- [ ] [2911. Minimum Changes to Make K Semi-palindromes](https://leetcode.cn/problems/minimum-changes-to-make-k-semi-palindromes/) (Hard)
- [ ] [3117. Minimum Sum of Values by Dividing Array](https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/) (Hard)

## 410. Split Array Largest Sum

-   [LeetCode](https://leetcode.com/problems/split-array-largest-sum/) | [LeetCode CH](https://leetcode.cn/problems/split-array-largest-sum/) (Hard)

-   Tags: array, binary search, dynamic programming, greedy, prefix sum

## 813. Largest Sum of Averages

-   [LeetCode](https://leetcode.com/problems/largest-sum-of-averages/) | [LeetCode CH](https://leetcode.cn/problems/largest-sum-of-averages/) (Medium)

-   Tags: array, dynamic programming, prefix sum

## 1278. Palindrome Partitioning III

-   [LeetCode](https://leetcode.com/problems/palindrome-partitioning-iii/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-partitioning-iii/) (Hard)

-   Tags: string, dynamic programming

```python title="1278. Palindrome Partitioning III - Python Solution"
# DP
def palindromePartition(s: str, k: int) -> int:
    n = len(s)
    min_change = [[0] * n for _ in range(n)]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            min_change[i][j] = min_change[i + 1][j - 1] + (1 if s[i] != s[j] else 0)

    dp = min_change[0]
    for i in range(1, k):
        for right in range(n - k + i, i - 1, -1):
            dp[right] = min(
                dp[left - 1] + min_change[left][right] for left in range(i, right + 1)
            )

    return dp[-1]


s = "aabbc"
k = 3
print(palindromePartition(s, k))  # 0

```

## 1745. Palindrome Partitioning IV

-   [LeetCode](https://leetcode.com/problems/palindrome-partitioning-iv/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-partitioning-iv/) (Hard)

-   Tags: string, dynamic programming

```python title="1745. Palindrome Partitioning IV - Python Solution"
# DP
def checkPartitioning(s: str) -> bool:
    def palidrome_partition(s, k):
        n = len(s)
        min_change = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                min_change[i][j] = min_change[i + 1][j - 1] + (1 if s[i] != s[j] else 0)

        dp = min_change[0]

        for i in range(1, k):
            for right in range(n - k + i, i - 1, -1):
                dp[right] = min(
                    dp[left - 1] + min_change[left][right]
                    for left in range(i, right + 1)
                )

        return dp[-1]

    return palidrome_partition(s, 3) == 0


s = "abcbdd"
print(checkPartitioning(s))  # True

```

## 1335. Minimum Difficulty of a Job Schedule

-   [LeetCode](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/) | [LeetCode CH](https://leetcode.cn/problems/minimum-difficulty-of-a-job-schedule/) (Hard)

-   Tags: array, dynamic programming

## 1473. Paint House III

-   [LeetCode](https://leetcode.com/problems/paint-house-iii/) | [LeetCode CH](https://leetcode.cn/problems/paint-house-iii/) (Hard)

-   Tags: array, dynamic programming

## 2209. Minimum White Tiles After Covering With Carpets

-   [LeetCode](https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/) | [LeetCode CH](https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets/) (Hard)

-   Tags: string, dynamic programming, prefix sum

## 1478. Allocate Mailboxes

-   [LeetCode](https://leetcode.com/problems/allocate-mailboxes/) | [LeetCode CH](https://leetcode.cn/problems/allocate-mailboxes/) (Hard)

-   Tags: array, math, dynamic programming, sorting

## 1959. Minimum Total Space Wasted With K Resizing Operations

-   [LeetCode](https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/) | [LeetCode CH](https://leetcode.cn/problems/minimum-total-space-wasted-with-k-resizing-operations/) (Medium)

-   Tags: array, dynamic programming

## 2478. Number of Beautiful Partitions

-   [LeetCode](https://leetcode.com/problems/number-of-beautiful-partitions/) | [LeetCode CH](https://leetcode.cn/problems/number-of-beautiful-partitions/) (Hard)

-   Tags: string, dynamic programming

## 3077. Maximum Strength of K Disjoint Subarrays

-   [LeetCode](https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/maximum-strength-of-k-disjoint-subarrays/) (Hard)

-   Tags: array, dynamic programming, prefix sum

## 2911. Minimum Changes to Make K Semi-palindromes

-   [LeetCode](https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/) | [LeetCode CH](https://leetcode.cn/problems/minimum-changes-to-make-k-semi-palindromes/) (Hard)

-   Tags: two pointers, string, dynamic programming

## 3117. Minimum Sum of Values by Dividing Array

-   [LeetCode](https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/) | [LeetCode CH](https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/) (Hard)

-   Tags: array, binary search, dynamic programming, bit manipulation, segment tree, queue
