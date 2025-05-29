from bisect import bisect_left
from heapq import heapify, heapreplace
from math import isqrt
from typing import List


# Min Heap
def minNumberOfSecondsMinHeap(
    mountainHeight: int, workerTimes: List[int]
) -> int:
    minHeap = [(t, t, t) for t in workerTimes]
    heapify(minHeap)

    for _ in range(mountainHeight):
        nxt, delta, base = minHeap[0]
        heapreplace(
            minHeap,
            (
                nxt + delta + base,
                delta + base,
                base,
            ),
        )
    return nxt


# Binary Search Min Answer
def minNumberOfSecondsBinarySearchMin(
    mountainHeight: int, workerTimes: List[int]
) -> int:
    def check(m: int) -> bool:
        left_h = mountainHeight
        for t in workerTimes:
            left_h -= (isqrt(m // t * 8 + 1) - 1) // 2
            if left_h <= 0:
                return True
        return False

    max_t = max(workerTimes)
    h = (mountainHeight - 1) // len(workerTimes) + 1
    return bisect_left(range(max_t * h * (h + 1) // 2), True, 1, key=check)


if __name__ == "__main__":
    mountainHeight = 4
    workerTimes = [2, 1, 1]
    assert minNumberOfSecondsMinHeap(mountainHeight, workerTimes) == 3
    assert minNumberOfSecondsBinarySearchMin(mountainHeight, workerTimes) == 3
