"""
-   A conveyor belt has packages that must be shipped from one port to another within `D` days. The `i-th` package has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt. The ship will be loaded with packages up to its capacity. The ship will not be loaded beyond its capacity. Return the least weight capacity of the ship.
"""

from typing import List


# Binary Search
def shipWithinDays(weights: List[int], days: int) -> int:

    def canShip(weights, D, capacity):
        days = 1
        current_weight = 0

        for weight in weights:
            if current_weight + weight > capacity:
                days += 1
                current_weight = 0
            current_weight += weight

        return days <= D

    left, right = max(weights), sum(weights)

    while left <= right:
        mid = left + (right - left) // 2

        if canShip(weights, days, mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(shipWithinDays(weights, days))  # 15
