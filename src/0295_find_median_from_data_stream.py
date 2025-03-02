from heapq import heappop, heappush


# Dual Heaps
class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count = 1 - self.count
        heappush(self.maxHeap, -num)
        heappush(self.minHeap, -heappop(self.maxHeap))

        if self.count == 1:
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        if self.count == 0:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        elif self.count == 1:
            return -self.maxHeap[0]


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
assert obj.findMedian() == 1.5
obj.addNum(3)
assert obj.findMedian() == 2
obj.addNum(4)
assert obj.findMedian() == 2.5
obj.addNum(5)
assert obj.findMedian() == 3
print("All Passed.")
