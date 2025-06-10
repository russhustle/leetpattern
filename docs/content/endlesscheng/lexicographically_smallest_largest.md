---
comments: True
---

# Lexicographically Smallest Largest

## Table of Contents

- [ ] [1323. Maximum 69 Number](https://leetcode.cn/problems/maximum-69-number/) (Easy)
- [ ] [3216. Lexicographically Smallest String After a Swap](https://leetcode.cn/problems/lexicographically-smallest-string-after-a-swap/) (Easy)
- [x] [2697. Lexicographically Smallest Palindrome](https://leetcode.cn/problems/lexicographically-smallest-palindrome/) (Easy)
- [ ] [1881. Maximum Value after Insertion](https://leetcode.cn/problems/maximum-value-after-insertion/) (Medium)
- [ ] [2734. Lexicographically Smallest String After Substring Operation](https://leetcode.cn/problems/lexicographically-smallest-string-after-substring-operation/) (Medium)
- [ ] [1946. Largest Number After Mutating Substring](https://leetcode.cn/problems/largest-number-after-mutating-substring/) (Medium)
- [ ] [1663. Smallest String With A Given Numeric Value](https://leetcode.cn/problems/smallest-string-with-a-given-numeric-value/) (Medium)
- [x] [1328. Break a Palindrome](https://leetcode.cn/problems/break-a-palindrome/) (Medium)
- [ ] [2259. Remove Digit From Number to Maximize Result](https://leetcode.cn/problems/remove-digit-from-number-to-maximize-result/) (Easy)
- [ ] [2566. Maximum Difference by Remapping a Digit](https://leetcode.cn/problems/maximum-difference-by-remapping-a-digit/) (Easy)
- [ ] [670. Maximum Swap](https://leetcode.cn/problems/maximum-swap/) (Medium)
- [ ] [3106. Lexicographically Smallest String After Operations With Constraint](https://leetcode.cn/problems/lexicographically-smallest-string-after-operations-with-constraint/) (Medium)
- [ ] [1053. Previous Permutation With One Swap](https://leetcode.cn/problems/previous-permutation-with-one-swap/) (Medium)
- [ ] [2375. Construct Smallest Number From DI String](https://leetcode.cn/problems/construct-smallest-number-from-di-string/) (Medium)
- [ ] [2182. Construct String With Repeat Limit](https://leetcode.cn/problems/construct-string-with-repeat-limit/) (Medium)
- [x] [738. Monotone Increasing Digits](https://leetcode.cn/problems/monotone-increasing-digits/) (Medium)
- [x] [3403. Find the Lexicographically Largest String From the Box I](https://leetcode.cn/problems/find-the-lexicographically-largest-string-from-the-box-i/) (Medium)
- [x] [3170. Lexicographically Minimum String After Removing Stars](https://leetcode.cn/problems/lexicographically-minimum-string-after-removing-stars/) (Medium)
- [ ] [1363. Largest Multiple of Three](https://leetcode.cn/problems/largest-multiple-of-three/) (Hard)
- [ ] [1754. Largest Merge Of Two Strings](https://leetcode.cn/problems/largest-merge-of-two-strings/) (Medium)
- [x] [1202. Smallest String With Swaps](https://leetcode.cn/problems/smallest-string-with-swaps/) (Medium)
- [ ] [2434. Using a Robot to Print the Lexicographically Smallest String](https://leetcode.cn/problems/using-a-robot-to-print-the-lexicographically-smallest-string/) (Medium)
- [ ] [1625. Lexicographically Smallest String After Applying Operations](https://leetcode.cn/problems/lexicographically-smallest-string-after-applying-operations/) (Medium)
- [ ] [2948. Make Lexicographically Smallest Array by Swapping Elements](https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements/) (Medium)
- [ ] [564. Find the Closest Palindrome](https://leetcode.cn/problems/find-the-closest-palindrome/) (Hard)
- [ ] [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](https://leetcode.cn/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/) (Hard)
- [ ] [2663. Lexicographically Smallest Beautiful String](https://leetcode.cn/problems/lexicographically-smallest-beautiful-string/) (Hard)
- [ ] [3302. Find the Lexicographically Smallest Valid Sequence](https://leetcode.cn/problems/find-the-lexicographically-smallest-valid-sequence/) (Medium)
- [ ] [555. Split Concatenated Strings](https://leetcode.cn/problems/split-concatenated-strings/) (Medium) 👑
- [ ] [3088. Make String Anti-palindrome](https://leetcode.cn/problems/make-string-anti-palindrome/) (Hard) 👑

## 1323. Maximum 69 Number

-   [LeetCode](https://leetcode.com/problems/maximum-69-number/) | [LeetCode CH](https://leetcode.cn/problems/maximum-69-number/) (Easy)

-   Tags: math, greedy
## 3216. Lexicographically Smallest String After a Swap

-   [LeetCode](https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/) | [LeetCode CH](https://leetcode.cn/problems/lexicographically-smallest-string-after-a-swap/) (Easy)

-   Tags: string, greedy
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

## 1881. Maximum Value after Insertion

-   [LeetCode](https://leetcode.com/problems/maximum-value-after-insertion/) | [LeetCode CH](https://leetcode.cn/problems/maximum-value-after-insertion/) (Medium)

-   Tags: string, greedy
## 2734. Lexicographically Smallest String After Substring Operation

-   [LeetCode](https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/) | [LeetCode CH](https://leetcode.cn/problems/lexicographically-smallest-string-after-substring-operation/) (Medium)

-   Tags: string, greedy
## 1946. Largest Number After Mutating Substring

-   [LeetCode](https://leetcode.com/problems/largest-number-after-mutating-substring/) | [LeetCode CH](https://leetcode.cn/problems/largest-number-after-mutating-substring/) (Medium)

-   Tags: array, string, greedy
## 1663. Smallest String With A Given Numeric Value

-   [LeetCode](https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/) | [LeetCode CH](https://leetcode.cn/problems/smallest-string-with-a-given-numeric-value/) (Medium)

-   Tags: string, greedy
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

## 2259. Remove Digit From Number to Maximize Result

-   [LeetCode](https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/) | [LeetCode CH](https://leetcode.cn/problems/remove-digit-from-number-to-maximize-result/) (Easy)

-   Tags: string, greedy, enumeration
## 2566. Maximum Difference by Remapping a Digit

-   [LeetCode](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/) | [LeetCode CH](https://leetcode.cn/problems/maximum-difference-by-remapping-a-digit/) (Easy)

-   Tags: math, greedy
## 670. Maximum Swap

-   [LeetCode](https://leetcode.com/problems/maximum-swap/) | [LeetCode CH](https://leetcode.cn/problems/maximum-swap/) (Medium)

-   Tags: math, greedy
## 3106. Lexicographically Smallest String After Operations With Constraint

-   [LeetCode](https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/) | [LeetCode CH](https://leetcode.cn/problems/lexicographically-smallest-string-after-operations-with-constraint/) (Medium)

-   Tags: string, greedy
## 1053. Previous Permutation With One Swap

-   [LeetCode](https://leetcode.com/problems/previous-permutation-with-one-swap/) | [LeetCode CH](https://leetcode.cn/problems/previous-permutation-with-one-swap/) (Medium)

-   Tags: array, greedy
## 2375. Construct Smallest Number From DI String

-   [LeetCode](https://leetcode.com/problems/construct-smallest-number-from-di-string/) | [LeetCode CH](https://leetcode.cn/problems/construct-smallest-number-from-di-string/) (Medium)

-   Tags: string, backtracking, stack, greedy
## 2182. Construct String With Repeat Limit

-   [LeetCode](https://leetcode.com/problems/construct-string-with-repeat-limit/) | [LeetCode CH](https://leetcode.cn/problems/construct-string-with-repeat-limit/) (Medium)

-   Tags: hash table, string, greedy, heap priority queue, counting
## 738. Monotone Increasing Digits

-   [LeetCode](https://leetcode.com/problems/monotone-increasing-digits/) | [LeetCode CH](https://leetcode.cn/problems/monotone-increasing-digits/) (Medium)

-   Tags: math, greedy
-   Return the largest number that is less than or equal to `n` with monotone increasing digits.


```python title="738. Monotone Increasing Digits - Python Solution"
# Greedy
def monotoneIncreasingDigits(n: int) -> int:
    strNum = list(str(n))

    for i in range(len(strNum) - 2, -1, -1):
        if int(strNum[i]) > int(strNum[i + 1]):
            strNum[i] = str(int(strNum[i]) - 1)
            strNum[i + 1 :] = ["9"] * (len(strNum) - (i + 1))

    return int("".join(strNum))


n = 332
print(monotoneIncreasingDigits(n))  # 299

```

## 3403. Find the Lexicographically Largest String From the Box I

-   [LeetCode](https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/) | [LeetCode CH](https://leetcode.cn/problems/find-the-lexicographically-largest-string-from-the-box-i/) (Medium)

-   Tags: two pointers, string, enumeration

```python title="3403. Find the Lexicographically Largest String From the Box I - Python Solution"
# Lexicographically Smallest/Largest
def answerString(word: str, numFriends: int) -> str:
    if numFriends == 1:
        return word

    n = len(word)
    return max(word[i : i + n - numFriends + 1] for i in range(n))


if __name__ == "__main__":
    assert answerString("dbca", 2) == "dbc"

```

## 3170. Lexicographically Minimum String After Removing Stars

-   [LeetCode](https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/) | [LeetCode CH](https://leetcode.cn/problems/lexicographically-minimum-string-after-removing-stars/) (Medium)

-   Tags: hash table, string, stack, greedy, heap priority queue

```python title="3170. Lexicographically Minimum String After Removing Stars - Python Solution"
from itertools import chain


# Stack
def clearStars(s: str) -> str:
    stacks = [[] for _ in range(26)]
    for i, c in enumerate(s):
        if c != "*":
            stacks[ord(c) - ord("a")].append(i)
            continue

        for st in stacks:
            if st:
                st.pop()
                break
    return "".join(s[i] for i in sorted(chain.from_iterable(stacks)))


if __name__ == "__main__":
    assert clearStars("aaba*") == "aab"

```

## 1363. Largest Multiple of Three

-   [LeetCode](https://leetcode.com/problems/largest-multiple-of-three/) | [LeetCode CH](https://leetcode.cn/problems/largest-multiple-of-three/) (Hard)

-   Tags: array, dynamic programming, greedy
## 1754. Largest Merge Of Two Strings

-   [LeetCode](https://leetcode.com/problems/largest-merge-of-two-strings/) | [LeetCode CH](https://leetcode.cn/problems/largest-merge-of-two-strings/) (Medium)

-   Tags: two pointers, string, greedy
## 1202. Smallest String With Swaps

-   [LeetCode](https://leetcode.com/problems/smallest-string-with-swaps/) | [LeetCode CH](https://leetcode.cn/problems/smallest-string-with-swaps/) (Medium)

-   Tags: array, hash table, string, depth first search, breadth first search, union find, sorting

```python title="1202. Smallest String With Swaps - Python Solution"
from collections import defaultdict
from typing import List


# Union Find
def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    n = len(s)
    par = list(range(n))
    components = defaultdict(list)

    def find(node):
        p = par[node]
        while par[p] != p:
            par[p] = par[par[p]]
            p = par[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 != p2:
            par[p1] = p2

    for index, j in pairs:
        union(index, j)

    for index in range(n):
        components[find(index)].append(index)

    res = list(s)
    for indices in components.values():
        chars = sorted([s[index] for index in indices])
        for index, char in zip(indices, chars):
            res[index] = char

    return "".join(res)


s = "dcab"
pairs = [[0, 3], [1, 2]]
print(smallestStringWithSwaps(s, pairs))  # "bacd"

```

## 2434. Using a Robot to Print the Lexicographically Smallest String

-   [LeetCode](https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/) | [LeetCode CH](https://leetcode.cn/problems/using-a-robot-to-print-the-lexicographically-smallest-string/) (Medium)

-   Tags: hash table, string, stack, greedy
## 1625. Lexicographically Smallest String After Applying Operations

-   [LeetCode](https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/) | [LeetCode CH](https://leetcode.cn/problems/lexicographically-smallest-string-after-applying-operations/) (Medium)

-   Tags: string, depth first search, breadth first search, enumeration
## 2948. Make Lexicographically Smallest Array by Swapping Elements

-   [LeetCode](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/) | [LeetCode CH](https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements/) (Medium)

-   Tags: array, union find, sorting
## 564. Find the Closest Palindrome

-   [LeetCode](https://leetcode.com/problems/find-the-closest-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/find-the-closest-palindrome/) (Hard)

-   Tags: math, string
## 1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits

-   [LeetCode](https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/) | [LeetCode CH](https://leetcode.cn/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/) (Hard)

-   Tags: string, greedy, binary indexed tree, segment tree
## 2663. Lexicographically Smallest Beautiful String

-   [LeetCode](https://leetcode.com/problems/lexicographically-smallest-beautiful-string/) | [LeetCode CH](https://leetcode.cn/problems/lexicographically-smallest-beautiful-string/) (Hard)

-   Tags: string, greedy
## 3302. Find the Lexicographically Smallest Valid Sequence

-   [LeetCode](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/) | [LeetCode CH](https://leetcode.cn/problems/find-the-lexicographically-smallest-valid-sequence/) (Medium)

-   Tags: two pointers, string, dynamic programming, greedy
## 555. Split Concatenated Strings

-   [LeetCode](https://leetcode.com/problems/split-concatenated-strings/) | [LeetCode CH](https://leetcode.cn/problems/split-concatenated-strings/) (Medium)

-   Tags: array, string, greedy
## 3088. Make String Anti-palindrome

-   [LeetCode](https://leetcode.com/problems/make-string-anti-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/make-string-anti-palindrome/) (Hard)

-   Tags: string, greedy, sorting, counting sort
