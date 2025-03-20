---
comments: True
---

# Greatest Common Divisor

## Table of Contents

- [ ] [1979. Find Greatest Common Divisor of Array](https://leetcode.cn/problems/find-greatest-common-divisor-of-array/) (Easy)
- [ ] [2807. Insert Greatest Common Divisors in Linked List](https://leetcode.cn/problems/insert-greatest-common-divisors-in-linked-list/) (Medium)
- [ ] [914. X of a Kind in a Deck of Cards](https://leetcode.cn/problems/x-of-a-kind-in-a-deck-of-cards/) (Easy)
- [ ] [1071. Greatest Common Divisor of Strings](https://leetcode.cn/problems/greatest-common-divisor-of-strings/) (Easy)
- [ ] [2344. Minimum Deletions to Make Array Divisible](https://leetcode.cn/problems/minimum-deletions-to-make-array-divisible/) (Hard)
- [ ] [365. Water and Jug Problem](https://leetcode.cn/problems/water-and-jug-problem/) (Medium)
- [ ] [858. Mirror Reflection](https://leetcode.cn/problems/mirror-reflection/) (Medium)
- [ ] [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](https://leetcode.cn/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/) (Medium)
- [ ] [1250. Check If It Is a Good Array](https://leetcode.cn/problems/check-if-it-is-a-good-array/) (Hard)
- [x] [149. Max Points on a Line](https://leetcode.cn/problems/max-points-on-a-line/) (Hard)
- [ ] [2607. Make K-Subarray Sums Equal](https://leetcode.cn/problems/make-k-subarray-sums-equal/) (Medium)
- [ ] [2447. Number of Subarrays With GCD Equal to K](https://leetcode.cn/problems/number-of-subarrays-with-gcd-equal-to-k/) (Medium)
- [ ] [2543. Check if Point Is Reachable](https://leetcode.cn/problems/check-if-point-is-reachable/) (Hard)
- [ ] [2183. Count Array Pairs Divisible by K](https://leetcode.cn/problems/count-array-pairs-divisible-by-k/) (Hard)
- [ ] [3312. Sorted GCD Pair Queries](https://leetcode.cn/problems/sorted-gcd-pair-queries/) (Hard)
- [ ] [1819. Number of Different Subsequences GCDs](https://leetcode.cn/problems/number-of-different-subsequences-gcds/) (Hard)
- [ ] [2436. Minimum Split Into Subarrays With GCD Greater Than One](https://leetcode.cn/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/) (Medium) 👑
- [ ] [2464. Minimum Subarrays in a Valid Split](https://leetcode.cn/problems/minimum-subarrays-in-a-valid-split/) (Medium) 👑
- [ ] [2941. Maximum GCD-Sum of a Subarray](https://leetcode.cn/problems/maximum-gcd-sum-of-a-subarray/) (Hard) 👑

## 1979. Find Greatest Common Divisor of Array

-   [LeetCode](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) | [LeetCode CH](https://leetcode.cn/problems/find-greatest-common-divisor-of-array/) (Easy)

-   Tags: array, math, number theory

## 2807. Insert Greatest Common Divisors in Linked List

-   [LeetCode](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/insert-greatest-common-divisors-in-linked-list/) (Medium)

-   Tags: linked list, math, number theory

## 914. X of a Kind in a Deck of Cards

-   [LeetCode](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/) | [LeetCode CH](https://leetcode.cn/problems/x-of-a-kind-in-a-deck-of-cards/) (Easy)

-   Tags: array, hash table, math, counting, number theory

## 1071. Greatest Common Divisor of Strings

-   [LeetCode](https://leetcode.com/problems/greatest-common-divisor-of-strings/) | [LeetCode CH](https://leetcode.cn/problems/greatest-common-divisor-of-strings/) (Easy)

-   Tags: math, string

## 2344. Minimum Deletions to Make Array Divisible

-   [LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/) | [LeetCode CH](https://leetcode.cn/problems/minimum-deletions-to-make-array-divisible/) (Hard)

-   Tags: array, math, sorting, heap priority queue, number theory

## 365. Water and Jug Problem

-   [LeetCode](https://leetcode.com/problems/water-and-jug-problem/) | [LeetCode CH](https://leetcode.cn/problems/water-and-jug-problem/) (Medium)

-   Tags: math, depth first search, breadth first search

## 858. Mirror Reflection

-   [LeetCode](https://leetcode.com/problems/mirror-reflection/) | [LeetCode CH](https://leetcode.cn/problems/mirror-reflection/) (Medium)

-   Tags: math, geometry, number theory

## 2654. Minimum Number of Operations to Make All Array Elements Equal to 1

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/) (Medium)

-   Tags: array, math, number theory

## 1250. Check If It Is a Good Array

-   [LeetCode](https://leetcode.com/problems/check-if-it-is-a-good-array/) | [LeetCode CH](https://leetcode.cn/problems/check-if-it-is-a-good-array/) (Hard)

-   Tags: array, math, number theory

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

## 2607. Make K-Subarray Sums Equal

-   [LeetCode](https://leetcode.com/problems/make-k-subarray-sums-equal/) | [LeetCode CH](https://leetcode.cn/problems/make-k-subarray-sums-equal/) (Medium)

-   Tags: array, math, greedy, sorting, number theory

## 2447. Number of Subarrays With GCD Equal to K

-   [LeetCode](https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/) | [LeetCode CH](https://leetcode.cn/problems/number-of-subarrays-with-gcd-equal-to-k/) (Medium)

-   Tags: array, math, number theory

## 2543. Check if Point Is Reachable

-   [LeetCode](https://leetcode.com/problems/check-if-point-is-reachable/) | [LeetCode CH](https://leetcode.cn/problems/check-if-point-is-reachable/) (Hard)

-   Tags: math, number theory

## 2183. Count Array Pairs Divisible by K

-   [LeetCode](https://leetcode.com/problems/count-array-pairs-divisible-by-k/) | [LeetCode CH](https://leetcode.cn/problems/count-array-pairs-divisible-by-k/) (Hard)

-   Tags: array, math, number theory

## 3312. Sorted GCD Pair Queries

-   [LeetCode](https://leetcode.com/problems/sorted-gcd-pair-queries/) | [LeetCode CH](https://leetcode.cn/problems/sorted-gcd-pair-queries/) (Hard)

-   Tags: array, hash table, math, binary search, combinatorics, counting, number theory, prefix sum

## 1819. Number of Different Subsequences GCDs

-   [LeetCode](https://leetcode.com/problems/number-of-different-subsequences-gcds/) | [LeetCode CH](https://leetcode.cn/problems/number-of-different-subsequences-gcds/) (Hard)

-   Tags: array, math, counting, number theory

## 2436. Minimum Split Into Subarrays With GCD Greater Than One

-   [LeetCode](https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/) | [LeetCode CH](https://leetcode.cn/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/) (Medium)

-   Tags: array, math, dynamic programming, greedy, number theory

## 2464. Minimum Subarrays in a Valid Split

-   [LeetCode](https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/) | [LeetCode CH](https://leetcode.cn/problems/minimum-subarrays-in-a-valid-split/) (Medium)

-   Tags: array, math, dynamic programming, number theory

## 2941. Maximum GCD-Sum of a Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-gcd-sum-of-a-subarray/) (Hard)

-   Tags: array, math, binary search, number theory
