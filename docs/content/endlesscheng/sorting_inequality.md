---
comments: True
---

# Sorting Inequality

## Table of Contents

- [ ] [2285. Maximum Total Importance of Roads](https://leetcode.cn/problems/maximum-total-importance-of-roads/) (Medium)
- [ ] [3016. Minimum Number of Pushes to Type Word II](https://leetcode.cn/problems/minimum-number-of-pushes-to-type-word-ii/) (Medium)
- [ ] [1402. Reducing Dishes](https://leetcode.cn/problems/reducing-dishes/) (Hard)
- [ ] [2931. Maximum Spending After Buying Items](https://leetcode.cn/problems/maximum-spending-after-buying-items/) (Hard)
- [x] [1589. Maximum Sum Obtained of Any Permutation](https://leetcode.cn/problems/maximum-sum-obtained-of-any-permutation/) (Medium)
- [ ] [1874. Minimize Product Sum of Two Arrays](https://leetcode.cn/problems/minimize-product-sum-of-two-arrays/) (Medium) 👑
- [ ] [2268. Minimum Number of Keypresses](https://leetcode.cn/problems/minimum-number-of-keypresses/) (Medium) 👑

## 2285. Maximum Total Importance of Roads

-   [LeetCode](https://leetcode.com/problems/maximum-total-importance-of-roads/) | [LeetCode CH](https://leetcode.cn/problems/maximum-total-importance-of-roads/) (Medium)

-   Tags: greedy, graph, sorting, heap priority queue

## 3016. Minimum Number of Pushes to Type Word II

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-pushes-to-type-word-ii/) (Medium)

-   Tags: hash table, string, greedy, sorting, counting

## 1402. Reducing Dishes

-   [LeetCode](https://leetcode.com/problems/reducing-dishes/) | [LeetCode CH](https://leetcode.cn/problems/reducing-dishes/) (Hard)

-   Tags: array, dynamic programming, greedy, sorting

## 2931. Maximum Spending After Buying Items

-   [LeetCode](https://leetcode.com/problems/maximum-spending-after-buying-items/) | [LeetCode CH](https://leetcode.cn/problems/maximum-spending-after-buying-items/) (Hard)

-   Tags: array, greedy, sorting, heap priority queue, matrix

## 1589. Maximum Sum Obtained of Any Permutation

-   [LeetCode](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/) | [LeetCode CH](https://leetcode.cn/problems/maximum-sum-obtained-of-any-permutation/) (Medium)

-   Tags: array, greedy, sorting, prefix sum

```python title="1589. Maximum Sum Obtained of Any Permutation - Python Solution"
from typing import List


# Greedy
def maxSumRangeQuery(nums: List[int], requests: List[List[int]]) -> int:
    n = len(nums)
    freq = [0 for _ in range(n + 1)]

    for start, end in requests:
        freq[start] += 1
        if end + 1 < n:
            freq[end + 1] -= 1

    for i in range(1, n):
        freq[i] += freq[i - 1]

    freq.pop()

    freq.sort(reverse=True)
    nums.sort(reverse=True)

    max_sum = 0
    mod = 10**9 + 7

    for i, j in zip(nums, freq):
        max_sum += i * j
        max_sum %= mod

    return max_sum


nums = [1, 2, 3, 4, 5]
requests = [[1, 3], [0, 1]]
print(maxSumRangeQuery(nums, requests))  # 19

```

## 1874. Minimize Product Sum of Two Arrays

-   [LeetCode](https://leetcode.com/problems/minimize-product-sum-of-two-arrays/) | [LeetCode CH](https://leetcode.cn/problems/minimize-product-sum-of-two-arrays/) (Medium)

-   Tags: array, greedy, sorting

## 2268. Minimum Number of Keypresses

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-keypresses/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-keypresses/) (Medium)

-   Tags: hash table, string, greedy, sorting, counting
