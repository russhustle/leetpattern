---
comments: True
---

# Binary Search Kth Min Max

- [ ] [668. Kth Smallest Number in Multiplication Table](https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/) (Hard)
- [x] [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/) (Medium)
- [ ] [719. Find K-th Smallest Pair Distance](https://leetcode.cn/problems/find-k-th-smallest-pair-distance/) (Hard)
- [ ] [878. Nth Magical Number](https://leetcode.cn/problems/nth-magical-number/) (Hard)
- [ ] [1201. Ugly Number III](https://leetcode.cn/problems/ugly-number-iii/) (Medium)
- [ ] [793. Preimage Size of Factorial Zeroes Function](https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/) (Hard)
- [x] [373. Find K Pairs with Smallest Sums](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/) (Medium)
- [ ] [1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows](https://leetcode.cn/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/) (Hard)
- [x] [786. K-th Smallest Prime Fraction](https://leetcode.cn/problems/k-th-smallest-prime-fraction/) (Medium)
- [ ] [3116. Kth Smallest Amount With Single Denomination Combination](https://leetcode.cn/problems/kth-smallest-amount-with-single-denomination-combination/) (Hard)
- [ ] [3134. Find the Median of the Uniqueness Array](https://leetcode.cn/problems/find-the-median-of-the-uniqueness-array/) (Hard)
- [ ] [2040. Kth Smallest Product of Two Sorted Arrays](https://leetcode.cn/problems/kth-smallest-product-of-two-sorted-arrays/) (Hard)
- [ ] [2386. Find the K-Sum of an Array](https://leetcode.cn/problems/find-the-k-sum-of-an-array/) (Hard)
- [ ] [1508. Range Sum of Sorted Subarray Sums](https://leetcode.cn/problems/range-sum-of-sorted-subarray-sums/) (Medium)
- [ ] [1918. Kth Smallest Subarray Sum](https://leetcode.cn/problems/kth-smallest-subarray-sum/) (Medium) 👑

## 668. Kth Smallest Number in Multiplication Table

-   [LeetCode](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/) | [LeetCode CH](https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/) (Hard)

-   Tags: math, binary search

## 378. Kth Smallest Element in a Sorted Matrix

-   [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | [LeetCode CH](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/) (Medium)

-   Tags: array, binary search, sorting, heap priority queue, matrix
-   Given an `n x n` matrix where each of the rows and columns are sorted in ascending order, return the `k-th` smallest element in the matrix.

```python title="378. Kth Smallest Element in a Sorted Matrix - Python Solution"
from heapq import heapify, heappop, heappush
from typing import List


# Heap - Merge K Sorted
def kthSmallestHeap(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    heap = [(matrix[i][0], i, 0) for i in range(n)]
    heapify(heap)

    for _ in range(k - 1):
        _, row, col = heappop(heap)

        if col + 1 < n:
            heappush(heap, (matrix[row][col + 1], row, col + 1))

    return heappop(heap)[0]


# Binary Search
def kthSmallestBinarySearch(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)

    def check(mid):
        i, j = n - 1, 0
        num = 0

        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                num += i + 1
                j += 1
            else:
                i -= 1

        return num >= k

    left, right = matrix[0][0], matrix[-1][-1]

    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1

    return left


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8

print(kthSmallestHeap(matrix, k))  # 13
print(kthSmallestBinarySearch(matrix, k))  # 13

```

## 719. Find K-th Smallest Pair Distance

-   [LeetCode](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) | [LeetCode CH](https://leetcode.cn/problems/find-k-th-smallest-pair-distance/) (Hard)

-   Tags: array, two pointers, binary search, sorting

## 878. Nth Magical Number

-   [LeetCode](https://leetcode.com/problems/nth-magical-number/) | [LeetCode CH](https://leetcode.cn/problems/nth-magical-number/) (Hard)

-   Tags: math, binary search

## 1201. Ugly Number III

-   [LeetCode](https://leetcode.com/problems/ugly-number-iii/) | [LeetCode CH](https://leetcode.cn/problems/ugly-number-iii/) (Medium)

-   Tags: math, binary search, combinatorics, number theory

## 793. Preimage Size of Factorial Zeroes Function

-   [LeetCode](https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/) | [LeetCode CH](https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/) (Hard)

-   Tags: math, binary search

## 373. Find K Pairs with Smallest Sums

-   [LeetCode](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | [LeetCode CH](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/) (Medium)

-   Tags: array, heap priority queue

```python title="373. Find K Pairs with Smallest Sums - Python Solution"
import heapq
from typing import List


# Heap - Merge K Sorted
def kSmallestPairs(
    nums1: List[int], nums2: List[int], k: int
) -> List[List[int]]:
    if not nums1 or not nums2 or k <= 0:
        return []

    result = []
    min_heap = []

    for j in range(min(k, len(nums2))):
        heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))

    while k > 0 and min_heap:
        _, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])
        k -= 1

        if i + 1 < len(nums1):
            heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))

    return result


nums1 = [1, 2, 4, 5, 6]
nums2 = [3, 5, 7, 9]
k = 3
print(kSmallestPairs(nums1, nums2, k))
# [[1, 3], [2, 3], [1, 5]]

```

## 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows

-   [LeetCode](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/) | [LeetCode CH](https://leetcode.cn/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/) (Hard)

-   Tags: array, binary search, heap priority queue, matrix

## 786. K-th Smallest Prime Fraction

-   [LeetCode](https://leetcode.com/problems/k-th-smallest-prime-fraction/) | [LeetCode CH](https://leetcode.cn/problems/k-th-smallest-prime-fraction/) (Medium)

-   Tags: array, two pointers, binary search, sorting, heap priority queue

```python title="786. K-th Smallest Prime Fraction - Python Solution"
import heapq
from typing import List


def kthSmallestPrimeFraction(arr: List[int], k: int) -> List[int]:
    max_heap = []

    for j in range(1, len(arr)):
        for i in range(j):
            heapq.heappush(max_heap, (-arr[i] / arr[j], arr[i], arr[j]))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

    return [max_heap[0][1], max_heap[0][2]]


arr = [1, 2, 3, 5]
k = 3
print(kthSmallestPrimeFraction(arr, k))  # [2, 5]

```

## 3116. Kth Smallest Amount With Single Denomination Combination

-   [LeetCode](https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/) | [LeetCode CH](https://leetcode.cn/problems/kth-smallest-amount-with-single-denomination-combination/) (Hard)

-   Tags: array, math, binary search, bit manipulation, combinatorics, number theory

## 3134. Find the Median of the Uniqueness Array

-   [LeetCode](https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/) | [LeetCode CH](https://leetcode.cn/problems/find-the-median-of-the-uniqueness-array/) (Hard)

-   Tags: array, hash table, binary search, sliding window

## 2040. Kth Smallest Product of Two Sorted Arrays

-   [LeetCode](https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/) | [LeetCode CH](https://leetcode.cn/problems/kth-smallest-product-of-two-sorted-arrays/) (Hard)

-   Tags: array, binary search

## 2386. Find the K-Sum of an Array

-   [LeetCode](https://leetcode.com/problems/find-the-k-sum-of-an-array/) | [LeetCode CH](https://leetcode.cn/problems/find-the-k-sum-of-an-array/) (Hard)

-   Tags: array, sorting, heap priority queue

## 1508. Range Sum of Sorted Subarray Sums

-   [LeetCode](https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/) | [LeetCode CH](https://leetcode.cn/problems/range-sum-of-sorted-subarray-sums/) (Medium)

-   Tags: array, two pointers, binary search, sorting

## 1918. Kth Smallest Subarray Sum

-   [LeetCode](https://leetcode.com/problems/kth-smallest-subarray-sum/) | [LeetCode CH](https://leetcode.cn/problems/kth-smallest-subarray-sum/) (Medium)

-   Tags: array, binary search, sliding window
