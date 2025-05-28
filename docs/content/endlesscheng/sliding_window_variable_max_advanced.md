---
comments: True
---

# Sliding Window Variable Max Advanced

## Table of Contents

- [ ] [2730. Find the Longest Semi-Repetitive Substring](https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/) (Medium)
- [ ] [2779. Maximum Beauty of an Array After Applying Operation](https://leetcode.cn/problems/maximum-beauty-of-an-array-after-applying-operation/) (Medium)
- [ ] [1838. Frequency of the Most Frequent Element](https://leetcode.cn/problems/frequency-of-the-most-frequent-element/) (Medium)
- [ ] [2516. Take K of Each Character From Left and Right](https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/) (Medium)
- [ ] [2831. Find the Longest Equal Subarray](https://leetcode.cn/problems/find-the-longest-equal-subarray/) (Medium)
- [ ] [2271. Maximum White Tiles Covered by a Carpet](https://leetcode.cn/problems/maximum-white-tiles-covered-by-a-carpet/) (Medium)
- [ ] [2106. Maximum Fruits Harvested After at Most K Steps](https://leetcode.cn/problems/maximum-fruits-harvested-after-at-most-k-steps/) (Hard)
- [x] [2555. Maximize Win From Two Segments](https://leetcode.cn/problems/maximize-win-from-two-segments/) (Medium)
- [ ] [2009. Minimum Number of Operations to Make Array Continuous](https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-continuous/) (Hard)
- [ ] [1610. Maximum Number of Visible Points](https://leetcode.cn/problems/maximum-number-of-visible-points/) (Hard)
- [ ] [2781. Length of the Longest Valid Substring](https://leetcode.cn/problems/length-of-the-longest-valid-substring/) (Hard)
- [ ] [3411. Maximum Subarray With Equal Products](https://leetcode.cn/problems/maximum-subarray-with-equal-products/) (Easy)
- [ ] [2968. Apply Operations to Maximize Frequency Score](https://leetcode.cn/problems/apply-operations-to-maximize-frequency-score/) (Hard)
- [ ] [1040. Moving Stones Until Consecutive II](https://leetcode.cn/problems/moving-stones-until-consecutive-ii/) (Medium)
- [ ] [3413. Maximum Coins From K Consecutive Bags](https://leetcode.cn/problems/maximum-coins-from-k-consecutive-bags/) (Medium)
- [ ] [395. Longest Substring with At Least K Repeating Characters](https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/) (Medium)
- [ ] [1763. Longest Nice Substring](https://leetcode.cn/problems/longest-nice-substring/) (Easy)
- [ ] [487. Max Consecutive Ones II](https://leetcode.cn/problems/max-consecutive-ones-ii/) (Medium) 👑
- [x] [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.cn/problems/longest-substring-with-at-most-two-distinct-characters/) (Medium) 👑
- [x] [340. Longest Substring with At Most K Distinct Characters](https://leetcode.cn/problems/longest-substring-with-at-most-k-distinct-characters/) (Medium) 👑

## 2730. Find the Longest Semi-Repetitive Substring

-   [LeetCode](https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/) | [LeetCode CH](https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/) (Medium)

-   Tags: string, sliding window
## 2779. Maximum Beauty of an Array After Applying Operation

-   [LeetCode](https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/) | [LeetCode CH](https://leetcode.cn/problems/maximum-beauty-of-an-array-after-applying-operation/) (Medium)

-   Tags: array, binary search, sliding window, sorting
## 1838. Frequency of the Most Frequent Element

-   [LeetCode](https://leetcode.com/problems/frequency-of-the-most-frequent-element/) | [LeetCode CH](https://leetcode.cn/problems/frequency-of-the-most-frequent-element/) (Medium)

-   Tags: array, binary search, greedy, sliding window, sorting, prefix sum
## 2516. Take K of Each Character From Left and Right

-   [LeetCode](https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/) | [LeetCode CH](https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/) (Medium)

-   Tags: hash table, string, sliding window
## 2831. Find the Longest Equal Subarray

-   [LeetCode](https://leetcode.com/problems/find-the-longest-equal-subarray/) | [LeetCode CH](https://leetcode.cn/problems/find-the-longest-equal-subarray/) (Medium)

-   Tags: array, hash table, binary search, sliding window
## 2271. Maximum White Tiles Covered by a Carpet

-   [LeetCode](https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/) | [LeetCode CH](https://leetcode.cn/problems/maximum-white-tiles-covered-by-a-carpet/) (Medium)

-   Tags: array, binary search, greedy, sliding window, sorting, prefix sum
## 2106. Maximum Fruits Harvested After at Most K Steps

-   [LeetCode](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/) | [LeetCode CH](https://leetcode.cn/problems/maximum-fruits-harvested-after-at-most-k-steps/) (Hard)

-   Tags: array, binary search, sliding window, prefix sum
## 2555. Maximize Win From Two Segments

-   [LeetCode](https://leetcode.com/problems/maximize-win-from-two-segments/) | [LeetCode CH](https://leetcode.cn/problems/maximize-win-from-two-segments/) (Medium)

-   Tags: array, binary search, sliding window

```python title="2555. Maximize Win From Two Segments - Python Solution"
from typing import List


# Sliding Window - Variable
def maximizeWin(prizePositions: List[int], k: int) -> int:
    n = len(prizePositions)

    if 2 * k >= prizePositions[-1] - prizePositions[0]:
        return n

    ans = left = 0
    mx = [0] * (n + 1)

    for right, p in enumerate(prizePositions):
        while p - prizePositions[left] > k:
            left += 1
        ans = max(ans, mx[left] + right - left + 1)
        mx[right + 1] = max(mx[right], right - left + 1)

    return ans


prizePositions = [1, 1, 2, 2, 3, 3, 5]
k = 2
print(maximizeWin(prizePositions, k))  # 7

```

## 2009. Minimum Number of Operations to Make Array Continuous

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-continuous/) (Hard)

-   Tags: array, hash table, binary search, sliding window
## 1610. Maximum Number of Visible Points

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-visible-points/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-visible-points/) (Hard)

-   Tags: array, math, geometry, sliding window, sorting
## 2781. Length of the Longest Valid Substring

-   [LeetCode](https://leetcode.com/problems/length-of-the-longest-valid-substring/) | [LeetCode CH](https://leetcode.cn/problems/length-of-the-longest-valid-substring/) (Hard)

-   Tags: array, hash table, string, sliding window
## 3411. Maximum Subarray With Equal Products

-   [LeetCode](https://leetcode.com/problems/maximum-subarray-with-equal-products/) | [LeetCode CH](https://leetcode.cn/problems/maximum-subarray-with-equal-products/) (Easy)

-   Tags: array, math, sliding window, enumeration, number theory
## 2968. Apply Operations to Maximize Frequency Score

-   [LeetCode](https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/) | [LeetCode CH](https://leetcode.cn/problems/apply-operations-to-maximize-frequency-score/) (Hard)

-   Tags: array, binary search, sliding window, sorting, prefix sum
## 1040. Moving Stones Until Consecutive II

-   [LeetCode](https://leetcode.com/problems/moving-stones-until-consecutive-ii/) | [LeetCode CH](https://leetcode.cn/problems/moving-stones-until-consecutive-ii/) (Medium)

-   Tags: array, math, two pointers, sorting
## 3413. Maximum Coins From K Consecutive Bags

-   [LeetCode](https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/) | [LeetCode CH](https://leetcode.cn/problems/maximum-coins-from-k-consecutive-bags/) (Medium)

-   Tags: array, binary search, greedy, sliding window, sorting, prefix sum
## 395. Longest Substring with At Least K Repeating Characters

-   [LeetCode](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/) | [LeetCode CH](https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/) (Medium)

-   Tags: hash table, string, divide and conquer, sliding window
## 1763. Longest Nice Substring

-   [LeetCode](https://leetcode.com/problems/longest-nice-substring/) | [LeetCode CH](https://leetcode.cn/problems/longest-nice-substring/) (Easy)

-   Tags: hash table, string, divide and conquer, bit manipulation, sliding window
## 487. Max Consecutive Ones II

-   [LeetCode](https://leetcode.com/problems/max-consecutive-ones-ii/) | [LeetCode CH](https://leetcode.cn/problems/max-consecutive-ones-ii/) (Medium)

-   Tags: array, dynamic programming, sliding window
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
