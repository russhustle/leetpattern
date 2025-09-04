---
comments: True
---

# Heap

## Table of Contents

- [x] [215. Kth Largest Element in an Array](https://leetcode.cn/problems/kth-largest-element-in-an-array/) (Medium)
- [x] [502. IPO](https://leetcode.cn/problems/ipo/) (Hard)
- [x] [373. Find K Pairs with Smallest Sums](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/) (Medium)
- [x] [295. Find Median from Data Stream](https://leetcode.cn/problems/find-median-from-data-stream/) (Hard)

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

## 373. Find K Pairs with Smallest Sums

-   [LeetCode](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | [LeetCode CH](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/) (Medium)

-   Tags: array, heap priority queue
```python title="373. Find K Pairs with Smallest Sums - Python Solution"
import heapq
from typing import List


# Heap - Merge K Sorted
def kSmallestPairs(
    nums1: List[int], nums2: List[int], k: int
) -> List[List[int]]:
    if not nums1 or not nums2 or k <= 0:
        return []

    res = []
    min_heap = []

    for j in range(min(k, len(nums2))):
        heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))

    while k > 0 and min_heap:
        _, i, j = heapq.heappop(min_heap)
        res.append([nums1[i], nums2[j]])
        k -= 1

        if i + 1 < len(nums1):
            heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))

    return res


if __name__ == "__main__":
    nums1 = [1, 2, 4, 5, 6]
    nums2 = [3, 5, 7, 9]
    k = 3
    assert kSmallestPairs(nums1, nums2, k) == [[1, 3], [2, 3], [1, 5]]

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
