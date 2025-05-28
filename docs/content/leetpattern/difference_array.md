---
comments: True
---

# Difference Array

## Table of Contents

- [x] [1094. Car Pooling](https://leetcode.cn/problems/car-pooling/) (Medium)
- [x] [370. Range Addition](https://leetcode.cn/problems/range-addition/) (Medium) 👑
- [x] [1109. Corporate Flight Bookings](https://leetcode.cn/problems/corporate-flight-bookings/) (Medium)
- [x] [2848. Points That Intersect With Cars](https://leetcode.cn/problems/points-that-intersect-with-cars/) (Easy)

## 1094. Car Pooling

-   [LeetCode](https://leetcode.com/problems/car-pooling/) | [LeetCode CH](https://leetcode.cn/problems/car-pooling/) (Medium)

-   Tags: array, sorting, heap priority queue, simulation, prefix sum
-   Return `False` if the total number of passengers at any point is greater than `capacity`. Otherwise, return `True`.


```python title="1094. Car Pooling - Python Solution"
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

```

## 370. Range Addition

-   [LeetCode](https://leetcode.com/problems/range-addition/) | [LeetCode CH](https://leetcode.cn/problems/range-addition/) (Medium)

-   Tags: array, prefix sum
-   Return the final array after applying all the Adition operations.


```python title="370. Range Addition - Python Solution"
from typing import List


# Difference Array
def getModifiedArray(length: int, updates: List[List[int]]) -> List[int]:
    result = [0 for _ in range(length)]

    for start, end, inc in updates:
        result[start] += inc

        if end + 1 < length:
            result[end + 1] -= inc

    for i in range(1, length):
        result[i] += result[i - 1]

    return result


length = 5
updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
print(getModifiedArray(length, updates))  # [-2, 0, 3, 5, 3]

```

## 1109. Corporate Flight Bookings

-   [LeetCode](https://leetcode.com/problems/corporate-flight-bookings/) | [LeetCode CH](https://leetcode.cn/problems/corporate-flight-bookings/) (Medium)

-   Tags: array, prefix sum
-   Return the number of seats booked on each flight.


```python title="1109. Corporate Flight Bookings - Python Solution"
from typing import List


# Difference Array
def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    """Return the number of seats booked for each flight."""
    res = [0 for _ in range(n)]

    for i, j, k in bookings:
        res[i - 1] += k
        if j < n:
            res[j] -= k

    for i in range(1, n):
        res[i] += res[i - 1]

    return res


bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
n = 5
print(corpFlightBookings(bookings, n))  # [10, 55, 45, 25, 25]

```

## 2848. Points That Intersect With Cars

-   [LeetCode](https://leetcode.com/problems/points-that-intersect-with-cars/) | [LeetCode CH](https://leetcode.cn/problems/points-that-intersect-with-cars/) (Easy)

-   Tags: array, hash table, prefix sum
-   Return the number of points that intersect with cars.


```python title="2848. Points That Intersect With Cars - Python Solution"
from itertools import accumulate
from typing import List


# Differnce Array
def numberOfPoints(nums: List[List[int]]) -> int:
    max_end = max(end for _, end in nums)

    diff = [0] * (max_end + 2)

    for start, end in nums:
        diff[start] += 1
        diff[end + 1] -= 1

    return sum(s > 0 for s in accumulate(diff))


nums = [[3, 6], [1, 5], [4, 7]]
print(numberOfPoints(nums))  # 7

```
