"""
-   Return `False` if the total number of passengers at any point is greater than `capacity`. Otherwise, return `True`.
"""

from itertools import accumulate
from typing import List


# Difference Array
def carPooling1(trips: List[List[int]], capacity: int) -> bool:
    max_location = 0
    for trip in trips:
        max_location = max(max_location, trip[2])

    diff = [0] * (max_location + 1)
    n = len(diff)

    for num, start, end in trips:
        diff[start] += num
        if end < n:
            diff[end] -= num

    cur = 0
    for i in range(n):
        cur += diff[i]
        if cur > capacity:
            return False

    return True


# Difference Array
def carPooling2(trips: List[List[int]], capacity: int) -> bool:
    diff = [0] * 1001

    for num, start, end in trips:
        diff[start] += num
        diff[end] -= num

    return all(s <= capacity for s in accumulate(diff))


trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4
print(carPooling1(trips, capacity))  # False
print(carPooling2(trips, capacity))  # False
