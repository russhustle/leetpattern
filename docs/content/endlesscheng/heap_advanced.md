---
comments: True
---

# Heap Advanced

## Table of Contents

- [x] [23. Merge k Sorted Lists](https://leetcode.cn/problems/merge-k-sorted-lists/) (Hard)
- [x] [355. Design Twitter](https://leetcode.cn/problems/design-twitter/) (Medium)
- [x] [502. IPO](https://leetcode.cn/problems/ipo/) (Hard)
- [ ] [1705. Maximum Number of Eaten Apples](https://leetcode.cn/problems/maximum-number-of-eaten-apples/) (Medium)
- [x] [778. Swim in Rising Water](https://leetcode.cn/problems/swim-in-rising-water/) (Hard)
- [x] [1631. Path With Minimum Effort](https://leetcode.cn/problems/path-with-minimum-effort/) (Medium)
- [ ] [1354. Construct Target Array With Multiple Sums](https://leetcode.cn/problems/construct-target-array-with-multiple-sums/) (Hard)
- [ ] [1353. Maximum Number of Events That Can Be Attended](https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/) (Medium)
- [ ] [1235. Maximum Profit in Job Scheduling](https://leetcode.cn/problems/maximum-profit-in-job-scheduling/) (Hard)
- [x] [632. Smallest Range Covering Elements from K Lists](https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/) (Hard)
- [ ] [2542. Maximum Subsequence Score](https://leetcode.cn/problems/maximum-subsequence-score/) (Medium)
- [ ] [1383. Maximum Performance of a Team](https://leetcode.cn/problems/maximum-performance-of-a-team/) (Hard)
- [ ] [2503. Maximum Number of Points From Grid Queries](https://leetcode.cn/problems/maximum-number-of-points-from-grid-queries/) (Hard)
- [ ] [2163. Minimum Difference in Sums After Removal of Elements](https://leetcode.cn/problems/minimum-difference-in-sums-after-removal-of-elements/) (Hard)
- [ ] [857. Minimum Cost to Hire K Workers](https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/) (Hard)
- [ ] [1606. Find Servers That Handled Most Number of Requests](https://leetcode.cn/problems/find-servers-that-handled-most-number-of-requests/) (Hard)
- [ ] [1851. Minimum Interval to Include Each Query](https://leetcode.cn/problems/minimum-interval-to-include-each-query/) (Hard)
- [ ] [218. The Skyline Problem](https://leetcode.cn/problems/the-skyline-problem/) (Hard)
- [ ] [407. Trapping Rain Water II](https://leetcode.cn/problems/trapping-rain-water-ii/) (Hard)
- [ ] [2940. Find Building Where Alice and Bob Can Meet](https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/) (Hard)
- [ ] [3399. Smallest Substring With Identical Characters II](https://leetcode.cn/problems/smallest-substring-with-identical-characters-ii/) (Hard)
- [ ] [2589. Minimum Time to Complete All Tasks](https://leetcode.cn/problems/minimum-time-to-complete-all-tasks/) (Hard)
- [ ] [3266. Final Array State After K Multiplication Operations II](https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-ii/) (Hard)
- [ ] [1675. Minimize Deviation in Array](https://leetcode.cn/problems/minimize-deviation-in-array/) (Hard)
- [ ] [2617. Minimum Number of Visited Cells in a Grid](https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/) (Hard)
- [ ] [2532. Time to Cross a Bridge](https://leetcode.cn/problems/time-to-cross-a-bridge/) (Hard)
- [ ] [1199. Minimum Time to Build Blocks](https://leetcode.cn/problems/minimum-time-to-build-blocks/) (Hard) 👑

## 23. Merge k Sorted Lists

-   [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/) | [LeetCode CH](https://leetcode.cn/problems/merge-k-sorted-lists/) (Hard)

-   Tags: linked list, divide and conquer, heap priority queue, merge sort
-   Prerequisite: 21. Merge Two Sorted Lists
-   Video explanation: [23. Merge K Sorted Lists - NeetCode](https://youtu.be/q5a5OiGbT6Q?si=SQ2dCvsYQ3LQctPh)

```python title="23. Merge k Sorted Lists - Python Solution"
import copy
import heapq
from typing import List, Optional

from template import ListNode


# Divide and Conquer
def mergeKListsDC(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists or len(lists) == 0:
        return None

    def mergeTwo(l1, l2):
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        cur.next = l1 if l1 else l2

        return dummy.next

    while len(lists) > 1:
        merged = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(mergeTwo(l1, l2))

        lists = merged

    return lists[0]


# Heap - Merge k Sorted
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy

    minHeap = []  # (val, idx, node)

    for idx, head in enumerate(lists):
        if head:
            heapq.heappush(minHeap, (head.val, idx, head))

    while minHeap:
        _, idx, node = heapq.heappop(minHeap)
        cur.next = node
        cur = cur.next

        node = node.next
        if node:
            heapq.heappush(minHeap, (node.val, idx, node))

    return dummy.next


n1 = ListNode.create([1, 4, 5])
n2 = ListNode.create([1, 3, 4])
n3 = ListNode.create([2, 6])
lists = [n1, n2, n3]
lists1 = copy.deepcopy(lists)
lists2 = copy.deepcopy(lists)
print(mergeKListsDC(lists1))
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
print(mergeKLists(lists2))
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

```

## 355. Design Twitter

-   [LeetCode](https://leetcode.com/problems/design-twitter/) | [LeetCode CH](https://leetcode.cn/problems/design-twitter/) (Medium)

-   Tags: hash table, linked list, design, heap priority queue
-   Similar question: [23. Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard)

```python title="355. Design Twitter - Python Solution"
import heapq
from collections import defaultdict
from typing import List


# Design
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        news_feed.extend(self.tweets[userId])
        for followee in self.followees[userId]:
            news_feed.extend(self.tweets[followee])

        return [tweet for _, tweet in heapq.nlargest(10, news_feed)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].discard(followeeId)


twitter = Twitter()
print(twitter.postTweet(1, 5))  # None
print(twitter.getNewsFeed(1))  # [5]
print(twitter.follow(1, 2))  # None
print(twitter.postTweet(2, 6))  # None
print(twitter.getNewsFeed(1))  # [6, 5]
print(twitter.unfollow(1, 2))  # None
print(twitter.getNewsFeed(1))  # [5]

```

## 502. IPO

-   [LeetCode](https://leetcode.com/problems/ipo/) | [LeetCode CH](https://leetcode.cn/problems/ipo/) (Hard)

-   Tags: array, greedy, sorting, heap priority queue
```python title="502. IPO - Python Solution"
import heapq
from typing import List


# Heap - Two Heaps
def findMaximizedCapital(
    k: int, w: int, profits: List[int], capital: List[int]
) -> int:
    """
    Time Complexity: O(k log N)
    Space Complexity: O(N)
    """
    if not profits or not capital:
        return w

    if w >= max(capital) and k >= len(capital):
        return sum(profits) + w

    max_profit = []
    min_capital = [(c, p) for c, p in zip(capital, profits)]
    heapq.heapify(min_capital)

    for _ in range(k):
        while min_capital and min_capital[0][0] <= w:
            _, pro = heapq.heappop(min_capital)
            heapq.heappush(max_profit, -pro)

        if max_profit:
            w += -heapq.heappop(max_profit)

    return w


if __name__ == "__main__":
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    assert findMaximizedCapital(k, w, profits, capital) == 4

```

## 1705. Maximum Number of Eaten Apples

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-eaten-apples/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-eaten-apples/) (Medium)

-   Tags: array, greedy, heap priority queue
## 778. Swim in Rising Water

-   [LeetCode](https://leetcode.com/problems/swim-in-rising-water/) | [LeetCode CH](https://leetcode.cn/problems/swim-in-rising-water/) (Hard)

-   Tags: array, binary search, depth first search, breadth first search, union find, heap priority queue, matrix
-   Return the minimum time when you can reach the target.

![778](https://assets.leetcode.com/uploads/2021/06/29/swim2-grid-1.jpg)

```python title="778. Swim in Rising Water - Python Solution"
import heapq
from typing import List


# Dijkstra's
def swimInWater(grid: List[List[int]]) -> int:
    n = len(grid)
    visited = set()
    minHeap = [(grid[0][0], 0, 0)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited.add((0, 0))

    while minHeap:
        time, r, c = heapq.heappop(minHeap)

        if r == n - 1 and c == n - 1:
            return time

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if nr in range(n) and nc in range(n) and (nr, nc) not in visited:
                visited.add((nr, nc))
                heapq.heappush(minHeap, (max(time, grid[nr][nc]), nr, nc))


grid = [
    [0, 1, 2, 3, 4],
    [24, 23, 22, 21, 5],
    [12, 13, 14, 15, 16],
    [11, 17, 18, 19, 20],
    [10, 9, 8, 7, 6],
]
print(swimInWater(grid))  # 16

```

## 1631. Path With Minimum Effort

-   [LeetCode](https://leetcode.com/problems/path-with-minimum-effort/) | [LeetCode CH](https://leetcode.cn/problems/path-with-minimum-effort/) (Medium)

-   Tags: array, binary search, depth first search, breadth first search, union find, heap priority queue, matrix
-   Return the minimum effort required to travel from the top-left to the bottom-right corner.

```python title="1631. Path With Minimum Effort - Python Solution"
import heapq
from typing import List


# Prim
def minimumEffortPath(heights: List[List[int]]) -> int:
    m, n = len(heights), len(heights[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * n for _ in range(m)]
    heap = [(0, 0, 0)]  # (effort, row, col)

    while heap:
        effort, r, c = heapq.heappop(heap)

        if visited[r][c]:
            continue

        if r == m - 1 and c == n - 1:
            return effort

        visited[r][c] = True

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                updated = max(effort, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(heap, (updated, nr, nc))

    return -1


heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
print(minimumEffortPath(heights))  # 2

```

## 1354. Construct Target Array With Multiple Sums

-   [LeetCode](https://leetcode.com/problems/construct-target-array-with-multiple-sums/) | [LeetCode CH](https://leetcode.cn/problems/construct-target-array-with-multiple-sums/) (Hard)

-   Tags: array, heap priority queue
## 1353. Maximum Number of Events That Can Be Attended

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/) (Medium)

-   Tags: array, greedy, sorting, heap priority queue
## 1235. Maximum Profit in Job Scheduling

-   [LeetCode](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) | [LeetCode CH](https://leetcode.cn/problems/maximum-profit-in-job-scheduling/) (Hard)

-   Tags: array, binary search, dynamic programming, sorting
## 632. Smallest Range Covering Elements from K Lists

-   [LeetCode](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | [LeetCode CH](https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/) (Hard)

-   Tags: array, hash table, greedy, sliding window, sorting, heap priority queue
```python title="632. Smallest Range Covering Elements from K Lists - Python Solution"
from heapq import heapify, heapreplace
from math import inf
from typing import List


# Heap
def smallestRange(nums: List[List[int]]) -> List[int]:
    heap = [(arr[0], i, 0) for i, arr in enumerate(nums)]
    heapify(heap)

    res_l = heap[0][0]
    res_r = right = max(arr[0] for arr in nums)

    while heap[0][2] + 1 < len(nums[heap[0][1]]):
        _, i, j = heap[0]
        x = nums[i][j + 1]
        heapreplace(heap, (x, i, j + 1))
        right = max(right, x)
        left = heap[0][0]
        if right - left < res_r - res_l:
            res_l, res_r = left, right

    return [res_l, res_r]


# Sliding Window Variable Min
def smallestRangeSliding(nums: List[List[int]]) -> List[int]:
    pairs = sorted((x, i) for (i, arr) in enumerate(nums) for x in arr)
    res_l, res_r = -inf, inf
    empty = len(nums)
    cnt = [0] * empty
    left = 0

    for r, i in pairs:
        if cnt[i] == 0:
            empty -= 1
        cnt[i] += 1
        while empty == 0:
            l, i = pairs[left]
            if r - l < res_r - res_l:
                res_l, res_r = l, r
            cnt[i] -= 1
            if cnt[i] == 0:
                empty += 1
            left += 1

    return [res_l, res_r]


if __name__ == "__main__":
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    assert smallestRange(nums) == [20, 24]
    assert smallestRangeSliding(nums) == [20, 24]

```

## 2542. Maximum Subsequence Score

-   [LeetCode](https://leetcode.com/problems/maximum-subsequence-score/) | [LeetCode CH](https://leetcode.cn/problems/maximum-subsequence-score/) (Medium)

-   Tags: array, greedy, sorting, heap priority queue
## 1383. Maximum Performance of a Team

-   [LeetCode](https://leetcode.com/problems/maximum-performance-of-a-team/) | [LeetCode CH](https://leetcode.cn/problems/maximum-performance-of-a-team/) (Hard)

-   Tags: array, greedy, sorting, heap priority queue
## 2503. Maximum Number of Points From Grid Queries

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-points-from-grid-queries/) (Hard)

-   Tags: array, two pointers, breadth first search, union find, sorting, heap priority queue, matrix
## 2163. Minimum Difference in Sums After Removal of Elements

-   [LeetCode](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/) | [LeetCode CH](https://leetcode.cn/problems/minimum-difference-in-sums-after-removal-of-elements/) (Hard)

-   Tags: array, dynamic programming, heap priority queue
## 857. Minimum Cost to Hire K Workers

-   [LeetCode](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/) (Hard)

-   Tags: array, greedy, sorting, heap priority queue
## 1606. Find Servers That Handled Most Number of Requests

-   [LeetCode](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/) | [LeetCode CH](https://leetcode.cn/problems/find-servers-that-handled-most-number-of-requests/) (Hard)

-   Tags: array, greedy, heap priority queue, ordered set
## 1851. Minimum Interval to Include Each Query

-   [LeetCode](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | [LeetCode CH](https://leetcode.cn/problems/minimum-interval-to-include-each-query/) (Hard)

-   Tags: array, binary search, line sweep, sorting, heap priority queue
## 218. The Skyline Problem

-   [LeetCode](https://leetcode.com/problems/the-skyline-problem/) | [LeetCode CH](https://leetcode.cn/problems/the-skyline-problem/) (Hard)

-   Tags: array, divide and conquer, binary indexed tree, segment tree, line sweep, heap priority queue, ordered set
## 407. Trapping Rain Water II

-   [LeetCode](https://leetcode.com/problems/trapping-rain-water-ii/) | [LeetCode CH](https://leetcode.cn/problems/trapping-rain-water-ii/) (Hard)

-   Tags: array, breadth first search, heap priority queue, matrix
## 2940. Find Building Where Alice and Bob Can Meet

-   [LeetCode](https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/) | [LeetCode CH](https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/) (Hard)

-   Tags: array, binary search, stack, binary indexed tree, segment tree, heap priority queue, monotonic stack
## 3399. Smallest Substring With Identical Characters II

-   [LeetCode](https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/) | [LeetCode CH](https://leetcode.cn/problems/smallest-substring-with-identical-characters-ii/) (Hard)

-   Tags: string, binary search
## 2589. Minimum Time to Complete All Tasks

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-complete-all-tasks/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-complete-all-tasks/) (Hard)

-   Tags: array, binary search, stack, greedy, sorting
## 3266. Final Array State After K Multiplication Operations II

-   [LeetCode](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/) | [LeetCode CH](https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-ii/) (Hard)

-   Tags: array, heap priority queue, simulation
## 1675. Minimize Deviation in Array

-   [LeetCode](https://leetcode.com/problems/minimize-deviation-in-array/) | [LeetCode CH](https://leetcode.cn/problems/minimize-deviation-in-array/) (Hard)

-   Tags: array, greedy, heap priority queue, ordered set
## 2617. Minimum Number of Visited Cells in a Grid

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/) (Hard)

-   Tags: array, dynamic programming, stack, breadth first search, union find, heap priority queue, matrix, monotonic stack
## 2532. Time to Cross a Bridge

-   [LeetCode](https://leetcode.com/problems/time-to-cross-a-bridge/) | [LeetCode CH](https://leetcode.cn/problems/time-to-cross-a-bridge/) (Hard)

-   Tags: array, heap priority queue, simulation
## 1199. Minimum Time to Build Blocks

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-build-blocks/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-build-blocks/) (Hard)

-   Tags: array, math, greedy, heap priority queue
