---
comments: True
---

# String Suffix Array

## Table of Contents

- [ ] [1163. Last Substring in Lexicographical Order](https://leetcode.cn/problems/last-substring-in-lexicographical-order/) (Hard)
- [ ] [1754. Largest Merge Of Two Strings](https://leetcode.cn/problems/largest-merge-of-two-strings/) (Medium)
- [x] [2904. Shortest and Lexicographically Smallest Beautiful String](https://leetcode.cn/problems/shortest-and-lexicographically-smallest-beautiful-string/) (Medium)
- [ ] [3213. Construct String with Minimum Cost](https://leetcode.cn/problems/construct-string-with-minimum-cost/) (Hard)
- [ ] [1044. Longest Duplicate Substring](https://leetcode.cn/problems/longest-duplicate-substring/) (Hard)
- [x] [718. Maximum Length of Repeated Subarray](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/) (Medium)
- [ ] [1923. Longest Common Subpath](https://leetcode.cn/problems/longest-common-subpath/) (Hard)
- [ ] [1408. String Matching in an Array](https://leetcode.cn/problems/string-matching-in-an-array/) (Easy)
- [ ] [3076. Shortest Uncommon Substring in an Array](https://leetcode.cn/problems/shortest-uncommon-substring-in-an-array/) (Medium)
- [ ] [1316. Distinct Echo Substrings](https://leetcode.cn/problems/distinct-echo-substrings/) (Hard)
- [ ] [3388. Count Beautiful Splits in an Array](https://leetcode.cn/problems/count-beautiful-splits-in-an-array/) (Medium)
- [ ] [2564. Substring XOR Queries](https://leetcode.cn/problems/substring-xor-queries/) (Medium)
- [ ] [1698. Number of Distinct Substrings in a String](https://leetcode.cn/problems/number-of-distinct-substrings-in-a-string/) (Medium) 👑
- [ ] [1062. Longest Repeating Substring](https://leetcode.cn/problems/longest-repeating-substring/) (Medium) 👑
- [ ] [3135. Equalize Strings by Adding or Removing Characters at Ends](https://leetcode.cn/problems/equalize-strings-by-adding-or-removing-characters-at-ends/) (Medium) 👑

## 1163. Last Substring in Lexicographical Order

-   [LeetCode](https://leetcode.com/problems/last-substring-in-lexicographical-order/) | [LeetCode CH](https://leetcode.cn/problems/last-substring-in-lexicographical-order/) (Hard)

-   Tags: two pointers, string
## 1754. Largest Merge Of Two Strings

-   [LeetCode](https://leetcode.com/problems/largest-merge-of-two-strings/) | [LeetCode CH](https://leetcode.cn/problems/largest-merge-of-two-strings/) (Medium)

-   Tags: two pointers, string, greedy
## 2904. Shortest and Lexicographically Smallest Beautiful String

-   [LeetCode](https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/) | [LeetCode CH](https://leetcode.cn/problems/shortest-and-lexicographically-smallest-beautiful-string/) (Medium)

-   Tags: string, sliding window
```python title="2904. Shortest and Lexicographically Smallest Beautiful String - Python Solution"
# Sliding Window Variable Size
def shortestBeautifulSubstring(s: str, k: int) -> str:
    n = len(s)
    left = 0
    oneCount = 0
    minLen = float("inf")
    res = ""

    for right in range(n):
        if s[right] == "1":
            oneCount += 1

        while oneCount == k:
            size = right - left + 1

            if size < minLen:
                minLen = size
                res = s[left : right + 1]
            elif size == minLen:
                res = min(res, s[left : right + 1])

            if s[left] == "1":
                oneCount -= 1
            left += 1

    return res


s = "100011001"
k = 3
print(shortestBeautifulSubstring(s, k))  # 11001

```

## 3213. Construct String with Minimum Cost

-   [LeetCode](https://leetcode.com/problems/construct-string-with-minimum-cost/) | [LeetCode CH](https://leetcode.cn/problems/construct-string-with-minimum-cost/) (Hard)

-   Tags: array, string, dynamic programming, suffix array
## 1044. Longest Duplicate Substring

-   [LeetCode](https://leetcode.com/problems/longest-duplicate-substring/) | [LeetCode CH](https://leetcode.cn/problems/longest-duplicate-substring/) (Hard)

-   Tags: string, binary search, sliding window, rolling hash, suffix array, hash function
## 718. Maximum Length of Repeated Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/) (Medium)

-   Tags: array, binary search, dynamic programming, sliding window, rolling hash, hash function
```python title="718. Maximum Length of Repeated Subarray - Python Solution"
from typing import List


def findLength(nums1: List[int], nums2: List[int]) -> int:
    m = len(nums1)
    n = len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            if length < dp[i][j]:
                length = dp[i][j]

    return length


print(findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))  # 3

```

## 1923. Longest Common Subpath

-   [LeetCode](https://leetcode.com/problems/longest-common-subpath/) | [LeetCode CH](https://leetcode.cn/problems/longest-common-subpath/) (Hard)

-   Tags: array, binary search, rolling hash, suffix array, hash function
## 1408. String Matching in an Array

-   [LeetCode](https://leetcode.com/problems/string-matching-in-an-array/) | [LeetCode CH](https://leetcode.cn/problems/string-matching-in-an-array/) (Easy)

-   Tags: array, string, string matching
## 3076. Shortest Uncommon Substring in an Array

-   [LeetCode](https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/) | [LeetCode CH](https://leetcode.cn/problems/shortest-uncommon-substring-in-an-array/) (Medium)

-   Tags: array, hash table, string, trie
## 1316. Distinct Echo Substrings

-   [LeetCode](https://leetcode.com/problems/distinct-echo-substrings/) | [LeetCode CH](https://leetcode.cn/problems/distinct-echo-substrings/) (Hard)

-   Tags: string, trie, rolling hash, hash function
## 3388. Count Beautiful Splits in an Array

-   [LeetCode](https://leetcode.com/problems/count-beautiful-splits-in-an-array/) | [LeetCode CH](https://leetcode.cn/problems/count-beautiful-splits-in-an-array/) (Medium)

-   Tags: array, dynamic programming
## 2564. Substring XOR Queries

-   [LeetCode](https://leetcode.com/problems/substring-xor-queries/) | [LeetCode CH](https://leetcode.cn/problems/substring-xor-queries/) (Medium)

-   Tags: array, hash table, string, bit manipulation
## 1698. Number of Distinct Substrings in a String

-   [LeetCode](https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/) | [LeetCode CH](https://leetcode.cn/problems/number-of-distinct-substrings-in-a-string/) (Medium)

-   Tags: string, trie, rolling hash, suffix array, hash function
## 1062. Longest Repeating Substring

-   [LeetCode](https://leetcode.com/problems/longest-repeating-substring/) | [LeetCode CH](https://leetcode.cn/problems/longest-repeating-substring/) (Medium)

-   Tags: string, binary search, dynamic programming, rolling hash, suffix array, hash function
## 3135. Equalize Strings by Adding or Removing Characters at Ends

-   [LeetCode](https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/) | [LeetCode CH](https://leetcode.cn/problems/equalize-strings-by-adding-or-removing-characters-at-ends/) (Medium)

-   Tags: string, binary search, dynamic programming, sliding window, hash function
