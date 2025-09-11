from collections import defaultdict
from typing import List


# Hash
def interchangeableRectangles(rectangles: List[List[int]]) -> int:
    res = 0
    counts = defaultdict(int)

    for w, h in rectangles:
        ratio = w / h
        res += counts[ratio]
        counts[ratio] += 1

    return res


rectangles = [[4, 8], [3, 6], [10, 20], [15, 30]]
print(interchangeableRectangles(rectangles))  # 6
