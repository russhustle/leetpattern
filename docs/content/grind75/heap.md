---
comments: True
---

# Heap

## Table of Contents

- [x] [973. K Closest Points to Origin](https://leetcode.cn/problems/k-closest-points-to-origin/) (Medium)
- [x] [621. Task Scheduler](https://leetcode.cn/problems/task-scheduler/) (Medium)
- [x] [295. Find Median from Data Stream](https://leetcode.cn/problems/find-median-from-data-stream/) (Hard)
- [x] [23. Merge k Sorted Lists](https://leetcode.cn/problems/merge-k-sorted-lists/) (Hard)

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
