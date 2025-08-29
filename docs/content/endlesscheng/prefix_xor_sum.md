---
comments: True
---

# Prefix XOR Sum

## Table of Contents

- [x] [1177. Can Make Palindrome from Substring](https://leetcode.cn/problems/can-make-palindrome-from-substring/) (Medium)
- [ ] [1371. Find the Longest Substring Containing Vowels in Even Counts](https://leetcode.cn/problems/find-the-longest-substring-containing-vowels-in-even-counts/) (Medium)
- [ ] [1542. Find Longest Awesome Substring](https://leetcode.cn/problems/find-longest-awesome-substring/) (Hard)
- [ ] [1915. Number of Wonderful Substrings](https://leetcode.cn/problems/number-of-wonderful-substrings/) (Medium)
- [ ] [2791. Count Paths That Can Form a Palindrome in a Tree](https://leetcode.cn/problems/count-paths-that-can-form-a-palindrome-in-a-tree/) (Hard)

## 1177. Can Make Palindrome from Substring

-   [LeetCode](https://leetcode.com/problems/can-make-palindrome-from-substring/) | [LeetCode CH](https://leetcode.cn/problems/can-make-palindrome-from-substring/) (Medium)

-   Tags: array, hash table, string, bit manipulation, prefix sum
```python title="1177. Can Make Palindrome from Substring - Python Solution"
from typing import List


# Prefix XOR Sum
def canMakePaliQueries(s: str, queries: List[List[int]]) -> List[bool]:
    sum = [[0] * 26]
    for c in s:
        sum.append(sum[-1].copy())
        sum[-1][ord(c) - ord("a")] ^= 1  # 奇数变偶数，偶数变奇数

    ans = []
    for left, right, k in queries:
        m = 0
        for sl, sr in zip(sum[left], sum[right + 1]):
            m += sr ^ sl
        ans.append(m // 2 <= k)
    return ans


if __name__ == "__main__":
    s = "abcda"
    queries = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]
    assert canMakePaliQueries(s, queries) == [True, False, False, True, True]

```

## 1371. Find the Longest Substring Containing Vowels in Even Counts

-   [LeetCode](https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/) | [LeetCode CH](https://leetcode.cn/problems/find-the-longest-substring-containing-vowels-in-even-counts/) (Medium)

-   Tags: hash table, string, bit manipulation, prefix sum
## 1542. Find Longest Awesome Substring

-   [LeetCode](https://leetcode.com/problems/find-longest-awesome-substring/) | [LeetCode CH](https://leetcode.cn/problems/find-longest-awesome-substring/) (Hard)

-   Tags: hash table, string, bit manipulation
## 1915. Number of Wonderful Substrings

-   [LeetCode](https://leetcode.com/problems/number-of-wonderful-substrings/) | [LeetCode CH](https://leetcode.cn/problems/number-of-wonderful-substrings/) (Medium)

-   Tags: hash table, string, bit manipulation, prefix sum
## 2791. Count Paths That Can Form a Palindrome in a Tree

-   [LeetCode](https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/) | [LeetCode CH](https://leetcode.cn/problems/count-paths-that-can-form-a-palindrome-in-a-tree/) (Hard)

-   Tags: dynamic programming, bit manipulation, tree, depth first search, bitmask
