---
comments: True
---

# Heap Kth Smallest Largest

## Table of Contents

- [x] [264. Ugly Number II](https://leetcode.cn/problems/ugly-number-ii/) (Medium)
- [x] [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/) (Medium)
- [x] [373. Find K Pairs with Smallest Sums](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/) (Medium)
- [ ] [1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows](https://leetcode.cn/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/) (Hard)
- [x] [786. K-th Smallest Prime Fraction](https://leetcode.cn/problems/k-th-smallest-prime-fraction/) (Medium)
- [ ] [2386. Find the K-Sum of an Array](https://leetcode.cn/problems/find-the-k-sum-of-an-array/) (Hard)

## 264. Ugly Number II

-   [LeetCode](https://leetcode.com/problems/ugly-number-ii/) | [LeetCode CH](https://leetcode.cn/problems/ugly-number-ii/) (Medium)

-   Tags: hash table, math, dynamic programming, heap priority queue

```python title="264. Ugly Number II - Python Solution"
import heapq


def nthUglyNumber(n: int) -> int:
    heap = [1]
    seen = set(heap)

    factors = [2, 3, 5]
    current = 1

    # Pop the smallest ugly number n times
    for _ in range(n):
        current = heapq.heappop(heap)  # Pop the smallest ugly number

        for factor in factors:
            new = current * factor
            if new not in seen:
                seen.add(new)
                heapq.heappush(heap, new)

    return current


print(nthUglyNumber(10))  # 12

```

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

## 2386. Find the K-Sum of an Array

-   [LeetCode](https://leetcode.com/problems/find-the-k-sum-of-an-array/) | [LeetCode CH](https://leetcode.cn/problems/find-the-k-sum-of-an-array/) (Hard)

-   Tags: array, sorting, heap priority queue
