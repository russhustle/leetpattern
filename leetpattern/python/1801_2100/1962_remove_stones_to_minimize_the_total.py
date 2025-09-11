from heapq import heapify, heapreplace
from typing import List


# Heap
def minStoneSum(piles: List[int], k: int) -> int:
    maxHeap = [-p for p in piles]
    heapify(maxHeap)

    for _ in range(k):
        heapreplace(maxHeap, maxHeap[0] // 2)

    return -sum(maxHeap)


if __name__ == "__main__":
    assert minStoneSum([5, 4, 9], 2) == 12
    assert minStoneSum([4, 3, 6, 7], 3) == 12
