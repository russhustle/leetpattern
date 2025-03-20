---
comments: True
---

# Heap Basics

## Table of Contents

- [x] [1046. Last Stone Weight](https://leetcode.cn/problems/last-stone-weight/) (Easy)
- [x] [3264. Final Array State After K Multiplication Operations I](https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-i/) (Easy)
- [ ] [2558. Take Gifts From the Richest Pile](https://leetcode.cn/problems/take-gifts-from-the-richest-pile/) (Easy)
- [ ] [2336. Smallest Number in Infinite Set](https://leetcode.cn/problems/smallest-number-in-infinite-set/) (Medium)
- [ ] [2530. Maximal Score After Applying K Operations](https://leetcode.cn/problems/maximal-score-after-applying-k-operations/) (Medium)
- [ ] [3066. Minimum Operations to Exceed Threshold Value II](https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-ii/) (Medium)
- [ ] [1962. Remove Stones to Minimize the Total](https://leetcode.cn/problems/remove-stones-to-minimize-the-total/) (Medium)
- [x] [703. Kth Largest Element in a Stream](https://leetcode.cn/problems/kth-largest-element-in-a-stream/) (Easy)
- [ ] [3275. K-th Nearest Obstacle Queries](https://leetcode.cn/problems/k-th-nearest-obstacle-queries/) (Medium)
- [ ] [2208. Minimum Operations to Halve Array Sum](https://leetcode.cn/problems/minimum-operations-to-halve-array-sum/) (Medium)
- [ ] [2233. Maximum Product After K Increments](https://leetcode.cn/problems/maximum-product-after-k-increments/) (Medium)
- [ ] [3296. Minimum Number of Seconds to Make Mountain Height Zero](https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero/) (Medium)
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
- [ ] [1167. Minimum Cost to Connect Sticks](https://leetcode.cn/problems/minimum-cost-to-connect-sticks/) (Medium) 👑

## 1046. Last Stone Weight

-   [LeetCode](https://leetcode.com/problems/last-stone-weight/) | [LeetCode CH](https://leetcode.cn/problems/last-stone-weight/) (Easy)

-   Tags: array, heap priority queue

```python title="1046. Last Stone Weight - Python Solution"
import heapq
from typing import List


# Heap
def lastStoneWeightHeap(stones: List[int]) -> int:
    heap = [-stone for stone in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        s1 = heapq.heappop(heap)
        s2 = heapq.heappop(heap)

        if s1 != s2:
            heapq.heappush(heap, s1 - s2)

    return -heap[0] if heap else 0


# 0/1 Knapsack
def lastStoneWeightKnapsack(stones: List[int]) -> int:
    total = sum(stones)
    target = total // 2

    dp = [0 for _ in range(target + 1)]

    for i in stones:
        for j in range(target, i - 1, -1):
            dp[j] = max(dp[j], dp[j - i] + i)

    return total - 2 * dp[target]


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |    Heap     |   O(n log n)    |     O(n)     |
# |  Knapsack   |      O(n)       |     O(n)     |
# |-------------|-----------------|--------------|


stones = [2, 7, 4, 1, 8, 1]
print(lastStoneWeightHeap(stones))  # 1
print(lastStoneWeightKnapsack(stones))  # 1

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

## 2336. Smallest Number in Infinite Set

-   [LeetCode](https://leetcode.com/problems/smallest-number-in-infinite-set/) | [LeetCode CH](https://leetcode.cn/problems/smallest-number-in-infinite-set/) (Medium)

-   Tags: hash table, design, heap priority queue, ordered set

## 2530. Maximal Score After Applying K Operations

-   [LeetCode](https://leetcode.com/problems/maximal-score-after-applying-k-operations/) | [LeetCode CH](https://leetcode.cn/problems/maximal-score-after-applying-k-operations/) (Medium)

-   Tags: array, greedy, heap priority queue

## 3066. Minimum Operations to Exceed Threshold Value II

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-ii/) (Medium)

-   Tags: array, heap priority queue, simulation

## 1962. Remove Stones to Minimize the Total

-   [LeetCode](https://leetcode.com/problems/remove-stones-to-minimize-the-total/) | [LeetCode CH](https://leetcode.cn/problems/remove-stones-to-minimize-the-total/) (Medium)

-   Tags: array, greedy, heap priority queue

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

## 2208. Minimum Operations to Halve Array Sum

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-halve-array-sum/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-halve-array-sum/) (Medium)

-   Tags: array, greedy, heap priority queue

## 2233. Maximum Product After K Increments

-   [LeetCode](https://leetcode.com/problems/maximum-product-after-k-increments/) | [LeetCode CH](https://leetcode.cn/problems/maximum-product-after-k-increments/) (Medium)

-   Tags: array, greedy, heap priority queue

## 3296. Minimum Number of Seconds to Make Mountain Height Zero

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero/) (Medium)

-   Tags: array, math, binary search, greedy, heap priority queue

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

## 1167. Minimum Cost to Connect Sticks

-   [LeetCode](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-to-connect-sticks/) (Medium)

-   Tags: array, greedy, heap priority queue
