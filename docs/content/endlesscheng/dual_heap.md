---
comments: True
---

# Dual Heap

## Table of Contents

- [ ] [2102. Sequentially Ordinal Rank Tracker](https://leetcode.cn/problems/sequentially-ordinal-rank-tracker/) (Hard)
- [x] [295. Find Median from Data Stream](https://leetcode.cn/problems/find-median-from-data-stream/) (Hard)
- [x] [480. Sliding Window Median](https://leetcode.cn/problems/sliding-window-median/) (Hard)
- [ ] [1825. Finding MK Average](https://leetcode.cn/problems/finding-mk-average/) (Hard)
- [ ] [3013. Divide an Array Into Subarrays With Minimum Cost II](https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/) (Hard)
- [ ] [3321. Find X-Sum of All K-Long Subarrays II](https://leetcode.cn/problems/find-x-sum-of-all-k-long-subarrays-ii/) (Hard)
- [ ] [3369. Design an Array Statistics Tracker ](https://leetcode.cn/problems/design-an-array-statistics-tracker/) (Hard) 👑
- [ ] [3422. Minimum Operations to Make Subarray Elements Equal](https://leetcode.cn/problems/minimum-operations-to-make-subarray-elements-equal/) (Medium) 👑

## 2102. Sequentially Ordinal Rank Tracker

-   [LeetCode](https://leetcode.com/problems/sequentially-ordinal-rank-tracker/) | [LeetCode CH](https://leetcode.cn/problems/sequentially-ordinal-rank-tracker/) (Hard)

-   Tags: design, heap priority queue, data stream, ordered set
## 295. Find Median from Data Stream

-   [LeetCode](https://leetcode.com/problems/find-median-from-data-stream/) | [LeetCode CH](https://leetcode.cn/problems/find-median-from-data-stream/) (Hard)

-   Tags: two pointers, design, sorting, heap priority queue, data stream

```python title="295. Find Median from Data Stream - Python Solution"
from heapq import heappop, heappush


# Dual Heaps
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
        return -self.maxHeap[0]


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
assert obj.findMedian() == 1.5
obj.addNum(3)
assert obj.findMedian() == 2
obj.addNum(4)
assert obj.findMedian() == 2.5
obj.addNum(5)
assert obj.findMedian() == 3
print("All Passed.")

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

## 480. Sliding Window Median

-   [LeetCode](https://leetcode.com/problems/sliding-window-median/) | [LeetCode CH](https://leetcode.cn/problems/sliding-window-median/) (Hard)

-   Tags: array, hash table, sliding window, heap priority queue

```python title="480. Sliding Window Median - Python Solution"
import heapq
from typing import List

from sortedcontainers import SortedList


# Heap - Two Heaps
def medianSlidingWindow1(nums: List[int], k: int) -> List[float]:
    min_heap, max_heap = [], []

    for i in range(k):
        heapq.heappush(min_heap, (nums[i], i))
    for i in range(k // 2):
        n, idx = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-n, idx))

    res = [
        (
            (min_heap[0][0] - max_heap[0][0]) / 2
            if k % 2 == 0
            else min_heap[0][0] * 1.0
        )
    ]

    for i in range(k, len(nums)):
        if nums[i] < min_heap[0][0]:
            heapq.heappush(max_heap, (-nums[i], i))

            if nums[i - k] >= min_heap[0][0]:
                n, idx = heapq.heappop(max_heap)
                heapq.heappush(min_heap, (-n, idx))
        else:
            heapq.heappush(min_heap, (nums[i], i))

            if nums[i - k] <= min_heap[0][0]:
                n, idx = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-n, idx))

        while min_heap and min_heap[0][1] <= i - k:
            heapq.heappop(min_heap)
        while max_heap and max_heap[0][1] <= i - k:
            heapq.heappop(max_heap)

        res.append(
            (min_heap[0][0] - max_heap[0][0]) / 2
            if k % 2 == 0
            else min_heap[0][0] * 1.0
        )

    return res


# Sorted List
def medianSlidingWindow2(nums: List[int], k: int) -> List[float]:
    window = SortedList()
    res = []

    for i in range(len(nums)):
        window.add(nums[i])

        if len(window) == k:
            if k % 2 == 1:
                res.append(window[k // 2])
            else:
                res.append((window[k // 2 - 1] + window[k // 2]) / 2.0)

            window.remove(nums[i - k + 1])

    return res


nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
k = 3
print(medianSlidingWindow1(nums, k))
print(medianSlidingWindow2(nums, k))

```

## 1825. Finding MK Average

-   [LeetCode](https://leetcode.com/problems/finding-mk-average/) | [LeetCode CH](https://leetcode.cn/problems/finding-mk-average/) (Hard)

-   Tags: design, queue, heap priority queue, data stream, ordered set
## 3013. Divide an Array Into Subarrays With Minimum Cost II

-   [LeetCode](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/) | [LeetCode CH](https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/) (Hard)

-   Tags: array, hash table, sliding window, heap priority queue
## 3321. Find X-Sum of All K-Long Subarrays II

-   [LeetCode](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/) | [LeetCode CH](https://leetcode.cn/problems/find-x-sum-of-all-k-long-subarrays-ii/) (Hard)

-   Tags: array, hash table, sliding window, heap priority queue
## 3369. Design an Array Statistics Tracker

-   [LeetCode](https://leetcode.com/problems/design-an-array-statistics-tracker/) | [LeetCode CH](https://leetcode.cn/problems/design-an-array-statistics-tracker/) (Hard)

-   Tags: hash table, binary search, design, queue, heap priority queue, data stream, ordered set
## 3422. Minimum Operations to Make Subarray Elements Equal

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-make-subarray-elements-equal/) (Medium)

-   Tags: array, hash table, math, sliding window, heap priority queue
