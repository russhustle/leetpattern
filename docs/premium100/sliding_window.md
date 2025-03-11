---
comments: True
---

# Sliding Window

- [x] [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.cn/problems/longest-substring-with-at-most-two-distinct-characters/) (Medium) 👑
- [x] [340. Longest Substring with At Most K Distinct Characters](https://leetcode.cn/problems/longest-substring-with-at-most-k-distinct-characters/) (Medium) 👑
- [ ] [487. Max Consecutive Ones II](https://leetcode.cn/problems/max-consecutive-ones-ii/) (Medium) 👑
- [ ] [1100. Find K-Length Substrings With No Repeated Characters](https://leetcode.cn/problems/find-k-length-substrings-with-no-repeated-characters/) (Medium) 👑

## 159. Longest Substring with At Most Two Distinct Characters

-   [LeetCode](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) | [LeetCode CH](https://leetcode.cn/problems/longest-substring-with-at-most-two-distinct-characters/) (Medium)

-   Tags: hash table, string, sliding window
-   Prerequisite: 3. Longest Substring Without Repeating Characters

```python title="159. Longest Substring with At Most Two Distinct Characters - Python Solution"
from collections import defaultdict


# Sliding Window - Variable
def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    n = len(s)
    if n <= 2:
        return n

    window = defaultdict(int)
    left, res = 0, 0

    for right in range(n):
        window[s[right]] += 1

        while len(window) > 2:
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

        res = max(res, right - left + 1)

    return res


s = "ccaabbb"
assert lengthOfLongestSubstringTwoDistinct(s) == 5

```

## 340. Longest Substring with At Most K Distinct Characters

-   [LeetCode](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) | [LeetCode CH](https://leetcode.cn/problems/longest-substring-with-at-most-k-distinct-characters/) (Medium)

-   Tags: hash table, string, sliding window

```python title="340. Longest Substring with At Most K Distinct Characters - Python Solution"
from collections import defaultdict


# Sliding Window Variable
def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    n = len(s)
    if n <= k:
        return n

    window = defaultdict(int)
    left, res = 0, 0

    for right in range(n):
        window[s[right]] += 1
        while len(window) > k:
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        res = max(res, right - left + 1)

    return res


s = "eceba"
k = 2
assert lengthOfLongestSubstringKDistinct(s, k) == 3

```

## 487. Max Consecutive Ones II

-   [LeetCode](https://leetcode.com/problems/max-consecutive-ones-ii/) | [LeetCode CH](https://leetcode.cn/problems/max-consecutive-ones-ii/) (Medium)

-   Tags: array, dynamic programming, sliding window

## 1100. Find K-Length Substrings With No Repeated Characters

-   [LeetCode](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/) | [LeetCode CH](https://leetcode.cn/problems/find-k-length-substrings-with-no-repeated-characters/) (Medium)

-   Tags: hash table, string, sliding window
