from heapq import heappop, heappush


# Heap
class SmallestInfiniteSet:
    def __init__(self):
        self.cur_min = 1
        self.added = set()
        self.min_heap = []

    def popSmallest(self) -> int:
        if self.min_heap:
            res = heappop(self.min_heap)
            self.added.remove(res)
            return res

        res = self.cur_min
        self.cur_min += 1
        return res

    def addBack(self, num: int) -> None:
        if num < self.cur_min and num not in self.added:
            self.added.add(num)
            heappush(self.min_heap, num)


if __name__ == "__main__":
    sis = SmallestInfiniteSet()
    assert sis.popSmallest() == 1
    sis.addBack(2)
    assert sis.popSmallest() == 2
    assert sis.popSmallest() == 3
    sis.addBack(1)
    assert sis.popSmallest() == 1
    assert sis.popSmallest() == 4
    sis.addBack(3)
    assert sis.popSmallest() == 3
