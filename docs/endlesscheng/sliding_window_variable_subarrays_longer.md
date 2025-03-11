---
comments: True
---

# Sliding Window Variable Subarrays Longer

- [x] [1358. Number of Substrings Containing All Three Characters](https://leetcode.cn/problems/number-of-substrings-containing-all-three-characters/) (Medium)
- [ ] [2962. Count Subarrays Where Max Element Appears at Least K Times](https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/) (Medium)
- [ ] [3325. Count Substrings With K-Frequency Characters I](https://leetcode.cn/problems/count-substrings-with-k-frequency-characters-i/) (Medium)
- [ ] [2799. Count Complete Subarrays in an Array](https://leetcode.cn/problems/count-complete-subarrays-in-an-array/) (Medium)
- [ ] [2537. Count the Number of Good Subarrays](https://leetcode.cn/problems/count-the-number-of-good-subarrays/) (Medium)
- [ ] [3298. Count Substrings That Can Be Rearranged to Contain a String II](https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/) (Hard)
- [ ] [2495. Number of Subarrays Having Even Product](https://leetcode.cn/problems/number-of-subarrays-having-even-product/) (Medium) 👑

## 1358. Number of Substrings Containing All Three Characters

-   [LeetCode](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/) | [LeetCode CH](https://leetcode.cn/problems/number-of-substrings-containing-all-three-characters/) (Medium)

-   Tags: hash table, string, sliding window

```python title="1358. Number of Substrings Containing All Three Characters - Python Solution"
from collections import defaultdict


# Sliding Window Variable Size
def numberOfSubstrings(s: str) -> int:
    freqs = defaultdict(int)
    res = 0
    left = 0

    for right in range(len(s)):
        freqs[s[right]] += 1

        while len(freqs) == 3:
            freqs[s[left]] -= 1
            if freqs[s[left]] == 0:
                del freqs[s[left]]
            left += 1

        res += left

    return res


s = "abcabc"
print(numberOfSubstrings(s))  # 10

```

## 2962. Count Subarrays Where Max Element Appears at Least K Times

-   [LeetCode](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/) | [LeetCode CH](https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/) (Medium)

-   Tags: array, sliding window

## 3325. Count Substrings With K-Frequency Characters I

-   [LeetCode](https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/) | [LeetCode CH](https://leetcode.cn/problems/count-substrings-with-k-frequency-characters-i/) (Medium)

-   Tags: hash table, string, sliding window

## 2799. Count Complete Subarrays in an Array

-   [LeetCode](https://leetcode.com/problems/count-complete-subarrays-in-an-array/) | [LeetCode CH](https://leetcode.cn/problems/count-complete-subarrays-in-an-array/) (Medium)

-   Tags: array, hash table, sliding window

## 2537. Count the Number of Good Subarrays

-   [LeetCode](https://leetcode.com/problems/count-the-number-of-good-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/count-the-number-of-good-subarrays/) (Medium)

-   Tags: array, hash table, sliding window

## 3298. Count Substrings That Can Be Rearranged to Contain a String II

-   [LeetCode](https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/) | [LeetCode CH](https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/) (Hard)

-   Tags: hash table, string, sliding window

## 2495. Number of Subarrays Having Even Product

-   [LeetCode](https://leetcode.com/problems/number-of-subarrays-having-even-product/) | [LeetCode CH](https://leetcode.cn/problems/number-of-subarrays-having-even-product/) (Medium)

-   Tags: array, math, dynamic programming
