import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)  # min heap

        while len(self.heap) > k:  # keep the heap size to k
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if (
            len(self.heap) < self.k
        ):  # if heap size is less than k, push the value
            heapq.heappush(self.heap, val)
        # if the value is greater than the smallest element in the heap
        # push the value and pop the smallest element
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)

        return self.heap[0]


kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))  # 4
