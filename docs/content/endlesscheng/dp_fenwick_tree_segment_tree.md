---
comments: True
---

# DP Fenwick Tree Segment Tree

## Table of Contents

- [x] [1626. Best Team With No Conflicts](https://leetcode.cn/problems/best-team-with-no-conflicts/) (Medium)
- [ ] [2407. Longest Increasing Subsequence II](https://leetcode.cn/problems/longest-increasing-subsequence-ii/) (Hard)
- [ ] [2770. Maximum Number of Jumps to Reach the Last Index](https://leetcode.cn/problems/maximum-number-of-jumps-to-reach-the-last-index/) (Medium)
- [ ] [2926. Maximum Balanced Subsequence Sum](https://leetcode.cn/problems/maximum-balanced-subsequence-sum/) (Hard)
- [ ] [2916. Subarrays Distinct Element Sum of Squares II](https://leetcode.cn/problems/subarrays-distinct-element-sum-of-squares-ii/) (Hard)
- [ ] [3410. Maximize Subarray Sum After Removing All Occurrences of One Element](https://leetcode.cn/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/) (Hard)

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

## 2407. Longest Increasing Subsequence II

-   [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence-ii/) | [LeetCode CH](https://leetcode.cn/problems/longest-increasing-subsequence-ii/) (Hard)

-   Tags: array, divide and conquer, dynamic programming, binary indexed tree, segment tree, queue, monotonic queue
## 2770. Maximum Number of Jumps to Reach the Last Index

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-jumps-to-reach-the-last-index/) (Medium)

-   Tags: array, dynamic programming
## 2926. Maximum Balanced Subsequence Sum

-   [LeetCode](https://leetcode.com/problems/maximum-balanced-subsequence-sum/) | [LeetCode CH](https://leetcode.cn/problems/maximum-balanced-subsequence-sum/) (Hard)

-   Tags: array, binary search, dynamic programming, binary indexed tree, segment tree
## 2916. Subarrays Distinct Element Sum of Squares II

-   [LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/) | [LeetCode CH](https://leetcode.cn/problems/subarrays-distinct-element-sum-of-squares-ii/) (Hard)

-   Tags: array, dynamic programming, binary indexed tree, segment tree
## 3410. Maximize Subarray Sum After Removing All Occurrences of One Element

-   [LeetCode](https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/) | [LeetCode CH](https://leetcode.cn/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/) (Hard)

-   Tags: array, dynamic programming, segment tree
