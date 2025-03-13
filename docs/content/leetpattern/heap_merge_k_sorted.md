---
comments: True
---

# Heap Merge K Sorted

- [x] [23. Merge k Sorted Lists](https://leetcode.cn/problems/merge-k-sorted-lists/) (Hard)
- [x] [373. Find K Pairs with Smallest Sums](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/) (Medium)
- [x] [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/) (Medium)

## 23. Merge k Sorted Lists

-   [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/) | [LeetCode CH](https://leetcode.cn/problems/merge-k-sorted-lists/) (Hard)

-   Tags: linked list, divide and conquer, heap priority queue, merge sort
-   Prerequisite: 21. Merge Two Sorted Lists

<iframe width="560" height="315" src="https://www.youtube.com/embed/q5a5OiGbT6Q?si=SlQg9SKZh1YL62vH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```python title="23. Merge k Sorted Lists - Python Solution"
import copy
import heapq
from typing import List, Optional

from template import ListNode


# Divide and Conquer
def mergeKListsDC(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists or len(lists) == 0:
        return None

    def mergeTwo(l1, l2):
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        cur.next = l1 if l1 else l2

        return dummy.next

    while len(lists) > 1:
        merged = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(mergeTwo(l1, l2))

        lists = merged

    return lists[0]


# Heap - Merge k Sorted
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy

    minHeap = []  # (val, idx, node)

    for idx, head in enumerate(lists):
        if head:
            heapq.heappush(minHeap, (head.val, idx, head))

    while minHeap:
        _, idx, node = heapq.heappop(minHeap)
        cur.next = node
        cur = cur.next

        node = node.next
        if node:
            heapq.heappush(minHeap, (node.val, idx, node))

    return dummy.next


n1 = ListNode.create([1, 4, 5])
n2 = ListNode.create([1, 3, 4])
n3 = ListNode.create([2, 6])
lists = [n1, n2, n3]
lists1 = copy.deepcopy(lists)
lists2 = copy.deepcopy(lists)
print(mergeKListsDC(lists1))
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
print(mergeKLists(lists2))
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

```

## 373. Find K Pairs with Smallest Sums

-   [LeetCode](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | [LeetCode CH](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/) (Medium)

-   Tags: array, heap priority queue

```python title="373. Find K Pairs with Smallest Sums - Python Solution"
import heapq
from typing import List


# Heap - Merge K Sorted
def kSmallestPairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
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
