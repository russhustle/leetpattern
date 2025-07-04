---
comments: True
---

# DP 1D

## Table of Contents

- [ ] [2944. Minimum Number of Coins for Fruits](https://leetcode.cn/problems/minimum-number-of-coins-for-fruits/) (Medium)
- [x] [2140. Solving Questions With Brainpower](https://leetcode.cn/problems/solving-questions-with-brainpower/) (Medium)
- [x] [983. Minimum Cost For Tickets](https://leetcode.cn/problems/minimum-cost-for-tickets/) (Medium)
- [ ] [2901. Longest Unequal Adjacent Groups Subsequence II](https://leetcode.cn/problems/longest-unequal-adjacent-groups-subsequence-ii/) (Medium)
- [ ] [3144. Minimum Substring Partition of Equal Character Frequency](https://leetcode.cn/problems/minimum-substring-partition-of-equal-character-frequency/) (Medium)
- [ ] [871. Minimum Number of Refueling Stops](https://leetcode.cn/problems/minimum-number-of-refueling-stops/) (Hard)
- [ ] [2896. Apply Operations to Make Two Strings Equal](https://leetcode.cn/problems/apply-operations-to-make-two-strings-equal/) (Medium)
- [ ] [2167. Minimum Time to Remove All Cars Containing Illegal Goods](https://leetcode.cn/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/) (Hard)
- [ ] [2188. Minimum Time to Finish the Race](https://leetcode.cn/problems/minimum-time-to-finish-the-race/) (Hard)
- [ ] [3389. Minimum Operations to Make Character Frequencies Equal](https://leetcode.cn/problems/minimum-operations-to-make-character-frequencies-equal/) (Hard)
- [ ] [3205. Maximum Array Hopping Score I](https://leetcode.cn/problems/maximum-array-hopping-score-i/) (Medium) 👑
- [ ] [1259. Handshakes That Don't Cross](https://leetcode.cn/problems/handshakes-that-dont-cross/) (Hard) 👑

## 2944. Minimum Number of Coins for Fruits

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-coins-for-fruits/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-coins-for-fruits/) (Medium)

-   Tags: array, dynamic programming, queue, heap priority queue, monotonic queue
## 2140. Solving Questions With Brainpower

-   [LeetCode](https://leetcode.com/problems/solving-questions-with-brainpower/) | [LeetCode CH](https://leetcode.cn/problems/solving-questions-with-brainpower/) (Medium)

-   Tags: array, dynamic programming

```python title="2140. Solving Questions With Brainpower - Python Solution"
from functools import cache
from typing import List


# Memoization
def mostPoints(questions: List[List[int]]) -> int:
    @cache
    def dfs(i: int) -> int:
        if i >= len(questions):
            return 0
        return max(dfs(i + 1), dfs(i + questions[i][1] + 1) + questions[i][0])

    return dfs(0)


if __name__ == "__main__":
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    print(mostPoints(questions))  # 5

```

## 983. Minimum Cost For Tickets

-   [LeetCode](https://leetcode.com/problems/minimum-cost-for-tickets/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-for-tickets/) (Medium)

-   Tags: array, dynamic programming

```python title="983. Minimum Cost For Tickets - Python Solution"
from typing import List


# DP
def mincostTickets(days: List[int], costs: List[int]) -> int:
    last = days[-1]
    dayset = set(days)
    dp = [0 for _ in range(last + 1)]

    for i in range(1, last + 1):
        if i not in dayset:
            dp[i] = dp[i - 1]
        else:
            dp[i] = min(
                dp[i - 1] + costs[0],
                dp[max(0, i - 7)] + costs[1],
                dp[max(0, i - 30)] + costs[2],
            )

    return dp[last]


days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(mincostTickets(days, costs))  # 11

```

## 2901. Longest Unequal Adjacent Groups Subsequence II

-   [LeetCode](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/) | [LeetCode CH](https://leetcode.cn/problems/longest-unequal-adjacent-groups-subsequence-ii/) (Medium)

-   Tags: array, string, dynamic programming
## 3144. Minimum Substring Partition of Equal Character Frequency

-   [LeetCode](https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/) | [LeetCode CH](https://leetcode.cn/problems/minimum-substring-partition-of-equal-character-frequency/) (Medium)

-   Tags: hash table, string, dynamic programming, counting
## 871. Minimum Number of Refueling Stops

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-refueling-stops/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-refueling-stops/) (Hard)

-   Tags: array, dynamic programming, greedy, heap priority queue
## 2896. Apply Operations to Make Two Strings Equal

-   [LeetCode](https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/) | [LeetCode CH](https://leetcode.cn/problems/apply-operations-to-make-two-strings-equal/) (Medium)

-   Tags: string, dynamic programming
## 2167. Minimum Time to Remove All Cars Containing Illegal Goods

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/) (Hard)

-   Tags: string, dynamic programming
## 2188. Minimum Time to Finish the Race

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-finish-the-race/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-finish-the-race/) (Hard)

-   Tags: array, dynamic programming
## 3389. Minimum Operations to Make Character Frequencies Equal

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-make-character-frequencies-equal/) (Hard)

-   Tags: hash table, string, dynamic programming, counting, enumeration
## 3205. Maximum Array Hopping Score I

-   [LeetCode](https://leetcode.com/problems/maximum-array-hopping-score-i/) | [LeetCode CH](https://leetcode.cn/problems/maximum-array-hopping-score-i/) (Medium)

-   Tags: array, dynamic programming, stack, greedy, monotonic stack
## 1259. Handshakes That Don't Cross

-   [LeetCode](https://leetcode.com/problems/handshakes-that-dont-cross/) | [LeetCode CH](https://leetcode.cn/problems/handshakes-that-dont-cross/) (Hard)

-   Tags: math, dynamic programming
