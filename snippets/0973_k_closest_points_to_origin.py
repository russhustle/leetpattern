import heapq
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []

    for x, y in points:
        dist = -(x**2 + y**2)  # max heap
        if len(heap) < k:
            heapq.heappush(heap, (dist, x, y))
        else:
            heapq.heappushpop(heap, (dist, x, y))  # push and pop the smallest

    return [[x, y] for (_, x, y) in heap]


# Time complexity: O(n * log(k))
#   - O(log(k)) for heapify
#   - O(n) for iterating through the input list
# Space complexity: O(k)

points = [[1, 3], [-2, 2]]
k = 1
print(kClosest(points, k))  # [[-2, 2]]
