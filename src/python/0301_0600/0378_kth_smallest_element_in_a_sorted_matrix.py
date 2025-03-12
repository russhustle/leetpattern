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
