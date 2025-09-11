from heapq import heapify, heappop, heappush
from math import isqrt
from typing import List


# Heap
def pickGifts(gifts: List[int], k: int) -> int:
    maxHeap = [-g for g in gifts]
    heapify(maxHeap)

    for _ in range(k):
        cur = heappop(maxHeap)

        if cur == -1:
            heappush(maxHeap, cur)
            break

        heappush(maxHeap, -isqrt(-cur))

    return sum(-i for i in maxHeap)


if __name__ == "__main__":
    assert pickGifts([25, 64, 9, 4, 100], 4) == 29
    assert pickGifts([1, 1, 1, 1], 4) == 0
