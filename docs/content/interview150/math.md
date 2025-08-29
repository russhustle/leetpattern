---
comments: True
---

# Math

## Table of Contents

- [x] [9. Palindrome Number](https://leetcode.cn/problems/palindrome-number/) (Easy)
- [x] [66. Plus One](https://leetcode.cn/problems/plus-one/) (Easy)
- [ ] [172. Factorial Trailing Zeroes](https://leetcode.cn/problems/factorial-trailing-zeroes/) (Medium)
- [x] [69. Sqrt(x)](https://leetcode.cn/problems/sqrtx/) (Easy)
- [x] [50. Pow(x, n)](https://leetcode.cn/problems/powx-n/) (Medium)
- [x] [149. Max Points on a Line](https://leetcode.cn/problems/max-points-on-a-line/) (Hard)

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

## 66. Plus One

-   [LeetCode](https://leetcode.com/problems/plus-one/) | [LeetCode CH](https://leetcode.cn/problems/plus-one/) (Easy)

-   Tags: array, math
```python title="66. Plus One - Python Solution"
from typing import List


# Math
def plusOne(digits: List[int]) -> List[int]:
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    return [1] + digits


digits = [4, 3, 2, 1]
print(plusOne(digits))  # [4, 3, 2, 2]

```

## 172. Factorial Trailing Zeroes

-   [LeetCode](https://leetcode.com/problems/factorial-trailing-zeroes/) | [LeetCode CH](https://leetcode.cn/problems/factorial-trailing-zeroes/) (Medium)

-   Tags: math
## 69. Sqrt(x)

-   [LeetCode](https://leetcode.com/problems/sqrtx/) | [LeetCode CH](https://leetcode.cn/problems/sqrtx/) (Easy)

-   Tags: math, binary search
```python title="69. Sqrt(x) - Python Solution"
# Left Right Pointers
def mySqrt(x: int) -> int:
    """Returns the square root of a number."""
    if x < 2:
        return x

    left, right = 0, x // 2

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1


x = 8
print(mySqrt(x))  # 2

```

## 50. Pow(x, n)

-   [LeetCode](https://leetcode.com/problems/powx-n/) | [LeetCode CH](https://leetcode.cn/problems/powx-n/) (Medium)

-   Tags: math, recursion
```python title="50. Pow(x, n) - Python Solution"
# Iterative
def myPowIterative(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    cur = x

    while n > 0:
        if n % 2 == 1:
            result *= cur

        cur *= cur
        n //= 2

    return result


# Recursive
def myPowRecursive(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n

    if n % 2 == 0:
        return myPowRecursive(x * x, n // 2)
    else:
        return x * myPowRecursive(x * x, n // 2)


x = 2.00000
n = 10
print(myPowIterative(x, n))  # 1024.0
print(myPowRecursive(x, n))  # 1024.0

```

## 149. Max Points on a Line

-   [LeetCode](https://leetcode.com/problems/max-points-on-a-line/) | [LeetCode CH](https://leetcode.cn/problems/max-points-on-a-line/) (Hard)

-   Tags: array, hash table, math, geometry
```python title="149. Max Points on a Line - Python Solution"
from collections import defaultdict
from typing import List


# GCD
def maxPoints(points: List[List[int]]) -> int:
    n = len(points)
    if n <= 2:
        return n

    res = 0

    for i in range(n - 1):
        x1, y1 = points[i]
        cnt = defaultdict(int)

        for j in range(i + 1, n):
            x2, y2 = points[j]
            g = "inf" if x1 == x2 else (y2 - y1) / (x2 - x1)
            cnt[g] += 1

        res = max(res, 1 + max(cnt.values()))

    return res


points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
print(maxPoints(points))  # 4

```
