---
comments: True
---

# Binary Search Min Answer

## Table of Contents

- [x] [1283. Find the Smallest Divisor Given a Threshold](https://leetcode.cn/problems/find-the-smallest-divisor-given-a-threshold/) (Medium)
- [x] [2187. Minimum Time to Complete Trips](https://leetcode.cn/problems/minimum-time-to-complete-trips/) (Medium)
- [x] [1870. Minimum Speed to Arrive on Time](https://leetcode.cn/problems/minimum-speed-to-arrive-on-time/) (Medium)
- [x] [1011. Capacity To Ship Packages Within D Days](https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/) (Medium)
- [x] [875. Koko Eating Bananas](https://leetcode.cn/problems/koko-eating-bananas/) (Medium)
- [x] [3296. Minimum Number of Seconds to Make Mountain Height Zero](https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero/) (Medium)
- [x] [475. Heaters](https://leetcode.cn/problems/heaters/) (Medium)
- [x] [2594. Minimum Time to Repair Cars](https://leetcode.cn/problems/minimum-time-to-repair-cars/) (Medium)
- [x] [1482. Minimum Number of Days to Make m Bouquets](https://leetcode.cn/problems/minimum-number-of-days-to-make-m-bouquets/) (Medium)
- [x] [3048. Earliest Second to Mark Indices I](https://leetcode.cn/problems/earliest-second-to-mark-indices-i/) (Medium)
- [ ] [2604. Minimum Time to Eat All Grains](https://leetcode.cn/problems/minimum-time-to-eat-all-grains/) (Hard) 👑
- [ ] [2702. Minimum Operations to Make Numbers Non-positive](https://leetcode.cn/problems/minimum-operations-to-make-numbers-non-positive/) (Hard) 👑
- [ ] [3453. Separate Squares I](https://leetcode.cn/problems/separate-squares-i/) (Medium)

## 1283. Find the Smallest Divisor Given a Threshold

-   [LeetCode](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) | [LeetCode CH](https://leetcode.cn/problems/find-the-smallest-divisor-given-a-threshold/) (Medium)

-   Tags: array, binary search
- 二分答案的关键是找到单调性，然后分析出判断条件

```python title="1283. Find the Smallest Divisor Given a Threshold - Python Solution"
from typing import List


# Binary Search Min Answer
def smallestDivisor(nums: List[int], threshold: int) -> int:
    left, right = 0, max(nums)

    while left + 1 < right:
        mid = left + (right - left) // 2
        if sum((x - 1) // mid for x in nums) <= threshold - len(nums):
            right = mid
        else:
            left = mid

    return right


if __name__ == "__main__":
    nums = [1, 2, 5, 9]
    threshold = 6
    assert smallestDivisor(nums, threshold) == 5

```

## 2187. Minimum Time to Complete Trips

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-complete-trips/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-complete-trips/) (Medium)

-   Tags: array, binary search
- Left: always insufficient trips
- Right: always sufficient trips

```python title="2187. Minimum Time to Complete Trips - Python Solution"
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

```

## 1870. Minimum Speed to Arrive on Time

-   [LeetCode](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/) | [LeetCode CH](https://leetcode.cn/problems/minimum-speed-to-arrive-on-time/) (Medium)

-   Tags: array, binary search
```python title="1870. Minimum Speed to Arrive on Time - Python Solution"
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

```

## 1011. Capacity To Ship Packages Within D Days

-   [LeetCode](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | [LeetCode CH](https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/) (Medium)

-   Tags: array, binary search
-   A conveyor belt has packages that must be shipped from one port to another within `D` days. The `i-th` package has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt. The ship will be loaded with packages up to its capacity. The ship will not be loaded beyond its capacity. Return the least weight capacity of the ship.

```python title="1011. Capacity To Ship Packages Within D Days - Python Solution"
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

```

## 875. Koko Eating Bananas

-   [LeetCode](https://leetcode.com/problems/koko-eating-bananas/) | [LeetCode CH](https://leetcode.cn/problems/koko-eating-bananas/) (Medium)

-   Tags: array, binary search
-   Koko loves to eat bananas. She wants to eat all the bananas within `H` hours. Each pile has a number of bananas. The `i-th` pile has `piles[i]` bananas. Return the minimum integer `K` such that she can eat all the bananas within `H` hours.

```python title="875. Koko Eating Bananas - Python Solution"
from typing import List


# Binary Search
def minEatingSpeed(piles: List[int], h: int) -> int:
    def canEat(piles, k, h):
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
print(minEatingSpeed(piles, h))  # 4

```

## 3296. Minimum Number of Seconds to Make Mountain Height Zero

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero/) (Medium)

-   Tags: array, math, binary search, greedy, heap priority queue
```python title="3296. Minimum Number of Seconds to Make Mountain Height Zero - Python Solution"
from bisect import bisect_left
from heapq import heapify, heapreplace
from math import isqrt
from typing import List


# Min Heap
def minNumberOfSecondsMinHeap(
    mountainHeight: int, workerTimes: List[int]
) -> int:
    minHeap = [(t, t, t) for t in workerTimes]
    heapify(minHeap)

    for _ in range(mountainHeight):
        nxt, delta, base = minHeap[0]
        heapreplace(
            minHeap,
            (
                nxt + delta + base,
                delta + base,
                base,
            ),
        )
    return nxt


# Binary Search Min Answer
def minNumberOfSecondsBinarySearchMin(
    mountainHeight: int, workerTimes: List[int]
) -> int:
    def check(m: int) -> bool:
        left_h = mountainHeight
        for t in workerTimes:
            left_h -= (isqrt(m // t * 8 + 1) - 1) // 2
            if left_h <= 0:
                return True
        return False

    max_t = max(workerTimes)
    h = (mountainHeight - 1) // len(workerTimes) + 1
    return bisect_left(range(max_t * h * (h + 1) // 2), True, 1, key=check)


if __name__ == "__main__":
    mountainHeight = 4
    workerTimes = [2, 1, 1]
    assert minNumberOfSecondsMinHeap(mountainHeight, workerTimes) == 3
    assert minNumberOfSecondsBinarySearchMin(mountainHeight, workerTimes) == 3

```

## 475. Heaters

-   [LeetCode](https://leetcode.com/problems/heaters/) | [LeetCode CH](https://leetcode.cn/problems/heaters/) (Medium)

-   Tags: array, two pointers, binary search, sorting
```python title="475. Heaters - Python Solution"
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

```

## 2594. Minimum Time to Repair Cars

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-repair-cars/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-repair-cars/) (Medium)

-   Tags: array, binary search
```python title="2594. Minimum Time to Repair Cars - Python Solution"
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

```

## 1482. Minimum Number of Days to Make m Bouquets

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-days-to-make-m-bouquets/) (Medium)

-   Tags: array, binary search
```python title="1482. Minimum Number of Days to Make m Bouquets - Python Solution"
from typing import List


# Binary Search Min Answer
def minDays(bloomDay: List[int], m: int, k: int) -> int:
    n = len(bloomDay)
    if m * k > n:
        return -1

    def canMake(day: int) -> bool:
        bouquets = 0
        flowers = 0
        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m

    left, right = min(bloomDay), max(bloomDay)
    res = -1

    while left <= right:
        mid = left + (right - left) // 2
        if canMake(mid):
            res = mid
            right = mid - 1
        else:
            left = mid + 1

    return res


if __name__ == "__main__":
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1
    assert minDays(bloomDay, m, k) == 3

```

## 3048. Earliest Second to Mark Indices I

-   [LeetCode](https://leetcode.com/problems/earliest-second-to-mark-indices-i/) | [LeetCode CH](https://leetcode.cn/problems/earliest-second-to-mark-indices-i/) (Medium)

-   Tags: array, binary search
```python title="3048. Earliest Second to Mark Indices I - Python Solution"
from bisect import bisect_left
from typing import List


# Binary Search Min Answer
def earliestSecondToMarkIndices(
    nums: List[int], changeIndices: List[int]
) -> int:
    n, m = len(nums), len(changeIndices)
    if n > m:
        return -1

    def check(mx: int) -> bool:
        last_t = [-1] * n
        for t, idx in enumerate(changeIndices[:mx]):
            last_t[idx - 1] = t
        if -1 in last_t:
            return False

        cnt = 0
        for i, idx in enumerate(changeIndices[:mx]):
            idx -= 1
            if i == last_t[idx]:
                if nums[idx] > cnt:
                    return False
                cnt -= nums[idx]
            else:
                cnt += 1
        return True

    left = n + sum(nums)
    res = left + bisect_left(range(left, m + 1), True, key=check)
    return -1 if res > m else res


if __name__ == "__main__":
    nums = [2, 2, 0]
    changeIndices = [2, 2, 2, 2, 3, 2, 2, 1]
    assert earliestSecondToMarkIndices(nums, changeIndices) == 8

```

## 2604. Minimum Time to Eat All Grains

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-eat-all-grains/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-eat-all-grains/) (Hard)

-   Tags: array, two pointers, binary search, sorting
## 2702. Minimum Operations to Make Numbers Non-positive

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-make-numbers-non-positive/) (Hard)

-   Tags: array, binary search
## 3453. Separate Squares I

-   [LeetCode](https://leetcode.com/problems/separate-squares-i/) | [LeetCode CH](https://leetcode.cn/problems/separate-squares-i/) (Medium)

-   Tags: array, binary search
