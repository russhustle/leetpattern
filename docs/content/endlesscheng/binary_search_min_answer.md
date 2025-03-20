---
comments: True
---

# Binary Search Min Answer

## Table of Contents

- [ ] [1283. Find the Smallest Divisor Given a Threshold](https://leetcode.cn/problems/find-the-smallest-divisor-given-a-threshold/) (Medium)
- [ ] [2187. Minimum Time to Complete Trips](https://leetcode.cn/problems/minimum-time-to-complete-trips/) (Medium)
- [x] [1870. Minimum Speed to Arrive on Time](https://leetcode.cn/problems/minimum-speed-to-arrive-on-time/) (Medium)
- [x] [1011. Capacity To Ship Packages Within D Days](https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/) (Medium)
- [x] [875. Koko Eating Bananas](https://leetcode.cn/problems/koko-eating-bananas/) (Medium)
- [ ] [3296. Minimum Number of Seconds to Make Mountain Height Zero](https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero/) (Medium)
- [ ] [475. Heaters](https://leetcode.cn/problems/heaters/) (Medium)
- [ ] [2594. Minimum Time to Repair Cars](https://leetcode.cn/problems/minimum-time-to-repair-cars/) (Medium)
- [ ] [1482. Minimum Number of Days to Make m Bouquets](https://leetcode.cn/problems/minimum-number-of-days-to-make-m-bouquets/) (Medium)
- [ ] [3048. Earliest Second to Mark Indices I](https://leetcode.cn/problems/earliest-second-to-mark-indices-i/) (Medium)
- [ ] [2604. Minimum Time to Eat All Grains](https://leetcode.cn/problems/minimum-time-to-eat-all-grains/) (Hard) 👑
- [ ] [2702. Minimum Operations to Make Numbers Non-positive](https://leetcode.cn/problems/minimum-operations-to-make-numbers-non-positive/) (Hard) 👑
- [ ] [3453. Separate Squares I](https://leetcode.cn/problems/separate-squares-i/) (Medium)

## 1283. Find the Smallest Divisor Given a Threshold

-   [LeetCode](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) | [LeetCode CH](https://leetcode.cn/problems/find-the-smallest-divisor-given-a-threshold/) (Medium)

-   Tags: array, binary search

## 2187. Minimum Time to Complete Trips

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-complete-trips/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-complete-trips/) (Medium)

-   Tags: array, binary search

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

## 475. Heaters

-   [LeetCode](https://leetcode.com/problems/heaters/) | [LeetCode CH](https://leetcode.cn/problems/heaters/) (Medium)

-   Tags: array, two pointers, binary search, sorting

## 2594. Minimum Time to Repair Cars

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-repair-cars/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-repair-cars/) (Medium)

-   Tags: array, binary search

## 1482. Minimum Number of Days to Make m Bouquets

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-days-to-make-m-bouquets/) (Medium)

-   Tags: array, binary search

## 3048. Earliest Second to Mark Indices I

-   [LeetCode](https://leetcode.com/problems/earliest-second-to-mark-indices-i/) | [LeetCode CH](https://leetcode.cn/problems/earliest-second-to-mark-indices-i/) (Medium)

-   Tags: array, binary search

## 2604. Minimum Time to Eat All Grains

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-eat-all-grains/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-eat-all-grains/) (Hard)

-   Tags: array, two pointers, binary search, sorting

## 2702. Minimum Operations to Make Numbers Non-positive

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-make-numbers-non-positive/) (Hard)

-   Tags: array, binary search

## 3453. Separate Squares I

-   [LeetCode](https://leetcode.com/problems/separate-squares-i/) | [LeetCode CH](https://leetcode.cn/problems/separate-squares-i/) (Medium)

-   Tags: array, binary search
