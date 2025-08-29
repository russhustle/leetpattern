---
comments: True
---

# Palindrome Greedy

## Table of Contents

- [x] [409. Longest Palindrome](https://leetcode.cn/problems/longest-palindrome/) (Easy)
- [x] [2697. Lexicographically Smallest Palindrome](https://leetcode.cn/problems/lexicographically-smallest-palindrome/) (Easy)
- [ ] [680. Valid Palindrome II](https://leetcode.cn/problems/valid-palindrome-ii/) (Easy)
- [x] [1328. Break a Palindrome](https://leetcode.cn/problems/break-a-palindrome/) (Medium)
- [x] [1400. Construct K Palindrome Strings](https://leetcode.cn/problems/construct-k-palindrome-strings/) (Medium)
- [ ] [2131. Longest Palindrome by Concatenating Two Letter Words](https://leetcode.cn/problems/longest-palindrome-by-concatenating-two-letter-words/) (Medium)
- [ ] [2384. Largest Palindromic Number](https://leetcode.cn/problems/largest-palindromic-number/) (Medium)
- [ ] [3035. Maximum Palindromes After Operations](https://leetcode.cn/problems/maximum-palindromes-after-operations/) (Medium)
- [ ] [1616. Split Two Strings to Make Palindrome](https://leetcode.cn/problems/split-two-strings-to-make-palindrome/) (Medium)
- [ ] [1147. Longest Chunked Palindrome Decomposition](https://leetcode.cn/problems/longest-chunked-palindrome-decomposition/) (Hard)
- [ ] [2193. Minimum Number of Moves to Make Palindrome](https://leetcode.cn/problems/minimum-number-of-moves-to-make-palindrome/) (Hard)
- [ ] [564. Find the Closest Palindrome](https://leetcode.cn/problems/find-the-closest-palindrome/) (Hard)
- [x] [266. Palindrome Permutation](https://leetcode.cn/problems/palindrome-permutation/) (Easy) 👑
- [ ] [2422. Merge Operations to Turn Array Into a Palindrome](https://leetcode.cn/problems/merge-operations-to-turn-array-into-a-palindrome/) (Medium) 👑
- [ ] [1842. Next Palindrome Using Same Digits](https://leetcode.cn/problems/next-palindrome-using-same-digits/) (Hard) 👑
- [ ] [3088. Make String Anti-palindrome](https://leetcode.cn/problems/make-string-anti-palindrome/) (Hard) 👑

## 409. Longest Palindrome

-   [LeetCode](https://leetcode.com/problems/longest-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/longest-palindrome/) (Easy)

-   Tags: hash table, string, greedy
-   Return the length of the longest palindrome that can be built with the characters in the string.

```python title="409. Longest Palindrome - Python Solution"
def longestPalindrome(s: str) -> int:
    hashmap = dict()
    result = 0

    for char in s:
        if char not in hashmap or hashmap[char] == 0:
            hashmap[char] = 1
        else:
            result += 2
            hashmap[char] = 0

    if any(hashmap.values()):
        result += 1

    return result


print(longestPalindrome("abccccdd"))  # 7

```

## 2697. Lexicographically Smallest Palindrome

-   [LeetCode](https://leetcode.com/problems/lexicographically-smallest-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/lexicographically-smallest-palindrome/) (Easy)

-   Tags: two pointers, string, greedy
```python title="2697. Lexicographically Smallest Palindrome - Python Solution"
def makeSmallestPalindrome(s: str) -> str:
    n = len(s)
    s = list(s)
    left, right = 0, n - 1

    while left < right:
        if s[left] < s[right]:
            s[right] = s[left]
        elif s[left] > s[right]:
            s[left] = s[right]
        left += 1
        right -= 1

    return "".join(s)


s = "egcfe"
print(makeSmallestPalindrome(s))  # "efcfe"

```

## 680. Valid Palindrome II

-   [LeetCode](https://leetcode.com/problems/valid-palindrome-ii/) | [LeetCode CH](https://leetcode.cn/problems/valid-palindrome-ii/) (Easy)

-   Tags: two pointers, string, greedy
## 1328. Break a Palindrome

-   [LeetCode](https://leetcode.com/problems/break-a-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/break-a-palindrome/) (Medium)

-   Tags: string, greedy
```python title="1328. Break a Palindrome - Python Solution"
# Greedy
def breakPalindrome(palindrome: str) -> str:
    n = len(palindrome)
    if n == 1:
        return ""

    for i in range(n // 2):
        if palindrome[i] != "a":
            return palindrome[:i] + "a" + palindrome[i + 1 :]

    return palindrome[:-1] + "b"


palindrome = "abccba"
print(breakPalindrome(palindrome))  # "aaccba"

```

## 1400. Construct K Palindrome Strings

-   [LeetCode](https://leetcode.com/problems/construct-k-palindrome-strings/) | [LeetCode CH](https://leetcode.cn/problems/construct-k-palindrome-strings/) (Medium)

-   Tags: hash table, string, greedy, counting
```python title="1400. Construct K Palindrome Strings - Python Solution"
from collections import Counter


def canConstructCounter(s: str, k: int) -> bool:
    if len(s) < k:
        return False

    counts = Counter(s)
    odd = 0

    for c in counts.values():
        odd += c % 2

    return odd <= k


def canConstructHash(s: str, k: int) -> bool:
    if len(s) < k:
        return False

    counts = [0 for _ in range(26)]

    for ch in s:
        idx = ord(ch) - ord("a")
        if counts[idx] == 0:
            counts[idx] += 1
        else:
            counts[idx] -= 1

    return sum(counts) <= k


s = "annabelle"
k = 2
print(canConstructCounter(s, k))  # True
print(canConstructHash(s, k))  # True

```

## 2131. Longest Palindrome by Concatenating Two Letter Words

-   [LeetCode](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/) | [LeetCode CH](https://leetcode.cn/problems/longest-palindrome-by-concatenating-two-letter-words/) (Medium)

-   Tags: array, hash table, string, greedy, counting
## 2384. Largest Palindromic Number

-   [LeetCode](https://leetcode.com/problems/largest-palindromic-number/) | [LeetCode CH](https://leetcode.cn/problems/largest-palindromic-number/) (Medium)

-   Tags: hash table, string, greedy, counting
## 3035. Maximum Palindromes After Operations

-   [LeetCode](https://leetcode.com/problems/maximum-palindromes-after-operations/) | [LeetCode CH](https://leetcode.cn/problems/maximum-palindromes-after-operations/) (Medium)

-   Tags: array, hash table, string, greedy, sorting, counting
## 1616. Split Two Strings to Make Palindrome

-   [LeetCode](https://leetcode.com/problems/split-two-strings-to-make-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/split-two-strings-to-make-palindrome/) (Medium)

-   Tags: two pointers, string
## 1147. Longest Chunked Palindrome Decomposition

-   [LeetCode](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/) | [LeetCode CH](https://leetcode.cn/problems/longest-chunked-palindrome-decomposition/) (Hard)

-   Tags: two pointers, string, dynamic programming, greedy, rolling hash, hash function
## 2193. Minimum Number of Moves to Make Palindrome

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-moves-to-make-palindrome/) (Hard)

-   Tags: two pointers, string, greedy, binary indexed tree
## 564. Find the Closest Palindrome

-   [LeetCode](https://leetcode.com/problems/find-the-closest-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/find-the-closest-palindrome/) (Hard)

-   Tags: math, string
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

## 2422. Merge Operations to Turn Array Into a Palindrome

-   [LeetCode](https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/merge-operations-to-turn-array-into-a-palindrome/) (Medium)

-   Tags: array, two pointers, greedy
## 1842. Next Palindrome Using Same Digits

-   [LeetCode](https://leetcode.com/problems/next-palindrome-using-same-digits/) | [LeetCode CH](https://leetcode.cn/problems/next-palindrome-using-same-digits/) (Hard)

-   Tags: two pointers, string
## 3088. Make String Anti-palindrome

-   [LeetCode](https://leetcode.com/problems/make-string-anti-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/make-string-anti-palindrome/) (Hard)

-   Tags: string, greedy, sorting, counting sort
