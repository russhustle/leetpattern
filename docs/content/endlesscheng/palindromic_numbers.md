---
comments: True
---

# Palindromic Numbers

## Table of Contents

- [x] [9. Palindrome Number](https://leetcode.cn/problems/palindrome-number/) (Easy)
- [ ] [2396. Strictly Palindromic Number](https://leetcode.cn/problems/strictly-palindromic-number/) (Medium)
- [ ] [2217. Find Palindrome With Fixed Length](https://leetcode.cn/problems/find-palindrome-with-fixed-length/) (Medium)
- [ ] [866. Prime Palindrome](https://leetcode.cn/problems/prime-palindrome/) (Medium)
- [ ] [2967. Minimum Cost to Make Array Equalindromic](https://leetcode.cn/problems/minimum-cost-to-make-array-equalindromic/) (Medium)
- [ ] [906. Super Palindromes](https://leetcode.cn/problems/super-palindromes/) (Hard)
- [ ] [2081. Sum of k-Mirror Numbers](https://leetcode.cn/problems/sum-of-k-mirror-numbers/) (Hard)
- [ ] [3260. Find the Largest Palindrome Divisible by K](https://leetcode.cn/problems/find-the-largest-palindrome-divisible-by-k/) (Hard)
- [ ] [3272. Find the Count of Good Integers](https://leetcode.cn/problems/find-the-count-of-good-integers/) (Hard)
- [ ] [564. Find the Closest Palindrome](https://leetcode.cn/problems/find-the-closest-palindrome/) (Hard)
- [ ] [479. Largest Palindrome Product](https://leetcode.cn/problems/largest-palindrome-product/) (Hard)

## 9. Palindrome Number

-   [LeetCode](https://leetcode.com/problems/palindrome-number/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-number/) (Easy)

-   Tags: math
-   Return true if the given number is a palindrome. Otherwise, return false.

```python title="9. Palindrome Number - Python Solution"
# Reverse
def isPalindromeReverse(x: int) -> bool:
    if x < 0:
        return False

    return str(x) == str(x)[::-1]


# Left Right Pointers
def isPalindromeLR(x: int) -> bool:
    if x < 0:
        return False

    x = list(str(x))  # 121 -> ['1', '2', '1']

    left, right = 0, len(x) - 1

    while left < right:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1

    return True


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |  Reverse   |  O(N)  |   O(N)  |
# | Left Right |  O(N)  |   O(1)  |
# |------------|--------|---------|


x = 121
print(isPalindromeReverse(x))  # True
print(isPalindromeLR(x))  # True

```

## 2396. Strictly Palindromic Number

-   [LeetCode](https://leetcode.com/problems/strictly-palindromic-number/) | [LeetCode CH](https://leetcode.cn/problems/strictly-palindromic-number/) (Medium)

-   Tags: math, two pointers, brainteaser
## 2217. Find Palindrome With Fixed Length

-   [LeetCode](https://leetcode.com/problems/find-palindrome-with-fixed-length/) | [LeetCode CH](https://leetcode.cn/problems/find-palindrome-with-fixed-length/) (Medium)

-   Tags: array, math
## 866. Prime Palindrome

-   [LeetCode](https://leetcode.com/problems/prime-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/prime-palindrome/) (Medium)

-   Tags: math, number theory
## 2967. Minimum Cost to Make Array Equalindromic

-   [LeetCode](https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-to-make-array-equalindromic/) (Medium)

-   Tags: array, math, binary search, greedy, sorting
## 906. Super Palindromes

-   [LeetCode](https://leetcode.com/problems/super-palindromes/) | [LeetCode CH](https://leetcode.cn/problems/super-palindromes/) (Hard)

-   Tags: math, string, enumeration
## 2081. Sum of k-Mirror Numbers

-   [LeetCode](https://leetcode.com/problems/sum-of-k-mirror-numbers/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-k-mirror-numbers/) (Hard)

-   Tags: math, enumeration
## 3260. Find the Largest Palindrome Divisible by K

-   [LeetCode](https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/) | [LeetCode CH](https://leetcode.cn/problems/find-the-largest-palindrome-divisible-by-k/) (Hard)

-   Tags: math, string, dynamic programming, greedy, number theory
## 3272. Find the Count of Good Integers

-   [LeetCode](https://leetcode.com/problems/find-the-count-of-good-integers/) | [LeetCode CH](https://leetcode.cn/problems/find-the-count-of-good-integers/) (Hard)

-   Tags: hash table, math, combinatorics, enumeration
## 564. Find the Closest Palindrome

-   [LeetCode](https://leetcode.com/problems/find-the-closest-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/find-the-closest-palindrome/) (Hard)

-   Tags: math, string
## 479. Largest Palindrome Product

-   [LeetCode](https://leetcode.com/problems/largest-palindrome-product/) | [LeetCode CH](https://leetcode.cn/problems/largest-palindrome-product/) (Hard)

-   Tags: math, enumeration
