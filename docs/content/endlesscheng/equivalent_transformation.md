---
comments: True
---

# Equivalent Transformation

## Table of Contents

- [ ] [3375. Minimum Operations to Make Array Values Equal to K](https://leetcode.cn/problems/minimum-operations-to-make-array-values-equal-to-k/) (Easy)
- [ ] [2914. Minimum Number of Changes to Make Binary String Beautiful](https://leetcode.cn/problems/minimum-number-of-changes-to-make-binary-string-beautiful/) (Medium)
- [ ] [3365. Rearrange K Substrings to Form Target String](https://leetcode.cn/problems/rearrange-k-substrings-to-form-target-string/) (Medium)
- [ ] [1657. Determine if Two Strings Are Close](https://leetcode.cn/problems/determine-if-two-strings-are-close/) (Medium)
- [ ] [2551. Put Marbles in Bags](https://leetcode.cn/problems/put-marbles-in-bags/) (Hard)
- [ ] [1585. Check If String Is Transformable With Substring Sort Operations](https://leetcode.cn/problems/check-if-string-is-transformable-with-substring-sort-operations/) (Hard)
- [ ] [1040. Moving Stones Until Consecutive II](https://leetcode.cn/problems/moving-stones-until-consecutive-ii/) (Medium)
- [ ] [249. Group Shifted Strings](https://leetcode.cn/problems/group-shifted-strings/) (Medium) 👑
- [x] [49. Group Anagrams](https://leetcode.cn/problems/group-anagrams/) (Medium)
- [ ] [1183. Maximum Number of Ones](https://leetcode.cn/problems/maximum-number-of-ones/) (Hard) 👑

## 3375. Minimum Operations to Make Array Values Equal to K

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-make-array-values-equal-to-k/) (Easy)

-   Tags: array, hash table

## 2914. Minimum Number of Changes to Make Binary String Beautiful

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-changes-to-make-binary-string-beautiful/) (Medium)

-   Tags: string

## 3365. Rearrange K Substrings to Form Target String

-   [LeetCode](https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/) | [LeetCode CH](https://leetcode.cn/problems/rearrange-k-substrings-to-form-target-string/) (Medium)

-   Tags: hash table, string, sorting

## 1657. Determine if Two Strings Are Close

-   [LeetCode](https://leetcode.com/problems/determine-if-two-strings-are-close/) | [LeetCode CH](https://leetcode.cn/problems/determine-if-two-strings-are-close/) (Medium)

-   Tags: hash table, string, sorting, counting

## 2551. Put Marbles in Bags

-   [LeetCode](https://leetcode.com/problems/put-marbles-in-bags/) | [LeetCode CH](https://leetcode.cn/problems/put-marbles-in-bags/) (Hard)

-   Tags: array, greedy, sorting, heap priority queue

## 1585. Check If String Is Transformable With Substring Sort Operations

-   [LeetCode](https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/) | [LeetCode CH](https://leetcode.cn/problems/check-if-string-is-transformable-with-substring-sort-operations/) (Hard)

-   Tags: string, greedy, sorting

## 1040. Moving Stones Until Consecutive II

-   [LeetCode](https://leetcode.com/problems/moving-stones-until-consecutive-ii/) | [LeetCode CH](https://leetcode.cn/problems/moving-stones-until-consecutive-ii/) (Medium)

-   Tags: array, math, two pointers, sorting

## 249. Group Shifted Strings

-   [LeetCode](https://leetcode.com/problems/group-shifted-strings/) | [LeetCode CH](https://leetcode.cn/problems/group-shifted-strings/) (Medium)

-   Tags: array, hash table, string

## 49. Group Anagrams

-   [LeetCode](https://leetcode.com/problems/group-anagrams/) | [LeetCode CH](https://leetcode.cn/problems/group-anagrams/) (Medium)

-   Tags: array, hash table, string, sorting

```python title="49. Group Anagrams - Python Solution"
from collections import defaultdict
from typing import List


# Hash - List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for i in s:
            count[ord(i) - ord("a")] += 1

        result[tuple(count)].append(s)

    return list(result.values())


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |    Hash     |     O(n * k)    |     O(n)     |
# |-------------|-----------------|--------------|


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

```

## 1183. Maximum Number of Ones

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-ones/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-ones/) (Hard)

-   Tags: math, greedy, sorting, heap priority queue
