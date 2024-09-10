import heapq
from typing import List


# Heap
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))  # 4
print(obj.add(5))  # 5
print(obj.add(10))  # 5
