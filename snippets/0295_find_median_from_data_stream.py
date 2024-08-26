from heapq import heappop, heappush


# Heap - Two Heaps
class MedianFinder:
    def __init__(self):
        self.max = []
        self.min = []

    def addNum(self, num: int) -> None:
        heappush(self.max, -num)
        heappush(self.min, -heappop(self.max))

        if len(self.min) > len(self.max):
            heappush(self.max, -heappop(self.min))

    def findMedian(self) -> float:
        if len(self.max) == len(self.min):
            return (-self.max[0] + self.min[0]) / 2.0
        else:
            return -self.max[0]


# TC: O(log n)
# SC: O(n)

median_finder = MedianFinder()
median_finder.addNum(1)
median_finder.addNum(2)
assert median_finder.findMedian() == 1.5
median_finder.addNum(3)
assert median_finder.findMedian() == 2
median_finder.addNum(4)
assert median_finder.findMedian() == 2.5
median_finder.addNum(5)
assert median_finder.findMedian() == 3
print("All Passed.")
