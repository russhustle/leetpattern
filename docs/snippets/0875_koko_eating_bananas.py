from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    def canEat(piles: List[int], k: int, h: int) -> bool:
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k
        return hours <= h

    left, right = 1, max(piles)

    while left <= right:
        mid = left + (right - left) // 2

        if canEat(piles, mid, h):
            right = mid - 1
        else:
            left = mid + 1

    return left


piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))