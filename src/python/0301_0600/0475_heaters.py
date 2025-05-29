from bisect import bisect_left, bisect_right
from math import inf
from typing import List


# Left Right Pointers
def findRadiusLR(houses: List[int], heaters: List[int]) -> int:
    heaters = heaters + [-inf, inf]
    houses.sort()
    heaters.sort()
    i, j, res = 0, 0, 0

    while i < len(houses):
        cur = inf
        while heaters[j] <= houses[i]:
            cur = houses[i] - heaters[j]
            j += 1
        cur = min(cur, heaters[j] - houses[i])
        res = max(cur, res)
        i += 1
        j -= 1

    return res


# Binary Search Min Answer
def findRadiusBS(houses: List[int], heaters: List[int]) -> int:
    houses.sort()
    heaters.sort()

    def closest(house):
        left = bisect_right(heaters, house) - 1
        d1 = abs(heaters[left] - house) if left >= 0 else inf

        right = bisect_left(heaters, house)
        d2 = abs(heaters[right] - house) if right < len(heaters) else inf

        return min(d1, d2)

    return max(closest(house) for house in houses)


if __name__ == "__main__":
    houses = [1, 2, 3]
    heaters = [2]
    assert findRadiusLR(houses, heaters) == 1
    assert findRadiusBS(houses, heaters) == 1
