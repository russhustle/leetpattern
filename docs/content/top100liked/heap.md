---
comments: True
---

# Heap

## Table of Contents

- [x] [215. Kth Largest Element in an Array](https://leetcode.cn/problems/kth-largest-element-in-an-array/) (Medium)
- [x] [347. Top K Frequent Elements](https://leetcode.cn/problems/top-k-frequent-elements/) (Medium)
- [x] [295. Find Median from Data Stream](https://leetcode.cn/problems/find-median-from-data-stream/) (Hard)

## 215. Kth Largest Element in an Array

-   [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [LeetCode CH](https://leetcode.cn/problems/kth-largest-element-in-an-array/) (Medium)

-   Tags: array, divide and conquer, sorting, heap priority queue, quickselect

```python title="215. Kth Largest Element in an Array - Python Solution"
import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    minHeap = []
    for i, num in enumerate(nums):
        heapq.heappush(minHeap, num)
        if i >= k:
            heapq.heappop(minHeap)
    return minHeap[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # 5

```

## 347. Top K Frequent Elements

-   [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/) | [LeetCode CH](https://leetcode.cn/problems/top-k-frequent-elements/) (Medium)

-   Tags: array, hash table, divide and conquer, sorting, heap priority queue, bucket sort, counting, quickselect

```python title="347. Top K Frequent Elements - Python Solution"
import heapq
from collections import Counter
from typing import List


# Heap + Counter
def topKFrequent(nums: List[int], k: int) -> List[int]:
    minHeap = []

    for val, freq in Counter(nums).items():
        if len(minHeap) < k:
            heapq.heappush(minHeap, (freq, val))
        else:
            heapq.heappushpop(minHeap, (freq, val))

    return [i for _, i in minHeap]


# Counter (Most Common)
def topKFrequentCounter(nums: List[int], k: int) -> List[int]:
    commons = Counter(nums).most_common(k)
    return [i for i, _ in commons]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))  # [1, 2]
print(topKFrequentCounter(nums, k))  # [1, 2]

```

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
