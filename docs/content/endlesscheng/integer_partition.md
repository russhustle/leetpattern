---
comments: True
---

# Integer Partition

## Table of Contents

- [x] [343. Integer Break](https://leetcode.cn/problems/integer-break/) (Medium)
- [ ] [1808. Maximize Number of Nice Divisors](https://leetcode.cn/problems/maximize-number-of-nice-divisors/) (Hard)

## 343. Integer Break

-   [LeetCode](https://leetcode.com/problems/integer-break/) | [LeetCode CH](https://leetcode.cn/problems/integer-break/) (Medium)

-   Tags: math, dynamic programming
-   Return the maximum product of the integer after breaking it into at least two positive integers.
-   `dp[i]` stores the maximum product of the integer `i`.
-   Formula: `dp[i] = max(dp[i - j] * j, (i - j) * j)`

|    dp    |   3    |   4    |   5    |   6    |    7    |    8     |
| :------: | :----: | :----: | :----: | :----: | :-----: | :------: |
|    2     | 2\*1=2 | 2\*2=4 | 2\*3=6 | 2\*4=8 | 2\*5=10 | 2\*6=12  |
| dp[2]=1  | 1\*1=2 | 1\*2=2 | 1\*3=3 | 1\*4=4 | 1\*5=5  |  1\*6=6  |
|    3     |        | 3\*1=3 | 3\*2=6 | 3\*3=9 | 3\*4=12 | 3\*5=15  |
| dp[3]=2  |        | 2\*1=2 | 2\*2=4 | 2\*3=6 | 2\*4=8  | 2\*5=10  |
|    4     |        |        | 4\*1=4 | 4\*2=8 | 4\*3=12 | 4\*4=16  |
| dp[4]=4  |        |        | 4\*1=4 | 4\*2=8 | 4\*3=12 | 4\*4=16  |
|    5     |        |        |        | 5\*1=5 | 5\*2=10 | 5\*3=15  |
| dp[5]=6  |        |        |        | 6\*1=6 | 6\*2=12 | 6\*3=18  |
|    6     |        |        |        |        | 6\*1=6  | 6\*2=12  |
| dp[6]=9  |        |        |        |        | 9\*1=9  | 9\*2=18  |
|    7     |        |        |        |        |         |  7\*1=7  |
| dp[7]=12 |        |        |        |        |         | 12\*1=12 |
| `dp[n]`  |   2    |   4    |   6    |   9    |   12    |    18    |

```python title="343. Integer Break - Python Solution"
def integerBreak(n: int) -> int:
    dp = [0 for _ in range(n + 1)]
    dp[2] = 1

    for i in range(3, n + 1):
        for j in range(2, i):
            dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)

    return dp[n]


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |    DP       |      O(n^2)     |     O(n)     |
# |-------------|-----------------|--------------|

n = 8
print(integerBreak(n))  # 18

```

## 1808. Maximize Number of Nice Divisors

-   [LeetCode](https://leetcode.com/problems/maximize-number-of-nice-divisors/) | [LeetCode CH](https://leetcode.cn/problems/maximize-number-of-nice-divisors/) (Hard)

-   Tags: math, recursion, number theory
