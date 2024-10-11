import math
from typing import List


# Binary Search
def minSpeedOnTime(dist: List[int], hour: float) -> int:
    if hour < len(dist) - 1:
        return -1

    def time_needed(speed):
        total_time = 0
        for i in range(len(dist) - 1):
            total_time += math.ceil(dist[i] / speed)
        total_time += dist[-1] / speed
        return total_time

    left, right = 1, 10**7
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if time_needed(mid) <= hour:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


dist = [1, 3, 2]
hour = 6
print(minSpeedOnTime(dist, hour))  # 1
