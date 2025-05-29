from math import isqrt
from typing import List


# Binary Search Min Answer
def repairCars(ranks: List[int], cars: int) -> int:
    left, right = 0, max(ranks) * cars * cars

    while left + 1 < right:
        mid = left + (right - left) // 2
        if sum(isqrt(mid // rank) for rank in ranks) >= cars:
            right = mid
        else:
            left = mid
    return right


if __name__ == "__main__":
    ranks = [4, 2, 3, 1]
    cars = 10
    assert repairCars(ranks, cars) == 16
