from heapq import heapify, heappop, heappush
from typing import List


# Heap
def connectSticks(sticks: List[int]) -> int:
    n = len(sticks)
    heapify(sticks)
    res = 0

    while n > 1:
        x = heappop(sticks)
        y = heappop(sticks)
        res += x + y
        heappush(sticks, x + y)
        n -= 1

    return res


if __name__ == "__main__":
    assert connectSticks([2, 4, 3]) == 14
    assert connectSticks([1, 8, 3, 5]) == 30
    assert connectSticks([5]) == 0
    assert connectSticks([1, 2, 3, 4, 5]) == 33
    assert connectSticks([1, 1, 1]) == 5
