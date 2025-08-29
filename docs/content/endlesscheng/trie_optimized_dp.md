---
comments: True
---

# Trie Optimized DP

## Table of Contents

- [x] [139. Word Break](https://leetcode.cn/problems/word-break/) (Medium)
- [ ] [140. Word Break II](https://leetcode.cn/problems/word-break-ii/) (Hard)
- [ ] [472. Concatenated Words](https://leetcode.cn/problems/concatenated-words/) (Hard)
- [ ] [2977. Minimum Cost to Convert String II](https://leetcode.cn/problems/minimum-cost-to-convert-string-ii/) (Hard)

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

## 140. Word Break II

-   [LeetCode](https://leetcode.com/problems/word-break-ii/) | [LeetCode CH](https://leetcode.cn/problems/word-break-ii/) (Hard)

-   Tags: array, hash table, string, dynamic programming, backtracking, trie, memoization
## 472. Concatenated Words

-   [LeetCode](https://leetcode.com/problems/concatenated-words/) | [LeetCode CH](https://leetcode.cn/problems/concatenated-words/) (Hard)

-   Tags: array, string, dynamic programming, depth first search, trie
## 2977. Minimum Cost to Convert String II

-   [LeetCode](https://leetcode.com/problems/minimum-cost-to-convert-string-ii/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-to-convert-string-ii/) (Hard)

-   Tags: array, string, dynamic programming, graph, trie, shortest path
