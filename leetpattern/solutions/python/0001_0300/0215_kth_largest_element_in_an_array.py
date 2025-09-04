import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    min_heap = []

    for i, num in enumerate(nums):
        heapq.heappush(min_heap, num)
        if i >= k:
            heapq.heappop(min_heap)

    return min_heap[0]


if __name__ == "__main__":
    assert findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
