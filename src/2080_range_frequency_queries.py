from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


# Binary Search
class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.freq = defaultdict(list)
        for idx, val in enumerate(arr):
            self.freq[val].append(idx)

    def query(self, left: int, right: int, value: int) -> int:
        idxs = self.freq[value]
        return bisect_right(idxs, right) - bisect_left(idxs, left)


arr = [1, 3, 1, 2, 4, 1, 3, 2, 1]
rfq = RangeFreqQuery(arr)
print(rfq.query(0, 4, 1))  # 2
print(rfq.query(2, 8, 1))  # 3
print(rfq.query(0, 8, 3))  # 2
print(rfq.query(4, 7, 2))  # 1
