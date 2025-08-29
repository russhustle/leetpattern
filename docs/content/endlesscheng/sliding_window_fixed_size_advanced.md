---
comments: True
---

# Sliding Window Fixed Size Advanced

## Table of Contents

- [ ] [1461. Check If a String Contains All Binary Codes of Size K](https://leetcode.cn/problems/check-if-a-string-contains-all-binary-codes-of-size-k/) (Medium)
- [ ] [2134. Minimum Swaps to Group All 1's Together II](https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together-ii/) (Medium)
- [ ] [1297. Maximum Number of Occurrences of a Substring](https://leetcode.cn/problems/maximum-number-of-occurrences-of-a-substring/) (Medium)
- [ ] [2653. Sliding Subarray Beauty](https://leetcode.cn/problems/sliding-subarray-beauty/) (Medium)
- [ ] [3439. Reschedule Meetings for Maximum Free Time I](https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-i/) (Medium)
- [ ] [1888. Minimum Number of Flips to Make the Binary String Alternating](https://leetcode.cn/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/) (Medium)
- [x] [567. Permutation in String](https://leetcode.cn/problems/permutation-in-string/) (Medium)
- [x] [438. Find All Anagrams in a String](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) (Medium)
- [ ] [30. Substring with Concatenation of All Words](https://leetcode.cn/problems/substring-with-concatenation-of-all-words/) (Hard)
- [ ] [2156. Find Substring With Given Hash Value](https://leetcode.cn/problems/find-substring-with-given-hash-value/) (Hard)
- [ ] [2953. Count Complete Substrings](https://leetcode.cn/problems/count-complete-substrings/) (Hard)
- [ ] [1016. Binary String With Substrings Representing 1 To N](https://leetcode.cn/problems/binary-string-with-substrings-representing-1-to-n/) (Medium)
- [ ] [683. K Empty Slots](https://leetcode.cn/problems/k-empty-slots/) (Hard) 👑
- [ ] [2067. Number of Equal Count Substrings](https://leetcode.cn/problems/number-of-equal-count-substrings/) (Medium) 👑
- [ ] [2524. Maximum Frequency Score of a Subarray](https://leetcode.cn/problems/maximum-frequency-score-of-a-subarray/) (Hard) 👑

## 1461. Check If a String Contains All Binary Codes of Size K

-   [LeetCode](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/) | [LeetCode CH](https://leetcode.cn/problems/check-if-a-string-contains-all-binary-codes-of-size-k/) (Medium)

-   Tags: hash table, string, bit manipulation, rolling hash, hash function
## 2134. Minimum Swaps to Group All 1's Together II

-   [LeetCode](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/) | [LeetCode CH](https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together-ii/) (Medium)

-   Tags: array, sliding window
## 1297. Maximum Number of Occurrences of a Substring

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-occurrences-of-a-substring/) (Medium)

-   Tags: hash table, string, sliding window
## 2653. Sliding Subarray Beauty

-   [LeetCode](https://leetcode.com/problems/sliding-subarray-beauty/) | [LeetCode CH](https://leetcode.cn/problems/sliding-subarray-beauty/) (Medium)

-   Tags: array, hash table, sliding window
## 3439. Reschedule Meetings for Maximum Free Time I

-   [LeetCode](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/) | [LeetCode CH](https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-i/) (Medium)

-   Tags: array, greedy, sliding window
## 1888. Minimum Number of Flips to Make the Binary String Alternating

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/) (Medium)

-   Tags: string, dynamic programming, greedy, sliding window
## 567. Permutation in String

-   [LeetCode](https://leetcode.com/problems/permutation-in-string/) | [LeetCode CH](https://leetcode.cn/problems/permutation-in-string/) (Medium)

-   Tags: hash table, two pointers, string, sliding window
```python title="567. Permutation in String - Python Solution"
def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    count1 = [0] * 26
    count2 = [0] * 26

    for i in range(len(s1)):
        count1[ord(s1[i]) - ord("a")] += 1
        count2[ord(s2[i]) - ord("a")] += 1

    matches = 0
    for i in range(26):
        if count1[i] == count2[i]:
            matches += 1

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        index = ord(s2[r]) - ord("a")
        count2[index] += 1
        if count1[index] == count2[index]:
            matches += 1
        elif count1[index] + 1 == count2[index]:
            matches -= 1

        index = ord(s2[l]) - ord("a")
        count2[index] -= 1
        if count1[index] == count2[index]:
            matches += 1
        elif count1[index] - 1 == count2[index]:
            matches -= 1

        l += 1

    return matches == 26


s1 = "ab"
s2 = "eidba"
print(checkInclusion(s1, s2))  # True

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

## 30. Substring with Concatenation of All Words

-   [LeetCode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | [LeetCode CH](https://leetcode.cn/problems/substring-with-concatenation-of-all-words/) (Hard)

-   Tags: hash table, string, sliding window
## 2156. Find Substring With Given Hash Value

-   [LeetCode](https://leetcode.com/problems/find-substring-with-given-hash-value/) | [LeetCode CH](https://leetcode.cn/problems/find-substring-with-given-hash-value/) (Hard)

-   Tags: string, sliding window, rolling hash, hash function
## 2953. Count Complete Substrings

-   [LeetCode](https://leetcode.com/problems/count-complete-substrings/) | [LeetCode CH](https://leetcode.cn/problems/count-complete-substrings/) (Hard)

-   Tags: hash table, string, sliding window
## 1016. Binary String With Substrings Representing 1 To N

-   [LeetCode](https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/) | [LeetCode CH](https://leetcode.cn/problems/binary-string-with-substrings-representing-1-to-n/) (Medium)

-   Tags: string
## 683. K Empty Slots

-   [LeetCode](https://leetcode.com/problems/k-empty-slots/) | [LeetCode CH](https://leetcode.cn/problems/k-empty-slots/) (Hard)

-   Tags: array, binary indexed tree, segment tree, queue, sliding window, heap priority queue, ordered set, monotonic queue
## 2067. Number of Equal Count Substrings

-   [LeetCode](https://leetcode.com/problems/number-of-equal-count-substrings/) | [LeetCode CH](https://leetcode.cn/problems/number-of-equal-count-substrings/) (Medium)

-   Tags: string, counting, prefix sum
## 2524. Maximum Frequency Score of a Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-frequency-score-of-a-subarray/) (Hard)

-   Tags: array, hash table, math, stack, sliding window
