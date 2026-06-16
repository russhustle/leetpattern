import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """Min Heap Setup: O(n log k) time, O(k) space.
        Keeping only k values means the smallest heap item is the kth largest.
        """
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """Min Heap Stream Update: O(log k) time, O(k) space.
        Push each value and remove the smallest once more than k candidates exist.
        """
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


def test_kth_largest():
    obj = KthLargest(3, [4, 5, 8, 2])
    assert obj.add(3) == 4
    assert obj.add(5) == 5
    assert obj.add(10) == 5
    assert obj.add(9) == 8
    assert obj.add(4) == 8

    obj = KthLargest(1, [])
    assert obj.add(-3) == -3
    assert obj.add(-2) == -2
    assert obj.add(-4) == -2

    obj = KthLargest(2, [0])
    assert obj.add(-1) == -1
    assert obj.add(1) == 0
    assert obj.add(1) == 1
