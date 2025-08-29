"""
- Left: always insufficient trips
- Right: always sufficient trips
"""

from typing import List


# Binary Search Min Answer
def minimumTime(time: List[int], totalTrips: int) -> int:
    min_t = min(time)
    left = min_t - 1
    right = min_t * totalTrips

    while left + 1 < right:
        mid = left + (right - left) // 2
        if sum(mid // t for t in time) >= totalTrips:
            right = mid
        else:
            left = mid

    return right


if __name__ == "__main__":
    time = [1, 2, 3]
    totalTrips = 5
    assert minimumTime(time, totalTrips) == 3
