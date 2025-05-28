---
comments: True
---

# Two Sequences Two Pointers

## Table of Contents

- [ ] [2540. Minimum Common Value](https://leetcode.cn/problems/minimum-common-value/) (Easy)
- [x] [88. Merge Sorted Array](https://leetcode.cn/problems/merge-sorted-array/) (Easy)
- [ ] [2570. Merge Two 2D Arrays by Summing Values](https://leetcode.cn/problems/merge-two-2d-arrays-by-summing-values/) (Easy)
- [ ] [1855. Maximum Distance Between a Pair of Values](https://leetcode.cn/problems/maximum-distance-between-a-pair-of-values/) (Medium)
- [x] [1385. Find the Distance Value Between Two Arrays](https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/) (Easy)
- [ ] [925. Long Pressed Name](https://leetcode.cn/problems/long-pressed-name/) (Easy)
- [ ] [809. Expressive Words](https://leetcode.cn/problems/expressive-words/) (Medium)
- [ ] [2337. Move Pieces to Obtain a String](https://leetcode.cn/problems/move-pieces-to-obtain-a-string/) (Medium)
- [ ] [777. Swap Adjacent in LR String](https://leetcode.cn/problems/swap-adjacent-in-lr-string/) (Medium)
- [x] [844. Backspace String Compare](https://leetcode.cn/problems/backspace-string-compare/) (Easy)
- [ ] [986. Interval List Intersections](https://leetcode.cn/problems/interval-list-intersections/) (Medium)
- [ ] [1537. Get the Maximum Score](https://leetcode.cn/problems/get-the-maximum-score/) (Hard)
- [ ] [244. Shortest Word Distance II](https://leetcode.cn/problems/shortest-word-distance-ii/) (Medium) 👑
- [ ] [2838. Maximum Coins Heroes Can Collect](https://leetcode.cn/problems/maximum-coins-heroes-can-collect/) (Medium) 👑
- [ ] [1229. Meeting Scheduler](https://leetcode.cn/problems/meeting-scheduler/) (Medium) 👑
- [ ] [1570. Dot Product of Two Sparse Vectors](https://leetcode.cn/problems/dot-product-of-two-sparse-vectors/) (Medium) 👑
- [ ] [1868. Product of Two Run-Length Encoded Arrays](https://leetcode.cn/problems/product-of-two-run-length-encoded-arrays/) (Medium) 👑

## 2540. Minimum Common Value

-   [LeetCode](https://leetcode.com/problems/minimum-common-value/) | [LeetCode CH](https://leetcode.cn/problems/minimum-common-value/) (Easy)

-   Tags: array, hash table, two pointers, binary search
## 88. Merge Sorted Array

-   [LeetCode](https://leetcode.com/problems/merge-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/merge-sorted-array/) (Easy)

-   Tags: array, two pointers, sorting

```python title="88. Merge Sorted Array - Python Solution"
from typing import List


# Left Right Pointers
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """Merges two sorted arrays in-place."""
    p1, p2, t = m - 1, n - 1, m + n - 1

    while p1 >= 0 or p2 >= 0:
        if p1 == -1:
            nums1[t] = nums2[p2]
            p2 -= 1
        elif p2 == -1:
            nums1[t] = nums1[p1]
            p1 -= 1
        elif nums1[p1] > nums2[p2]:
            nums1[t] = nums1[p1]
            p1 -= 1
        else:
            nums1[t] = nums2[p2]
            p2 -= 1

        t -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # [1, 2, 2, 3, 5, 6]

```

## 2570. Merge Two 2D Arrays by Summing Values

-   [LeetCode](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/) | [LeetCode CH](https://leetcode.cn/problems/merge-two-2d-arrays-by-summing-values/) (Easy)

-   Tags: array, hash table, two pointers
## 1855. Maximum Distance Between a Pair of Values

-   [LeetCode](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/) | [LeetCode CH](https://leetcode.cn/problems/maximum-distance-between-a-pair-of-values/) (Medium)

-   Tags: array, two pointers, binary search
## 1385. Find the Distance Value Between Two Arrays

-   [LeetCode](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/) | [LeetCode CH](https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/) (Easy)

-   Tags: array, two pointers, binary search, sorting

```python title="1385. Find the Distance Value Between Two Arrays - Python Solution"
from bisect import bisect_left
from typing import List


# Binary Search
def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
    arr2.sort()
    res = 0

    for x in arr1:
        i = bisect_left(arr2, x - d)
        if i == len(arr2) or arr2[i] > x + d:
            res += 1

    return res


arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
print(findTheDistanceValue(arr1, arr2, d))  # 2

```

## 925. Long Pressed Name

-   [LeetCode](https://leetcode.com/problems/long-pressed-name/) | [LeetCode CH](https://leetcode.cn/problems/long-pressed-name/) (Easy)

-   Tags: two pointers, string
## 809. Expressive Words

-   [LeetCode](https://leetcode.com/problems/expressive-words/) | [LeetCode CH](https://leetcode.cn/problems/expressive-words/) (Medium)

-   Tags: array, two pointers, string
## 2337. Move Pieces to Obtain a String

-   [LeetCode](https://leetcode.com/problems/move-pieces-to-obtain-a-string/) | [LeetCode CH](https://leetcode.cn/problems/move-pieces-to-obtain-a-string/) (Medium)

-   Tags: two pointers, string
## 777. Swap Adjacent in LR String

-   [LeetCode](https://leetcode.com/problems/swap-adjacent-in-lr-string/) | [LeetCode CH](https://leetcode.cn/problems/swap-adjacent-in-lr-string/) (Medium)

-   Tags: two pointers, string
## 844. Backspace String Compare

-   [LeetCode](https://leetcode.com/problems/backspace-string-compare/) | [LeetCode CH](https://leetcode.cn/problems/backspace-string-compare/) (Easy)

-   Tags: two pointers, string, stack, simulation

```python title="844. Backspace String Compare - Python Solution"
def backspaceCompare(s: str, t: str) -> bool:

    def build(text):
        stack = []

        for char in text:
            if char != "#":
                stack.append(char)
            elif stack:
                stack.pop()

        return "".join(stack)

    return build(s) == build(t)


print(backspaceCompare("ab#c", "ad#c"))  # True

```

## 986. Interval List Intersections

-   [LeetCode](https://leetcode.com/problems/interval-list-intersections/) | [LeetCode CH](https://leetcode.cn/problems/interval-list-intersections/) (Medium)

-   Tags: array, two pointers, line sweep
## 1537. Get the Maximum Score

-   [LeetCode](https://leetcode.com/problems/get-the-maximum-score/) | [LeetCode CH](https://leetcode.cn/problems/get-the-maximum-score/) (Hard)

-   Tags: array, two pointers, dynamic programming, greedy
## 244. Shortest Word Distance II

-   [LeetCode](https://leetcode.com/problems/shortest-word-distance-ii/) | [LeetCode CH](https://leetcode.cn/problems/shortest-word-distance-ii/) (Medium)

-   Tags: array, hash table, two pointers, string, design
## 2838. Maximum Coins Heroes Can Collect

-   [LeetCode](https://leetcode.com/problems/maximum-coins-heroes-can-collect/) | [LeetCode CH](https://leetcode.cn/problems/maximum-coins-heroes-can-collect/) (Medium)

-   Tags: array, two pointers, binary search, sorting, prefix sum
## 1229. Meeting Scheduler

-   [LeetCode](https://leetcode.com/problems/meeting-scheduler/) | [LeetCode CH](https://leetcode.cn/problems/meeting-scheduler/) (Medium)

-   Tags: array, two pointers, sorting
## 1570. Dot Product of Two Sparse Vectors

-   [LeetCode](https://leetcode.com/problems/dot-product-of-two-sparse-vectors/) | [LeetCode CH](https://leetcode.cn/problems/dot-product-of-two-sparse-vectors/) (Medium)

-   Tags: array, hash table, two pointers, design
## 1868. Product of Two Run-Length Encoded Arrays

-   [LeetCode](https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/) | [LeetCode CH](https://leetcode.cn/problems/product-of-two-run-length-encoded-arrays/) (Medium)

-   Tags: array, two pointers
