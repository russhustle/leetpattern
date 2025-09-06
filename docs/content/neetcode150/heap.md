---
comments: True
---

# Heap

## Table of Contents

- [x] [703. Kth Largest Element in a Stream](https://leetcode.cn/problems/kth-largest-element-in-a-stream/) (Easy)
- [x] [1046. Last Stone Weight](https://leetcode.cn/problems/last-stone-weight/) (Easy)
- [x] [973. K Closest Points to Origin](https://leetcode.cn/problems/k-closest-points-to-origin/) (Medium)
- [x] [215. Kth Largest Element in an Array](https://leetcode.cn/problems/kth-largest-element-in-an-array/) (Medium)
- [x] [621. Task Scheduler](https://leetcode.cn/problems/task-scheduler/) (Medium)
- [x] [355. Design Twitter](https://leetcode.cn/problems/design-twitter/) (Medium)
- [x] [295. Find Median from Data Stream](https://leetcode.cn/problems/find-median-from-data-stream/) (Hard)

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

## 973. K Closest Points to Origin

-   [LeetCode](https://leetcode.com/problems/k-closest-points-to-origin/) | [LeetCode CH](https://leetcode.cn/problems/k-closest-points-to-origin/) (Medium)

-   Tags: array, math, divide and conquer, geometry, sorting, heap priority queue, quickselect
```python title="973. K Closest Points to Origin - Python Solution"
import heapq
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []

    for x, y in points:
        dist = -(x**2 + y**2)  # max heap
        if len(heap) < k:
            heapq.heappush(heap, (dist, x, y))
        else:
            heapq.heappushpop(heap, (dist, x, y))  # push and pop the smallest

    return [[x, y] for (_, x, y) in heap]


# Time complexity: O(n * log(k))
#   - O(log(k)) for heapify
#   - O(n) for iterating through the input list
# Space complexity: O(k)

points = [[1, 3], [-2, 2]]
k = 1
print(kClosest(points, k))  # [[-2, 2]]

```

## 215. Kth Largest Element in an Array

-   [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [LeetCode CH](https://leetcode.cn/problems/kth-largest-element-in-an-array/) (Medium)

-   Tags: array, divide and conquer, sorting, heap priority queue, quickselect
```python title="215. Kth Largest Element in an Array - Python Solution"
import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    min_heap = []

    for i, num in enumerate(nums):
        heapq.heappush(min_heap, num)
        if i >= k:
            heapq.heappop(min_heap)

    return min_heap[0]


if __name__ == "__main__":
    assert findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5

```

## 621. Task Scheduler

-   [LeetCode](https://leetcode.com/problems/task-scheduler/) | [LeetCode CH](https://leetcode.cn/problems/task-scheduler/) (Medium)

-   Tags: array, hash table, greedy, sorting, heap priority queue, counting
```python title="621. Task Scheduler - Python Solution"
import heapq
from collections import Counter, deque
from typing import List


# Heap
def leastInterval1(tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    heap = [-c for c in count.values()]
    heapq.heapify(heap)

    time = 0

    q = deque()

    while heap or q:
        time += 1

        if heap:
            cnt = 1 + heapq.heappop(heap)
            if cnt:
                q.append((cnt, time + n))

        if q and q[0][1] == time:
            heapq.heappush(heap, q.popleft()[0])

    return time


def leastInterval2(tasks: List[str], n: int) -> int:
    freq = Counter(tasks)

    maxExec = max(freq.values())
    maxCount = sum(1 for v in freq.values() if v == maxExec)

    return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(leastInterval1(tasks, n))  # 8
print(leastInterval2(tasks, n))  # 8

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

## 295. Find Median from Data Stream

-   [LeetCode](https://leetcode.com/problems/find-median-from-data-stream/) | [LeetCode CH](https://leetcode.cn/problems/find-median-from-data-stream/) (Hard)

-   Tags: two pointers, design, sorting, heap priority queue, data stream
```python title="295. Find Median from Data Stream - Python Solution"
from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.min_size = 0
        self.max_size = 0

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)
        heappush(self.minHeap, -heappop(self.maxHeap))
        self.min_size += 1

        if self.min_size > self.max_size:
            heappush(self.maxHeap, -heappop(self.minHeap))
            self.min_size -= 1
            self.max_size += 1

    def findMedian(self) -> float:
        if self.min_size == self.max_size:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        return float(-self.maxHeap[0])


def test_median_finder():
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    assert obj.findMedian() == 1.5
    obj.addNum(3)
    assert obj.findMedian() == 2.0
    obj.addNum(4)
    assert obj.findMedian() == 2.5
    obj.addNum(5)
    assert obj.findMedian() == 3.0

```

```cpp title="295. Find Median from Data Stream - C++ Solution"
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

class MedianFinder {
   private:
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int max_size = 0;
    int min_size = 0;

   public:
    MedianFinder() {}

    void addNum(int num) {
        if (min_size == max_size) {
            minHeap.push(num);
            maxHeap.push(minHeap.top());
            minHeap.pop();
            max_size++;
        } else {
            maxHeap.push(num);
            minHeap.push(maxHeap.top());
            maxHeap.pop();
            min_size++;
        }
    }

    double findMedian() {
        if (min_size == max_size) {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        } else {
            return (double)maxHeap.top();
        }
    }
};

int main() {
    MedianFinder* obj = new MedianFinder();
    obj->addNum(1);
    obj->addNum(2);
    cout << obj->findMedian() << endl;  // 1.5
    obj->addNum(3);
    cout << obj->findMedian() << endl;  // 2
    return 0;
}
```
