from typing import List


class minEatingSpeed:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(piles, k, h):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours <= h

        left, right = 1, max(piles) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if canEat(piles, mid, h):
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    sol = minEatingSpeed()
    assert sol.minEatingSpeed(piles, h) == 4
