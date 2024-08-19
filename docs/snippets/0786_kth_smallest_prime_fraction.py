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
