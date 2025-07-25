---
comments: True
---

# Heap Basics

## Table of Contents

- [x] [1046. Last Stone Weight](https://leetcode.cn/problems/last-stone-weight/) (Easy)
- [x] [3264. Final Array State After K Multiplication Operations I](https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-i/) (Easy)
- [x] [2558. Take Gifts From the Richest Pile](https://leetcode.cn/problems/take-gifts-from-the-richest-pile/) (Easy)
- [x] [2336. Smallest Number in Infinite Set](https://leetcode.cn/problems/smallest-number-in-infinite-set/) (Medium)
- [x] [2530. Maximal Score After Applying K Operations](https://leetcode.cn/problems/maximal-score-after-applying-k-operations/) (Medium)
- [x] [3066. Minimum Operations to Exceed Threshold Value II](https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-ii/) (Medium)
- [x] [1962. Remove Stones to Minimize the Total](https://leetcode.cn/problems/remove-stones-to-minimize-the-total/) (Medium)
- [x] [703. Kth Largest Element in a Stream](https://leetcode.cn/problems/kth-largest-element-in-a-stream/) (Easy)
- [x] [3275. K-th Nearest Obstacle Queries](https://leetcode.cn/problems/k-th-nearest-obstacle-queries/) (Medium)
- [ ] [2208. Minimum Operations to Halve Array Sum](https://leetcode.cn/problems/minimum-operations-to-halve-array-sum/) (Medium)
- [ ] [2233. Maximum Product After K Increments](https://leetcode.cn/problems/maximum-product-after-k-increments/) (Medium)
- [x] [3296. Minimum Number of Seconds to Make Mountain Height Zero](https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero/) (Medium)
- [ ] [1942. The Number of the Smallest Unoccupied Chair](https://leetcode.cn/problems/the-number-of-the-smallest-unoccupied-chair/) (Medium)
- [ ] [1801. Number of Orders in the Backlog](https://leetcode.cn/problems/number-of-orders-in-the-backlog/) (Medium)
- [ ] [2406. Divide Intervals Into Minimum Number of Groups](https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups/) (Medium)
- [ ] [2462. Total Cost to Hire K Workers](https://leetcode.cn/problems/total-cost-to-hire-k-workers/) (Medium)
- [ ] [1834. Single-Threaded CPU](https://leetcode.cn/problems/single-threaded-cpu/) (Medium)
- [ ] [3408. Design Task Manager](https://leetcode.cn/problems/design-task-manager/) (Medium)
- [ ] [1792. Maximum Average Pass Ratio](https://leetcode.cn/problems/maximum-average-pass-ratio/) (Medium)
- [ ] [2931. Maximum Spending After Buying Items](https://leetcode.cn/problems/maximum-spending-after-buying-items/) (Hard)
- [ ] [1882. Process Tasks Using Servers](https://leetcode.cn/problems/process-tasks-using-servers/) (Medium)
- [ ] [2402. Meeting Rooms III](https://leetcode.cn/problems/meeting-rooms-iii/) (Hard)
- [x] [253. Meeting Rooms II](https://leetcode.cn/problems/meeting-rooms-ii/) (Medium) 👑
- [x] [1167. Minimum Cost to Connect Sticks](https://leetcode.cn/problems/minimum-cost-to-connect-sticks/) (Medium) 👑

## 1046. Last Stone Weight

-   [LeetCode](https://leetcode.com/problems/last-stone-weight/) | [LeetCode CH](https://leetcode.cn/problems/last-stone-weight/) (Easy)

-   Tags: array, heap priority queue
- Heap
    - Time: O(n log n); Space: O(n)
- 0/1 Knapsack
    - Time: O(n); Space: O(n)


```python title="1046. Last Stone Weight - Python Solution"
from heapq import heapify, heappop, heappush
from typing import List


# Heap
def lastStoneWeightHeap(stones: List[int]) -> int:
    maxHeap = [-s for s in stones]
    heapify(maxHeap)

    while len(maxHeap) > 1:
        s1 = heappop(maxHeap)
        s2 = heappop(maxHeap)

        if s1 != s2:
            heappush(maxHeap, s1 - s2)

    return -maxHeap[0] if maxHeap else 0


# 0/1 Knapsack
def lastStoneWeightKnapsack(stones: List[int]) -> int:
    total = sum(stones)
    target = total // 2

    dp = [0 for _ in range(target + 1)]

    for i in stones:
        for j in range(target, i - 1, -1):
            dp[j] = max(dp[j], dp[j - i] + i)

    return total - 2 * dp[target]


if __name__ == "__main__":
    stones = [2, 7, 4, 1, 8, 1]
    assert lastStoneWeightHeap(stones) == 1
    assert lastStoneWeightKnapsack(stones) == 1

```

```cpp title="1046. Last Stone Weight - C++ Solution"
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int lastStoneWeight(vector<int> &stones)
{
    priority_queue<int> maxHeap(stones.begin(), stones.end());

    while (maxHeap.size() >= 1)
    {
        int first = maxHeap.top();
        maxHeap.pop();
        int second = maxHeap.top();
        maxHeap.pop();

        if (first != second)
        {
            maxHeap.push(first - second);
        }
    }

    return maxHeap.empty() ? 0 : maxHeap.top();
}

int main()
{
    vector<int> stones = {2, 7, 4, 1, 8, 1};
    cout << lastStoneWeight(stones) << endl; // 1
    return 0;
}

```

## 3264. Final Array State After K Multiplication Operations I

-   [LeetCode](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/) | [LeetCode CH](https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-i/) (Easy)

-   Tags: array, math, heap priority queue, simulation

```python title="3264. Final Array State After K Multiplication Operations I - Python Solution"
import heapq
from typing import List


# Brute Force
def getFinalStateBF(nums: List[int], k: int, multiplier: int) -> List[int]:
    for _ in range(k):
        minNum = min(nums)
        idx = nums.index(minNum)
        nums[idx] *= multiplier

    return nums


# Heap
def getFinalStateHeap(nums: List[int], k: int, multiplier: int) -> List[int]:
    minHeap = []
    for idx, num in enumerate(nums):
        heapq.heappush(minHeap, (num, idx))

    for _ in range(k):
        num, idx = heapq.heappop(minHeap)
        nums[idx] = num * multiplier
        heapq.heappush(minHeap, (nums[idx], idx))

    return nums


k = 5
multiplier = 2
print(getFinalStateBF([2, 1, 3, 5, 6], k, multiplier))  # [8, 4, 6, 5, 6]
print(getFinalStateHeap([2, 1, 3, 5, 6], k, multiplier))  # [8, 4, 6, 5, 6]

```

## 2558. Take Gifts From the Richest Pile

-   [LeetCode](https://leetcode.com/problems/take-gifts-from-the-richest-pile/) | [LeetCode CH](https://leetcode.cn/problems/take-gifts-from-the-richest-pile/) (Easy)

-   Tags: array, heap priority queue, simulation

```python title="2558. Take Gifts From the Richest Pile - Python Solution"
from heapq import heapify, heappop, heappush
from math import isqrt
from typing import List


# Heap
def pickGifts(gifts: List[int], k: int) -> int:
    maxHeap = [-g for g in gifts]
    heapify(maxHeap)

    for _ in range(k):
        cur = heappop(maxHeap)

        if cur == -1:
            heappush(maxHeap, cur)
            break

        heappush(maxHeap, -isqrt(-cur))

    return sum(-i for i in maxHeap)


if __name__ == "__main__":
    assert pickGifts([25, 64, 9, 4, 100], 4) == 29
    assert pickGifts([1, 1, 1, 1], 4) == 0

```

## 2336. Smallest Number in Infinite Set

-   [LeetCode](https://leetcode.com/problems/smallest-number-in-infinite-set/) | [LeetCode CH](https://leetcode.cn/problems/smallest-number-in-infinite-set/) (Medium)

-   Tags: hash table, design, heap priority queue, ordered set

```python title="2336. Smallest Number in Infinite Set - Python Solution"
from heapq import heappop, heappush


# Heap
class SmallestInfiniteSet:
    def __init__(self):
        self.cur_min = 1
        self.added = set()
        self.min_heap = []

    def popSmallest(self) -> int:
        if self.min_heap:
            res = heappop(self.min_heap)
            self.added.remove(res)
            return res

        res = self.cur_min
        self.cur_min += 1
        return res

    def addBack(self, num: int) -> None:
        if num < self.cur_min and num not in self.added:
            self.added.add(num)
            heappush(self.min_heap, num)


if __name__ == "__main__":
    sis = SmallestInfiniteSet()
    assert sis.popSmallest() == 1
    sis.addBack(2)
    assert sis.popSmallest() == 2
    assert sis.popSmallest() == 3
    sis.addBack(1)
    assert sis.popSmallest() == 1
    assert sis.popSmallest() == 4
    sis.addBack(3)
    assert sis.popSmallest() == 3

```

## 2530. Maximal Score After Applying K Operations

-   [LeetCode](https://leetcode.com/problems/maximal-score-after-applying-k-operations/) | [LeetCode CH](https://leetcode.cn/problems/maximal-score-after-applying-k-operations/) (Medium)

-   Tags: array, greedy, heap priority queue

```python title="2530. Maximal Score After Applying K Operations - Python Solution"
from heapq import heapify, heappop, heappush
from math import ceil
from typing import List


# Heap
def maxKelements(nums: List[int], k: int) -> int:
    res = 0
    maxHeap = [-n for n in nums]
    heapify(maxHeap)

    while k > 0:
        cur = -heappop(maxHeap)
        res += cur
        heappush(maxHeap, -ceil(cur / 3))
        k -= 1

    return res


if __name__ == "__main__":
    assert maxKelements([10, 10, 10, 10, 10], 5) == 50
    assert maxKelements([1, 10, 3, 3, 3], 3) == 17
    assert maxKelements([1, 2, 3, 4, 5], 5) == 16

```

## 3066. Minimum Operations to Exceed Threshold Value II

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-ii/) (Medium)

-   Tags: array, heap priority queue, simulation

```python title="3066. Minimum Operations to Exceed Threshold Value II - Python Solution"
from heapq import heapify, heappop, heappush
from typing import List


# Heap
def minOperations(nums: List[int], k: int) -> int:
    heapify(nums)
    res = 0

    while nums[0] < k:
        x = heappop(nums)
        y = heappop(nums)
        heappush(nums, x * 2 + y)
        res += 1

    return res


if __name__ == "__main__":
    assert minOperations([2, 11, 10, 1, 3], 10) == 2
    assert minOperations([1, 1, 2, 4, 9], 20) == 4

```

## 1962. Remove Stones to Minimize the Total

-   [LeetCode](https://leetcode.com/problems/remove-stones-to-minimize-the-total/) | [LeetCode CH](https://leetcode.cn/problems/remove-stones-to-minimize-the-total/) (Medium)

-   Tags: array, greedy, heap priority queue

```python title="1962. Remove Stones to Minimize the Total - Python Solution"
from heapq import heapify, heapreplace
from typing import List


# Heap
def minStoneSum(piles: List[int], k: int) -> int:
    maxHeap = [-p for p in piles]
    heapify(maxHeap)

    for _ in range(k):
        heapreplace(maxHeap, maxHeap[0] // 2)

    return -sum(maxHeap)


if __name__ == "__main__":
    assert minStoneSum([5, 4, 9], 2) == 12
    assert minStoneSum([4, 3, 6, 7], 3) == 12

```

## 703. Kth Largest Element in a Stream

-   [LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | [LeetCode CH](https://leetcode.cn/problems/kth-largest-element-in-a-stream/) (Easy)

-   Tags: tree, design, binary search tree, heap priority queue, binary tree, data stream

```python title="703. Kth Largest Element in a Stream - Python Solution"
import heapq
from typing import List


# Heap
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))  # 4
print(obj.add(5))  # 5
print(obj.add(10))  # 5

```

## 3275. K-th Nearest Obstacle Queries

-   [LeetCode](https://leetcode.com/problems/k-th-nearest-obstacle-queries/) | [LeetCode CH](https://leetcode.cn/problems/k-th-nearest-obstacle-queries/) (Medium)

-   Tags: array, heap priority queue

```python title="3275. K-th Nearest Obstacle Queries - Python Solution"
from heapq import heappop, heappush
from typing import List


# Heap
def resultsArray(queries: List[List[int]], k: int) -> List[int]:
    n = len(queries)
    res = [-1 for _ in range(n)]
    maxHeap = []

    for i in range(n):
        dist = abs(queries[i][0]) + abs(queries[i][1])
        heappush(maxHeap, -dist)

        if i < k - 1:
            continue

        while len(maxHeap) > k:
            heappop(maxHeap)

        res[i] = -maxHeap[0]

    return res


if __name__ == "__main__":
    queries = [[1, 2], [3, 4], [2, 3], [-3, 0]]
    k = 2
    assert resultsArray(queries, k) == [-1, 7, 5, 3]

```

## 2208. Minimum Operations to Halve Array Sum

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-halve-array-sum/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-halve-array-sum/) (Medium)

-   Tags: array, greedy, heap priority queue
## 2233. Maximum Product After K Increments

-   [LeetCode](https://leetcode.com/problems/maximum-product-after-k-increments/) | [LeetCode CH](https://leetcode.cn/problems/maximum-product-after-k-increments/) (Medium)

-   Tags: array, greedy, heap priority queue
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

## 1942. The Number of the Smallest Unoccupied Chair

-   [LeetCode](https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/) | [LeetCode CH](https://leetcode.cn/problems/the-number-of-the-smallest-unoccupied-chair/) (Medium)

-   Tags: array, hash table, heap priority queue
## 1801. Number of Orders in the Backlog

-   [LeetCode](https://leetcode.com/problems/number-of-orders-in-the-backlog/) | [LeetCode CH](https://leetcode.cn/problems/number-of-orders-in-the-backlog/) (Medium)

-   Tags: array, heap priority queue, simulation
## 2406. Divide Intervals Into Minimum Number of Groups

-   [LeetCode](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/) | [LeetCode CH](https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups/) (Medium)

-   Tags: array, two pointers, greedy, sorting, heap priority queue, prefix sum
## 2462. Total Cost to Hire K Workers

-   [LeetCode](https://leetcode.com/problems/total-cost-to-hire-k-workers/) | [LeetCode CH](https://leetcode.cn/problems/total-cost-to-hire-k-workers/) (Medium)

-   Tags: array, two pointers, heap priority queue, simulation
## 1834. Single-Threaded CPU

-   [LeetCode](https://leetcode.com/problems/single-threaded-cpu/) | [LeetCode CH](https://leetcode.cn/problems/single-threaded-cpu/) (Medium)

-   Tags: array, sorting, heap priority queue
## 3408. Design Task Manager

-   [LeetCode](https://leetcode.com/problems/design-task-manager/) | [LeetCode CH](https://leetcode.cn/problems/design-task-manager/) (Medium)

-   Tags: hash table, design, heap priority queue, ordered set
## 1792. Maximum Average Pass Ratio

-   [LeetCode](https://leetcode.com/problems/maximum-average-pass-ratio/) | [LeetCode CH](https://leetcode.cn/problems/maximum-average-pass-ratio/) (Medium)

-   Tags: array, greedy, heap priority queue
## 2931. Maximum Spending After Buying Items

-   [LeetCode](https://leetcode.com/problems/maximum-spending-after-buying-items/) | [LeetCode CH](https://leetcode.cn/problems/maximum-spending-after-buying-items/) (Hard)

-   Tags: array, greedy, sorting, heap priority queue, matrix
## 1882. Process Tasks Using Servers

-   [LeetCode](https://leetcode.com/problems/process-tasks-using-servers/) | [LeetCode CH](https://leetcode.cn/problems/process-tasks-using-servers/) (Medium)

-   Tags: array, heap priority queue
## 2402. Meeting Rooms III

-   [LeetCode](https://leetcode.com/problems/meeting-rooms-iii/) | [LeetCode CH](https://leetcode.cn/problems/meeting-rooms-iii/) (Hard)

-   Tags: array, hash table, sorting, heap priority queue, simulation
## 253. Meeting Rooms II

-   [LeetCode](https://leetcode.com/problems/meeting-rooms-ii/) | [LeetCode CH](https://leetcode.cn/problems/meeting-rooms-ii/) (Medium)

-   Tags: array, two pointers, greedy, sorting, heap priority queue, prefix sum
- Given an array of meeting time `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.


```python title="253. Meeting Rooms II - Python Solution"
import heapq
from typing import List


# Heap
def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    minHeap = [intervals[0][1]]

    for i in range(1, len(intervals)):
        if intervals[i][0] >= minHeap[0]:
            heapq.heappop(minHeap)
        heapq.heappush(minHeap, intervals[i][1])

    return len(minHeap)


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert minMeetingRooms(intervals) == 2

```

## 1167. Minimum Cost to Connect Sticks

-   [LeetCode](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-to-connect-sticks/) (Medium)

-   Tags: array, greedy, heap priority queue

```python title="1167. Minimum Cost to Connect Sticks - Python Solution"
from heapq import heapify, heappop, heappush
from typing import List


# Heap
def connectSticks(sticks: List[int]) -> int:
    n = len(sticks)
    heapify(sticks)
    res = 0

    while n > 1:
        x = heappop(sticks)
        y = heappop(sticks)
        res += x + y
        heappush(sticks, x + y)
        n -= 1

    return res


if __name__ == "__main__":
    assert connectSticks([2, 4, 3]) == 14
    assert connectSticks([1, 8, 3, 5]) == 30
    assert connectSticks([5]) == 0
    assert connectSticks([1, 2, 3, 4, 5]) == 33
    assert connectSticks([1, 1, 1]) == 5

```
