---
comments: True
---

# Hashing

## Table of Contents

- [ ] [760. Find Anagram Mappings](https://leetcode.cn/problems/find-anagram-mappings/) (Easy) 👑
- [x] [266. Palindrome Permutation](https://leetcode.cn/problems/palindrome-permutation/) (Easy) 👑
- [x] [734. Sentence Similarity](https://leetcode.cn/problems/sentence-similarity/) (Easy) 👑
- [ ] [1165. Single-Row Keyboard](https://leetcode.cn/problems/single-row-keyboard/) (Easy) 👑
- [ ] [249. Group Shifted Strings](https://leetcode.cn/problems/group-shifted-strings/) (Medium) 👑
- [ ] [1133. Largest Unique Number](https://leetcode.cn/problems/largest-unique-number/) (Easy) 👑
- [ ] [1426. Counting Elements](https://leetcode.cn/problems/counting-elements/) (Easy) 👑
- [ ] [1198. Find Smallest Common Element in All Rows](https://leetcode.cn/problems/find-smallest-common-element-in-all-rows/) (Medium) 👑

## 760. Find Anagram Mappings

-   [LeetCode](https://leetcode.com/problems/find-anagram-mappings/) | [LeetCode CH](https://leetcode.cn/problems/find-anagram-mappings/) (Easy)

-   Tags: array, hash table

## 266. Palindrome Permutation

-   [LeetCode](https://leetcode.com/problems/palindrome-permutation/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-permutation/) (Easy)

-   Tags: hash table, string, bit manipulation

```python title="266. Palindrome Permutation - Python Solution"
from collections import defaultdict


# Hash
def canPermutePalindromeDict(s: str) -> bool:
    if len(s) == 1:
        return True

    count = defaultdict(int)

    for ch in s:
        if count[ch] == 1:
            count[ch] = 0
            continue
        count[ch] = 1

    return sum(count.values()) <= 1


# Set
def canPermutePalindromeSet(s: str) -> bool:
    if len(s) == 1:
        return True

    seen = set()

    for ch in s:
        if ch in seen:
            seen.remove(ch)
        else:
            seen.add(ch)

    return len(seen) <= 1


assert canPermutePalindromeDict("carerac") is True
assert canPermutePalindromeSet("carerac") is True

```

## 734. Sentence Similarity

-   [LeetCode](https://leetcode.com/problems/sentence-similarity/) | [LeetCode CH](https://leetcode.cn/problems/sentence-similarity/) (Easy)

-   Tags: array, hash table, string

```python title="734. Sentence Similarity - Python Solution"
# Hash Set
def areSentencesSimilar(sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2):
        return False

    sim = set(map(tuple, similarPairs))

    for i in range(len(sentence1)):
        s1, s2 = sentence1[i], sentence2[i]
        if s1 == s2 or (s1, s2) in sim or (s2, s1) in sim:
            continue
        return False

    return True


if __name__ == "__main__":
    sentence1 = ["great", "acting", "skills"]
    sentence2 = ["fine", "drama", "talent"]
    similarPairs = [
        ["great", "fine"],
        ["drama", "acting"],
        ["skills", "talent"],
    ]
    print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # True

```

## 1165. Single-Row Keyboard

-   [LeetCode](https://leetcode.com/problems/single-row-keyboard/) | [LeetCode CH](https://leetcode.cn/problems/single-row-keyboard/) (Easy)

-   Tags: hash table, string

## 249. Group Shifted Strings

-   [LeetCode](https://leetcode.com/problems/group-shifted-strings/) | [LeetCode CH](https://leetcode.cn/problems/group-shifted-strings/) (Medium)

-   Tags: array, hash table, string

## 1133. Largest Unique Number

-   [LeetCode](https://leetcode.com/problems/largest-unique-number/) | [LeetCode CH](https://leetcode.cn/problems/largest-unique-number/) (Easy)

-   Tags: array, hash table, sorting

## 1426. Counting Elements

-   [LeetCode](https://leetcode.com/problems/counting-elements/) | [LeetCode CH](https://leetcode.cn/problems/counting-elements/) (Easy)

-   Tags: array, hash table

## 1198. Find Smallest Common Element in All Rows

-   [LeetCode](https://leetcode.com/problems/find-smallest-common-element-in-all-rows/) | [LeetCode CH](https://leetcode.cn/problems/find-smallest-common-element-in-all-rows/) (Medium)

-   Tags: array, hash table, binary search, matrix, counting
