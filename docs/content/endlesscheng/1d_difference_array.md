---
comments: True
---

# 1D Difference Array

## Table of Contents

- [x] [2848. Points That Intersect With Cars](https://leetcode.cn/problems/points-that-intersect-with-cars/) (Easy)
- [ ] [1893. Check if All the Integers in a Range Are Covered](https://leetcode.cn/problems/check-if-all-the-integers-in-a-range-are-covered/) (Easy)
- [ ] [1854. Maximum Population Year](https://leetcode.cn/problems/maximum-population-year/) (Easy)
- [ ] [2960. Count Tested Devices After Test Operations](https://leetcode.cn/problems/count-tested-devices-after-test-operations/) (Easy)
- [x] [1094. Car Pooling](https://leetcode.cn/problems/car-pooling/) (Medium)
- [x] [1109. Corporate Flight Bookings](https://leetcode.cn/problems/corporate-flight-bookings/) (Medium)
- [ ] [3355. Zero Array Transformation I](https://leetcode.cn/problems/zero-array-transformation-i/) (Medium)
- [x] [56. Merge Intervals](https://leetcode.cn/problems/merge-intervals/) (Medium)
- [x] [57. Insert Interval](https://leetcode.cn/problems/insert-interval/) (Medium)
- [ ] [732. My Calendar III](https://leetcode.cn/problems/my-calendar-iii/) (Hard)
- [ ] [2406. Divide Intervals Into Minimum Number of Groups](https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups/) (Medium)
- [ ] [2381. Shifting Letters II](https://leetcode.cn/problems/shifting-letters-ii/) (Medium)
- [ ] [3453. Separate Squares I](https://leetcode.cn/problems/separate-squares-i/) (Medium)
- [ ] [995. Minimum Number of K Consecutive Bit Flips](https://leetcode.cn/problems/minimum-number-of-k-consecutive-bit-flips/) (Hard)
- [x] [1589. Maximum Sum Obtained of Any Permutation](https://leetcode.cn/problems/maximum-sum-obtained-of-any-permutation/) (Medium)
- [ ] [1526. Minimum Number of Increments on Subarrays to Form a Target Array](https://leetcode.cn/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/) (Hard)
- [ ] [3356. Zero Array Transformation II](https://leetcode.cn/problems/zero-array-transformation-ii/) (Medium)
- [ ] [1943. Describe the Painting](https://leetcode.cn/problems/describe-the-painting/) (Medium)
- [ ] [3224. Minimum Array Changes to Make Differences Equal](https://leetcode.cn/problems/minimum-array-changes-to-make-differences-equal/) (Medium)
- [ ] [2251. Number of Flowers in Full Bloom](https://leetcode.cn/problems/number-of-flowers-in-full-bloom/) (Hard)
- [ ] [2772. Apply Operations to Make All Array Elements Equal to Zero](https://leetcode.cn/problems/apply-operations-to-make-all-array-elements-equal-to-zero/) (Medium)
- [ ] [3229. Minimum Operations to Make Array Equal to Target](https://leetcode.cn/problems/minimum-operations-to-make-array-equal-to-target/) (Hard)
- [ ] [798. Smallest Rotation with Highest Score](https://leetcode.cn/problems/smallest-rotation-with-highest-score/) (Hard)
- [ ] [3347. Maximum Frequency of an Element After Performing Operations II](https://leetcode.cn/problems/maximum-frequency-of-an-element-after-performing-operations-ii/) (Hard)
- [ ] [2528. Maximize the Minimum Powered City](https://leetcode.cn/problems/maximize-the-minimum-powered-city/) (Hard)
- [ ] [1674. Minimum Moves to Make Array Complementary](https://leetcode.cn/problems/minimum-moves-to-make-array-complementary/) (Medium)
- [ ] [3362. Zero Array Transformation III](https://leetcode.cn/problems/zero-array-transformation-iii/) (Medium)
- [ ] [3017. Count the Number of Houses at a Certain Distance II](https://leetcode.cn/problems/count-the-number-of-houses-at-a-certain-distance-ii/) (Hard)
- [x] [253. Meeting Rooms II](https://leetcode.cn/problems/meeting-rooms-ii/) (Medium) 👑
- [x] [370. Range Addition](https://leetcode.cn/problems/range-addition/) (Medium) 👑
- [ ] [1989. Maximum Number of People That Can Be Caught in Tag](https://leetcode.cn/problems/maximum-number-of-people-that-can-be-caught-in-tag/) (Medium) 👑
- [ ] [759. Employee Free Time](https://leetcode.cn/problems/employee-free-time/) (Hard) 👑
- [ ] [2021. Brightest Position on Street](https://leetcode.cn/problems/brightest-position-on-street/) (Medium) 👑
- [ ] [2015. Average Height of Buildings in Each Segment](https://leetcode.cn/problems/average-height-of-buildings-in-each-segment/) (Medium) 👑
- [ ] [2237. Count Positions on Street With Required Brightness](https://leetcode.cn/problems/count-positions-on-street-with-required-brightness/) (Medium) 👑
- [ ] [3009. Maximum Number of Intersections on the Chart](https://leetcode.cn/problems/maximum-number-of-intersections-on-the-chart/) (Hard) 👑
- [ ] [3279. Maximum Total Area Occupied by Pistons](https://leetcode.cn/problems/maximum-total-area-occupied-by-pistons/) (Hard) 👑

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

## 1893. Check if All the Integers in a Range Are Covered

-   [LeetCode](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/) | [LeetCode CH](https://leetcode.cn/problems/check-if-all-the-integers-in-a-range-are-covered/) (Easy)

-   Tags: array, hash table, prefix sum
## 1854. Maximum Population Year

-   [LeetCode](https://leetcode.com/problems/maximum-population-year/) | [LeetCode CH](https://leetcode.cn/problems/maximum-population-year/) (Easy)

-   Tags: array, counting, prefix sum
## 2960. Count Tested Devices After Test Operations

-   [LeetCode](https://leetcode.com/problems/count-tested-devices-after-test-operations/) | [LeetCode CH](https://leetcode.cn/problems/count-tested-devices-after-test-operations/) (Easy)

-   Tags: array, simulation, counting
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

## 3355. Zero Array Transformation I

-   [LeetCode](https://leetcode.com/problems/zero-array-transformation-i/) | [LeetCode CH](https://leetcode.cn/problems/zero-array-transformation-i/) (Medium)

-   Tags: array, prefix sum
## 56. Merge Intervals

-   [LeetCode](https://leetcode.com/problems/merge-intervals/) | [LeetCode CH](https://leetcode.cn/problems/merge-intervals/) (Medium)

-   Tags: array, sorting
-   Merge all overlapping intervals.

<iframe width="560" height="315" src="https://www.youtube.com/embed/44H3cEC2fFM?si=J-Jr_Fg2eDse3-de" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


```python title="56. Merge Intervals - Python Solution"
from typing import List


# Intervals
def merge(intervals: List[List[int]]) -> List[List[int]]:
    n = len(intervals)
    if n <= 1:
        return intervals

    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]

    for i in range(1, n):
        if intervals[i][0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])

    return res


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# [[1, 6], [8, 10], [15, 18]]

```

```cpp title="56. Merge Intervals - C++ Solution"
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// Interval
vector<vector<int>> merge(vector<vector<int>>& intervals) {
    sort(intervals.begin(), intervals.end());
    vector<vector<int>> res;

    for (auto& range : intervals) {
        if (!res.empty() && range[0] <= res.back()[1]) {
            res.back()[1] = max(res.back()[1], range[1]);
        } else {
            res.emplace_back(range);
        }
    }
    return res;
}

int main() {
    vector<vector<int>> intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
    vector<vector<int>> res = merge(intervals);
    for (auto& range : res) {
        cout << range[0] << ", " << range[1] << endl;
    }
    return 0;
}

```

## 57. Insert Interval

-   [LeetCode](https://leetcode.com/problems/insert-interval/) | [LeetCode CH](https://leetcode.cn/problems/insert-interval/) (Medium)

-   Tags: array

```python title="57. Insert Interval - Python Solution"
from typing import List


# Interval
def insert(
    intervals: List[List[int]], newInterval: List[int]
) -> List[List[int]]:
    n = len(intervals)

    if n == 0:
        return [newInterval]

    if newInterval[1] < intervals[0][0]:
        return [newInterval] + intervals

    if newInterval[0] > intervals[-1][1]:
        return intervals + [newInterval]

    i = 0
    result = []

    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    while i < n:
        result.append(intervals[i])
        i += 1

    return result


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(insert(intervals, newInterval))  # [[1, 5], [6, 9]]

```

## 732. My Calendar III

-   [LeetCode](https://leetcode.com/problems/my-calendar-iii/) | [LeetCode CH](https://leetcode.cn/problems/my-calendar-iii/) (Hard)

-   Tags: binary search, design, segment tree, prefix sum, ordered set
## 2406. Divide Intervals Into Minimum Number of Groups

-   [LeetCode](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/) | [LeetCode CH](https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups/) (Medium)

-   Tags: array, two pointers, greedy, sorting, heap priority queue, prefix sum
## 2381. Shifting Letters II

-   [LeetCode](https://leetcode.com/problems/shifting-letters-ii/) | [LeetCode CH](https://leetcode.cn/problems/shifting-letters-ii/) (Medium)

-   Tags: array, string, prefix sum
## 3453. Separate Squares I

-   [LeetCode](https://leetcode.com/problems/separate-squares-i/) | [LeetCode CH](https://leetcode.cn/problems/separate-squares-i/) (Medium)

-   Tags: array, binary search
## 995. Minimum Number of K Consecutive Bit Flips

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-k-consecutive-bit-flips/) (Hard)

-   Tags: array, bit manipulation, queue, sliding window, prefix sum
## 1589. Maximum Sum Obtained of Any Permutation

-   [LeetCode](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/) | [LeetCode CH](https://leetcode.cn/problems/maximum-sum-obtained-of-any-permutation/) (Medium)

-   Tags: array, greedy, sorting, prefix sum

```python title="1589. Maximum Sum Obtained of Any Permutation - Python Solution"
from typing import List


# Greedy
def maxSumRangeQuery(nums: List[int], requests: List[List[int]]) -> int:
    n = len(nums)
    freq = [0 for _ in range(n + 1)]

    for start, end in requests:
        freq[start] += 1
        if end + 1 < n:
            freq[end + 1] -= 1

    for i in range(1, n):
        freq[i] += freq[i - 1]

    freq.pop()

    freq.sort(reverse=True)
    nums.sort(reverse=True)

    max_sum = 0
    mod = 10**9 + 7

    for i, j in zip(nums, freq):
        max_sum += i * j
        max_sum %= mod

    return max_sum


nums = [1, 2, 3, 4, 5]
requests = [[1, 3], [0, 1]]
print(maxSumRangeQuery(nums, requests))  # 19

```

## 1526. Minimum Number of Increments on Subarrays to Form a Target Array

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/) (Hard)

-   Tags: array, dynamic programming, stack, greedy, monotonic stack
## 3356. Zero Array Transformation II

-   [LeetCode](https://leetcode.com/problems/zero-array-transformation-ii/) | [LeetCode CH](https://leetcode.cn/problems/zero-array-transformation-ii/) (Medium)

-   Tags: array, binary search, prefix sum
## 1943. Describe the Painting

-   [LeetCode](https://leetcode.com/problems/describe-the-painting/) | [LeetCode CH](https://leetcode.cn/problems/describe-the-painting/) (Medium)

-   Tags: array, hash table, sorting, prefix sum
## 3224. Minimum Array Changes to Make Differences Equal

-   [LeetCode](https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/) | [LeetCode CH](https://leetcode.cn/problems/minimum-array-changes-to-make-differences-equal/) (Medium)

-   Tags: array, hash table, prefix sum
## 2251. Number of Flowers in Full Bloom

-   [LeetCode](https://leetcode.com/problems/number-of-flowers-in-full-bloom/) | [LeetCode CH](https://leetcode.cn/problems/number-of-flowers-in-full-bloom/) (Hard)

-   Tags: array, hash table, binary search, sorting, prefix sum, ordered set
## 2772. Apply Operations to Make All Array Elements Equal to Zero

-   [LeetCode](https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/) | [LeetCode CH](https://leetcode.cn/problems/apply-operations-to-make-all-array-elements-equal-to-zero/) (Medium)

-   Tags: array, prefix sum
## 3229. Minimum Operations to Make Array Equal to Target

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-make-array-equal-to-target/) (Hard)

-   Tags: array, dynamic programming, stack, greedy, monotonic stack
## 798. Smallest Rotation with Highest Score

-   [LeetCode](https://leetcode.com/problems/smallest-rotation-with-highest-score/) | [LeetCode CH](https://leetcode.cn/problems/smallest-rotation-with-highest-score/) (Hard)

-   Tags: array, prefix sum
## 3347. Maximum Frequency of an Element After Performing Operations II

-   [LeetCode](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/) | [LeetCode CH](https://leetcode.cn/problems/maximum-frequency-of-an-element-after-performing-operations-ii/) (Hard)

-   Tags: array, binary search, sliding window, sorting, prefix sum
## 2528. Maximize the Minimum Powered City

-   [LeetCode](https://leetcode.com/problems/maximize-the-minimum-powered-city/) | [LeetCode CH](https://leetcode.cn/problems/maximize-the-minimum-powered-city/) (Hard)

-   Tags: array, binary search, greedy, queue, sliding window, prefix sum
## 1674. Minimum Moves to Make Array Complementary

-   [LeetCode](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/) | [LeetCode CH](https://leetcode.cn/problems/minimum-moves-to-make-array-complementary/) (Medium)

-   Tags: array, hash table, prefix sum
## 3362. Zero Array Transformation III

-   [LeetCode](https://leetcode.com/problems/zero-array-transformation-iii/) | [LeetCode CH](https://leetcode.cn/problems/zero-array-transformation-iii/) (Medium)

-   Tags: array, greedy, sorting, heap priority queue, prefix sum
## 3017. Count the Number of Houses at a Certain Distance II

-   [LeetCode](https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/) | [LeetCode CH](https://leetcode.cn/problems/count-the-number-of-houses-at-a-certain-distance-ii/) (Hard)

-   Tags: graph, prefix sum
## 253. Meeting Rooms II

-   [LeetCode](https://leetcode.com/problems/meeting-rooms-ii/) | [LeetCode CH](https://leetcode.cn/problems/meeting-rooms-ii/) (Medium)

-   Tags: array, two pointers, greedy, sorting, heap priority queue, prefix sum

```python title="253. Meeting Rooms II - Python Solution"
import heapq
from typing import List


# Heap
def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    heap = [intervals[0][1]]

    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])

    return len(heap)


intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals))  # 2

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

## 1989. Maximum Number of People That Can Be Caught in Tag

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-people-that-can-be-caught-in-tag/) (Medium)

-   Tags: array, greedy
## 759. Employee Free Time

-   [LeetCode](https://leetcode.com/problems/employee-free-time/) | [LeetCode CH](https://leetcode.cn/problems/employee-free-time/) (Hard)

-   Tags: array, sorting, heap priority queue
## 2021. Brightest Position on Street

-   [LeetCode](https://leetcode.com/problems/brightest-position-on-street/) | [LeetCode CH](https://leetcode.cn/problems/brightest-position-on-street/) (Medium)

-   Tags: array, sorting, prefix sum, ordered set
## 2015. Average Height of Buildings in Each Segment

-   [LeetCode](https://leetcode.com/problems/average-height-of-buildings-in-each-segment/) | [LeetCode CH](https://leetcode.cn/problems/average-height-of-buildings-in-each-segment/) (Medium)

-   Tags: array, greedy, sorting, heap priority queue
## 2237. Count Positions on Street With Required Brightness

-   [LeetCode](https://leetcode.com/problems/count-positions-on-street-with-required-brightness/) | [LeetCode CH](https://leetcode.cn/problems/count-positions-on-street-with-required-brightness/) (Medium)

-   Tags: array, prefix sum
## 3009. Maximum Number of Intersections on the Chart

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-intersections-on-the-chart/) (Hard)

-   Tags: array, math, binary indexed tree, geometry
## 3279. Maximum Total Area Occupied by Pistons

-   [LeetCode](https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/) | [LeetCode CH](https://leetcode.cn/problems/maximum-total-area-occupied-by-pistons/) (Hard)

-   Tags: array, hash table, string, simulation, counting, prefix sum
