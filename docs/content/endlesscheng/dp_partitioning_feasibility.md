---
comments: True
---

# DP Partitioning Feasibility

## Table of Contents

- [ ] [2369. Check if There is a Valid Partition For The Array](https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/) (Medium)
- [x] [139. Word Break](https://leetcode.cn/problems/word-break/) (Medium)

## 2369. Check if There is a Valid Partition For The Array

-   [LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/) | [LeetCode CH](https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/) (Medium)

-   Tags: array, dynamic programming
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
