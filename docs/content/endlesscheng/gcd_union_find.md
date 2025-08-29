---
comments: True
---

# GCD Union Find

## Table of Contents

- [ ] [2709. Greatest Common Divisor Traversal](https://leetcode.cn/problems/greatest-common-divisor-traversal/) (Hard)
- [ ] [1627. Graph Connectivity With Threshold](https://leetcode.cn/problems/graph-connectivity-with-threshold/) (Hard)
- [x] [952. Largest Component Size by Common Factor](https://leetcode.cn/problems/largest-component-size-by-common-factor/) (Hard)
- [ ] [1998. GCD Sort of an Array](https://leetcode.cn/problems/gcd-sort-of-an-array/) (Hard)
- [ ] [3378. Count Connected Components in LCM Graph](https://leetcode.cn/problems/count-connected-components-in-lcm-graph/) (Hard)

## 2709. Greatest Common Divisor Traversal

-   [LeetCode](https://leetcode.com/problems/greatest-common-divisor-traversal/) | [LeetCode CH](https://leetcode.cn/problems/greatest-common-divisor-traversal/) (Hard)

-   Tags: array, math, union find, number theory
## 1627. Graph Connectivity With Threshold

-   [LeetCode](https://leetcode.com/problems/graph-connectivity-with-threshold/) | [LeetCode CH](https://leetcode.cn/problems/graph-connectivity-with-threshold/) (Hard)

-   Tags: array, math, union find, number theory
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

## 1998. GCD Sort of an Array

-   [LeetCode](https://leetcode.com/problems/gcd-sort-of-an-array/) | [LeetCode CH](https://leetcode.cn/problems/gcd-sort-of-an-array/) (Hard)

-   Tags: array, math, union find, sorting, number theory
## 3378. Count Connected Components in LCM Graph

-   [LeetCode](https://leetcode.com/problems/count-connected-components-in-lcm-graph/) | [LeetCode CH](https://leetcode.cn/problems/count-connected-components-in-lcm-graph/) (Hard)

-   Tags: array, hash table, math, union find, number theory
