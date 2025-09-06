---
comments: True
---

# Heap Two Heaps

## Table of Contents

- [x] [295. Find Median from Data Stream](https://leetcode.cn/problems/find-median-from-data-stream/) (Hard)
- [x] [480. Sliding Window Median](https://leetcode.cn/problems/sliding-window-median/) (Hard)
- [x] [502. IPO](https://leetcode.cn/problems/ipo/) (Hard)

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
