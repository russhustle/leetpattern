---
comments: True
---

# Sliding Window Variable Min

- [x] [209. Minimum Size Subarray Sum](https://leetcode.cn/problems/minimum-size-subarray-sum/) (Medium)
- [x] [2904. Shortest and Lexicographically Smallest Beautiful String](https://leetcode.cn/problems/shortest-and-lexicographically-smallest-beautiful-string/) (Medium)
- [ ] [1234. Replace the Substring for Balanced String](https://leetcode.cn/problems/replace-the-substring-for-balanced-string/) (Medium)
- [ ] [2875. Minimum Size Subarray in Infinite Array](https://leetcode.cn/problems/minimum-size-subarray-in-infinite-array/) (Medium)
- [x] [76. Minimum Window Substring](https://leetcode.cn/problems/minimum-window-substring/) (Hard)
- [ ] [632. Smallest Range Covering Elements from K Lists](https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/) (Hard)

## 209. Minimum Size Subarray Sum

-   [LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/) | [LeetCode CH](https://leetcode.cn/problems/minimum-size-subarray-sum/) (Medium)

-   Tags: array, binary search, sliding window, prefix sum

```python title="209. Minimum Size Subarray Sum - Python Solution"
import bisect
from typing import List


# Prefix Sum
def minSubArrayLenPS(target: int, nums: List[int]) -> int:
    n = len(nums)
    prefix_sums = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

    minLen = float("inf")

    for i in range(n + 1):
        new_target = target + prefix_sums[i]
        bound = bisect.bisect_left(prefix_sums, new_target)
        if bound != len(prefix_sums):
            minLen = min(minLen, bound - i)

    return 0 if minLen == float("inf") else minLen


# Sliding Window Variable Size
def minSubArrayLenSW(target: int, nums: List[int]) -> int:
    res, cur = float("inf"), 0
    left = 0

    for right in range(len(nums)):
        cur += nums[right]

        while cur >= target:
            res = min(res, right - left + 1)
            cur -= nums[left]
            left += 1

    return res if res != float("inf") else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLenPS(target, nums))  # 2
print(minSubArrayLenSW(target, nums))  # 2

```

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

## 1234. Replace the Substring for Balanced String

-   [LeetCode](https://leetcode.com/problems/replace-the-substring-for-balanced-string/) | [LeetCode CH](https://leetcode.cn/problems/replace-the-substring-for-balanced-string/) (Medium)

-   Tags: string, sliding window

## 2875. Minimum Size Subarray in Infinite Array

-   [LeetCode](https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/) | [LeetCode CH](https://leetcode.cn/problems/minimum-size-subarray-in-infinite-array/) (Medium)

-   Tags: array, hash table, sliding window, prefix sum

## 76. Minimum Window Substring

-   [LeetCode](https://leetcode.com/problems/minimum-window-substring/) | [LeetCode CH](https://leetcode.cn/problems/minimum-window-substring/) (Hard)

-   Tags: hash table, string, sliding window

```python title="76. Minimum Window Substring - Python Solution"
from collections import Counter


def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""

    counts = Counter(t)
    required = len(counts)

    left, right = 0, 0
    formed = 0
    window_counts = dict()

    result = float("inf"), None, None

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in counts and window_counts[char] == counts[char]:
            formed += 1

        while left <= right and formed == required:
            char = s[left]
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)
            window_counts[char] -= 1
            if char in counts and window_counts[char] < counts[char]:
                formed -= 1
            left += 1

        right += 1

    return "" if result[0] == float("inf") else s[result[1] : result[2] + 1]


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  # BANC

```

## 632. Smallest Range Covering Elements from K Lists

-   [LeetCode](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | [LeetCode CH](https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/) (Hard)

-   Tags: array, hash table, greedy, sliding window, sorting, heap priority queue
