---
comments: True
---

# Enumerate Middle

## Table of Contents

- [ ] [2909. Minimum Sum of Mountain Triplets II](https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-ii/) (Medium)
- [ ] [1930. Unique Length-3 Palindromic Subsequences](https://leetcode.cn/problems/unique-length-3-palindromic-subsequences/) (Medium)
- [ ] [3128. Right Triangles](https://leetcode.cn/problems/right-triangles/) (Medium)
- [x] [2874. Maximum Value of an Ordered Triplet II](https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-ii/) (Medium)
- [ ] [447. Number of Boomerangs](https://leetcode.cn/problems/number-of-boomerangs/) (Medium)
- [x] [456. 132 Pattern](https://leetcode.cn/problems/132-pattern/) (Medium)
- [ ] [3067. Count Pairs of Connectable Servers in a Weighted Tree Network](https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/) (Medium)
- [ ] [3455. Shortest Matching Substring](https://leetcode.cn/problems/shortest-matching-substring/) (Hard)
- [ ] [2242. Maximum Score of a Node Sequence](https://leetcode.cn/problems/maximum-score-of-a-node-sequence/) (Hard)
- [ ] [2867. Count Valid Paths in a Tree](https://leetcode.cn/problems/count-valid-paths-in-a-tree/) (Hard)
- [x] [2552. Count Increasing Quadruplets](https://leetcode.cn/problems/count-increasing-quadruplets/) (Hard)
- [ ] [3257. Maximum Value Sum by Placing Three Rooks II](https://leetcode.cn/problems/maximum-value-sum-by-placing-three-rooks-ii/) (Hard)
- [ ] [3073. Maximum Increasing Triplet Value](https://leetcode.cn/problems/maximum-increasing-triplet-value/) (Medium) 👑

## 2909. Minimum Sum of Mountain Triplets II

-   [LeetCode](https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/) | [LeetCode CH](https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-ii/) (Medium)

-   Tags: array
## 1930. Unique Length-3 Palindromic Subsequences

-   [LeetCode](https://leetcode.com/problems/unique-length-3-palindromic-subsequences/) | [LeetCode CH](https://leetcode.cn/problems/unique-length-3-palindromic-subsequences/) (Medium)

-   Tags: hash table, string, bit manipulation, prefix sum
## 3128. Right Triangles

-   [LeetCode](https://leetcode.com/problems/right-triangles/) | [LeetCode CH](https://leetcode.cn/problems/right-triangles/) (Medium)

-   Tags: array, hash table, math, combinatorics, counting
## 2874. Maximum Value of an Ordered Triplet II

-   [LeetCode](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/) | [LeetCode CH](https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-ii/) (Medium)

-   Tags: array

```python title="2874. Maximum Value of an Ordered Triplet II - Python Solution"
from typing import List


def maximumTripletValue(nums: List[int]) -> int:
    res = 0
    max_diff = 0
    max_prev = 0

    for num in nums:
        res = max(res, max_diff * num)
        max_diff = max(max_diff, max_prev - num)
        max_prev = max(max_prev, num)

    return res


if __name__ == "__main__":
    nums = [12, 6, 1, 2, 7]
    print(maximumTripletValue(nums))  # 77

```

## 447. Number of Boomerangs

-   [LeetCode](https://leetcode.com/problems/number-of-boomerangs/) | [LeetCode CH](https://leetcode.cn/problems/number-of-boomerangs/) (Medium)

-   Tags: array, hash table, math
## 456. 132 Pattern

-   [LeetCode](https://leetcode.com/problems/132-pattern/) | [LeetCode CH](https://leetcode.cn/problems/132-pattern/) (Medium)

-   Tags: array, binary search, stack, monotonic stack, ordered set

```python title="456. 132 Pattern - Python Solution"
from typing import List


# Monotonic Stack
def find132pattern(nums: List[int]) -> bool:
    n = len(nums)
    if n < 3:
        return False

    stack = []
    second_max = float("-inf")

    for i in range(n - 1, -1, -1):
        if nums[i] < second_max:
            return True

        while stack and stack[-1] < nums[i]:
            second_max = stack.pop()

        stack.append(nums[i])

    return False


nums = [-1, 3, 2, 0]
print(find132pattern(nums))  # True

```

## 3067. Count Pairs of Connectable Servers in a Weighted Tree Network

-   [LeetCode](https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/) | [LeetCode CH](https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/) (Medium)

-   Tags: array, tree, depth first search
## 3455. Shortest Matching Substring

-   [LeetCode](https://leetcode.com/problems/shortest-matching-substring/) | [LeetCode CH](https://leetcode.cn/problems/shortest-matching-substring/) (Hard)

-   Tags: two pointers, string, binary search, string matching
## 2242. Maximum Score of a Node Sequence

-   [LeetCode](https://leetcode.com/problems/maximum-score-of-a-node-sequence/) | [LeetCode CH](https://leetcode.cn/problems/maximum-score-of-a-node-sequence/) (Hard)

-   Tags: array, graph, sorting, enumeration
## 2867. Count Valid Paths in a Tree

-   [LeetCode](https://leetcode.com/problems/count-valid-paths-in-a-tree/) | [LeetCode CH](https://leetcode.cn/problems/count-valid-paths-in-a-tree/) (Hard)

-   Tags: math, dynamic programming, tree, depth first search, number theory
## 2552. Count Increasing Quadruplets

-   [LeetCode](https://leetcode.com/problems/count-increasing-quadruplets/) | [LeetCode CH](https://leetcode.cn/problems/count-increasing-quadruplets/) (Hard)

-   Tags: array, dynamic programming, binary indexed tree, enumeration, prefix sum

```python title="2552. Count Increasing Quadruplets - Python Solution"
from typing import List


# DP
def countQuadruplets(nums: List[int]) -> int:
    n = len(nums)
    great = [[0] * (n + 1) for _ in range(n)]
    less = [0 for _ in range(n + 1)]

    for k in range(n - 2, 1, -1):
        great[k] = great[k + 1].copy()
        for x in range(1, nums[k + 1]):
            great[k][x] += 1

    ans = 0

    for j in range(1, n - 1):
        for x in range(nums[j - 1] + 1, n + 1):
            less[x] += 1
        for k in range(j + 1, n - 1):
            if nums[j] > nums[k]:
                ans += less[nums[k]] * great[k][nums[j]]
    return ans


nums = [1, 3, 2, 4, 5]
print(countQuadruplets(nums))  # 2

```

## 3257. Maximum Value Sum by Placing Three Rooks II

-   [LeetCode](https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/) | [LeetCode CH](https://leetcode.cn/problems/maximum-value-sum-by-placing-three-rooks-ii/) (Hard)

-   Tags: array, dynamic programming, matrix, enumeration
## 3073. Maximum Increasing Triplet Value

-   [LeetCode](https://leetcode.com/problems/maximum-increasing-triplet-value/) | [LeetCode CH](https://leetcode.cn/problems/maximum-increasing-triplet-value/) (Medium)

-   Tags: array, ordered set
