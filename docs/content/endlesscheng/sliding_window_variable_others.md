---
comments: True
---

# Sliding Window Variable Others

## Table of Contents

- [ ] [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) (Medium)
- [ ] [825. Friends Of Appropriate Ages](https://leetcode.cn/problems/friends-of-appropriate-ages/) (Medium)
- [ ] [2401. Longest Nice Subarray](https://leetcode.cn/problems/longest-nice-subarray/) (Medium)
- [ ] [1156. Swap For Longest Repeated Character Substring](https://leetcode.cn/problems/swap-for-longest-repeated-character-substring/) (Medium)
- [x] [424. Longest Repeating Character Replacement](https://leetcode.cn/problems/longest-repeating-character-replacement/) (Medium)
- [x] [438. Find All Anagrams in a String](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) (Medium)
- [ ] [1712. Ways to Split Array Into Three Subarrays](https://leetcode.cn/problems/ways-to-split-array-into-three-subarrays/) (Medium)
- [ ] [1918. Kth Smallest Subarray Sum](https://leetcode.cn/problems/kth-smallest-subarray-sum/) (Medium) 👑

## 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

-   [LeetCode](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | [LeetCode CH](https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) (Medium)

-   Tags: array, queue, sliding window, heap priority queue, ordered set, monotonic queue

## 825. Friends Of Appropriate Ages

-   [LeetCode](https://leetcode.com/problems/friends-of-appropriate-ages/) | [LeetCode CH](https://leetcode.cn/problems/friends-of-appropriate-ages/) (Medium)

-   Tags: array, two pointers, binary search, sorting

## 2401. Longest Nice Subarray

-   [LeetCode](https://leetcode.com/problems/longest-nice-subarray/) | [LeetCode CH](https://leetcode.cn/problems/longest-nice-subarray/) (Medium)

-   Tags: array, bit manipulation, sliding window

## 1156. Swap For Longest Repeated Character Substring

-   [LeetCode](https://leetcode.com/problems/swap-for-longest-repeated-character-substring/) | [LeetCode CH](https://leetcode.cn/problems/swap-for-longest-repeated-character-substring/) (Medium)

-   Tags: hash table, string, sliding window

## 424. Longest Repeating Character Replacement

-   [LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/) | [LeetCode CH](https://leetcode.cn/problems/longest-repeating-character-replacement/) (Medium)

-   Tags: hash table, string, sliding window

```python title="424. Longest Repeating Character Replacement - Python Solution"
from collections import defaultdict


# Sliding Window - Variable
def characterReplacement(s: str, k: int) -> int:
    left = 0
    maxCount = 0
    counts = defaultdict(int)
    maxLen = 0

    for right in range(len(s)):
        counts[s[right]] += 1
        maxCount = max(maxCount, counts[s[right]])

        while right - left + 1 - maxCount > k:
            counts[s[left]] -= 1
            left += 1

        maxLen = max(maxLen, right - left + 1)

    return maxLen


s = "ABAB"
k = 2
print(characterReplacement(s, k))  # 4

```

## 438. Find All Anagrams in a String

-   [LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | [LeetCode CH](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) (Medium)

-   Tags: hash table, string, sliding window

```python title="438. Find All Anagrams in a String - Python Solution"
from typing import List


# Sliding Window Fixed Size
def findAnagrams(s: str, p: str) -> List[int]:
    n, k = len(s), len(p)
    target = [0 for _ in range(26)]
    for ch in p:
        target[ord(ch) - ord("a")] += 1

    count = [0 for _ in range(26)]
    left = 0
    res = []

    for right in range(n):
        count[ord(s[right]) - ord("a")] += 1
        if right < k - 1:
            continue

        if count == target:
            res.append(left)

        count[ord(s[left]) - ord("a")] -= 1
        left += 1

    return res


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))  # [0, 6]

```

## 1712. Ways to Split Array Into Three Subarrays

-   [LeetCode](https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/ways-to-split-array-into-three-subarrays/) (Medium)

-   Tags: array, two pointers, binary search, prefix sum

## 1918. Kth Smallest Subarray Sum

-   [LeetCode](https://leetcode.com/problems/kth-smallest-subarray-sum/) | [LeetCode CH](https://leetcode.cn/problems/kth-smallest-subarray-sum/) (Medium)

-   Tags: array, binary search, sliding window
