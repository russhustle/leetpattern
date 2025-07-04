---
comments: True
---

# Factors

## Table of Contents

- [ ] [2427. Number of Common Factors](https://leetcode.cn/problems/number-of-common-factors/) (Easy)
- [ ] [1952. Three Divisors](https://leetcode.cn/problems/three-divisors/) (Easy)
- [ ] [1492. The kth Factor of n](https://leetcode.cn/problems/the-kth-factor-of-n/) (Medium)
- [ ] [507. Perfect Number](https://leetcode.cn/problems/perfect-number/) (Easy)
- [ ] [1390. Four Divisors](https://leetcode.cn/problems/four-divisors/) (Medium)
- [ ] [1362. Closest Divisors](https://leetcode.cn/problems/closest-divisors/) (Medium)
- [ ] [829. Consecutive Numbers Sum](https://leetcode.cn/problems/consecutive-numbers-sum/) (Hard)
- [ ] [3447. Assign Elements to Groups with Constraints](https://leetcode.cn/problems/assign-elements-to-groups-with-constraints/) (Medium)
- [ ] [3164. Find the Number of Good Pairs II](https://leetcode.cn/problems/find-the-number-of-good-pairs-ii/) (Medium)
- [x] [952. Largest Component Size by Common Factor](https://leetcode.cn/problems/largest-component-size-by-common-factor/) (Hard)
- [ ] [1627. Graph Connectivity With Threshold](https://leetcode.cn/problems/graph-connectivity-with-threshold/) (Hard)
- [ ] [2198. Number of Single Divisor Triplets](https://leetcode.cn/problems/number-of-single-divisor-triplets/) (Medium) 👑
- [ ] [625. Minimum Factorization](https://leetcode.cn/problems/minimum-factorization/) (Medium) 👑
- [ ] [2847. Smallest Number With Given Digit Product](https://leetcode.cn/problems/smallest-number-with-given-digit-product/) (Medium) 👑

## 2427. Number of Common Factors

-   [LeetCode](https://leetcode.com/problems/number-of-common-factors/) | [LeetCode CH](https://leetcode.cn/problems/number-of-common-factors/) (Easy)

-   Tags: math, enumeration, number theory
## 1952. Three Divisors

-   [LeetCode](https://leetcode.com/problems/three-divisors/) | [LeetCode CH](https://leetcode.cn/problems/three-divisors/) (Easy)

-   Tags: math, enumeration, number theory
## 1492. The kth Factor of n

-   [LeetCode](https://leetcode.com/problems/the-kth-factor-of-n/) | [LeetCode CH](https://leetcode.cn/problems/the-kth-factor-of-n/) (Medium)

-   Tags: math, number theory
## 507. Perfect Number

-   [LeetCode](https://leetcode.com/problems/perfect-number/) | [LeetCode CH](https://leetcode.cn/problems/perfect-number/) (Easy)

-   Tags: math
## 1390. Four Divisors

-   [LeetCode](https://leetcode.com/problems/four-divisors/) | [LeetCode CH](https://leetcode.cn/problems/four-divisors/) (Medium)

-   Tags: array, math
## 1362. Closest Divisors

-   [LeetCode](https://leetcode.com/problems/closest-divisors/) | [LeetCode CH](https://leetcode.cn/problems/closest-divisors/) (Medium)

-   Tags: math
## 829. Consecutive Numbers Sum

-   [LeetCode](https://leetcode.com/problems/consecutive-numbers-sum/) | [LeetCode CH](https://leetcode.cn/problems/consecutive-numbers-sum/) (Hard)

-   Tags: math, enumeration
## 3447. Assign Elements to Groups with Constraints

-   [LeetCode](https://leetcode.com/problems/assign-elements-to-groups-with-constraints/) | [LeetCode CH](https://leetcode.cn/problems/assign-elements-to-groups-with-constraints/) (Medium)

-   Tags: array, hash table
## 3164. Find the Number of Good Pairs II

-   [LeetCode](https://leetcode.com/problems/find-the-number-of-good-pairs-ii/) | [LeetCode CH](https://leetcode.cn/problems/find-the-number-of-good-pairs-ii/) (Medium)

-   Tags: array, hash table
## 952. Largest Component Size by Common Factor

-   [LeetCode](https://leetcode.com/problems/largest-component-size-by-common-factor/) | [LeetCode CH](https://leetcode.cn/problems/largest-component-size-by-common-factor/) (Hard)

-   Tags: array, hash table, math, union find, number theory

```python title="952. Largest Component Size by Common Factor - Python Solution"
from collections import defaultdict
from typing import List


# Union Find
def largestComponentSize(nums: List[int]) -> int:
    par = {i: i for i in nums}
    rank = {i: 0 for i in nums}

    def find(n):
        p = par[n]
        while par[p] != p:
            par[p] = par[par[p]]
            p = par[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 != p2:
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1

    def prime_factors(n):
        """Return the prime factors of n."""
        i = 2
        factors = set()
        while i * i <= n:
            while (n % i) == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors

    factor_map = defaultdict(list)  # factor -> [nums]
    for num in nums:
        factors = prime_factors(num)
        for factor in factors:
            factor_map[factor].append(num)

    for factor, group in factor_map.items():
        for i in range(1, len(group)):
            union(group[0], group[i])

    sizes = defaultdict(int)  # component root -> size
    for num in nums:
        root = find(num)
        sizes[root] += 1

    return max(sizes.values())


nums = [20, 50, 9, 63]
print(largestComponentSize(nums))  # 2

```

## 1627. Graph Connectivity With Threshold

-   [LeetCode](https://leetcode.com/problems/graph-connectivity-with-threshold/) | [LeetCode CH](https://leetcode.cn/problems/graph-connectivity-with-threshold/) (Hard)

-   Tags: array, math, union find, number theory
## 2198. Number of Single Divisor Triplets

-   [LeetCode](https://leetcode.com/problems/number-of-single-divisor-triplets/) | [LeetCode CH](https://leetcode.cn/problems/number-of-single-divisor-triplets/) (Medium)

-   Tags: math
## 625. Minimum Factorization

-   [LeetCode](https://leetcode.com/problems/minimum-factorization/) | [LeetCode CH](https://leetcode.cn/problems/minimum-factorization/) (Medium)

-   Tags: math, greedy
## 2847. Smallest Number With Given Digit Product

-   [LeetCode](https://leetcode.com/problems/smallest-number-with-given-digit-product/) | [LeetCode CH](https://leetcode.cn/problems/smallest-number-with-given-digit-product/) (Medium)

-   Tags: math, greedy
