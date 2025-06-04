from heapq import heapify, heappop, heappush
from math import ceil
from typing import List


# Heap
def maxKelements(nums: List[int], k: int) -> int:
    res = 0
    maxHeap = [-n for n in nums]
    heapify(maxHeap)

    while k > 0:
        cur = -heappop(maxHeap)
        res += cur
        heappush(maxHeap, -ceil(cur / 3))
        k -= 1

    return res


if __name__ == "__main__":
    assert maxKelements([10, 10, 10, 10, 10], 5) == 50
    assert maxKelements([1, 10, 3, 3, 3], 3) == 17
    assert maxKelements([1, 2, 3, 4, 5], 5) == 16
