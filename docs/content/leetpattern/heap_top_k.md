---
comments: True
---

# Heap Top K

## Table of Contents

- [x] [215. Kth Largest Element in an Array](https://leetcode.cn/problems/kth-largest-element-in-an-array/) (Medium)
- [x] [973. K Closest Points to Origin](https://leetcode.cn/problems/k-closest-points-to-origin/) (Medium)
- [x] [347. Top K Frequent Elements](https://leetcode.cn/problems/top-k-frequent-elements/) (Medium)
- [x] [692. Top K Frequent Words](https://leetcode.cn/problems/top-k-frequent-words/) (Medium)
- [x] [264. Ugly Number II](https://leetcode.cn/problems/ugly-number-ii/) (Medium)
- [x] [451. Sort Characters By Frequency](https://leetcode.cn/problems/sort-characters-by-frequency/) (Medium)
- [x] [703. Kth Largest Element in a Stream](https://leetcode.cn/problems/kth-largest-element-in-a-stream/) (Easy)
- [x] [767. Reorganize String](https://leetcode.cn/problems/reorganize-string/) (Medium)
- [x] [786. K-th Smallest Prime Fraction](https://leetcode.cn/problems/k-th-smallest-prime-fraction/) (Medium)

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

## 692. Top K Frequent Words

-   [LeetCode](https://leetcode.com/problems/top-k-frequent-words/) | [LeetCode CH](https://leetcode.cn/problems/top-k-frequent-words/) (Medium)

-   Tags: array, hash table, string, trie, sorting, heap priority queue, bucket sort, counting
```python title="692. Top K Frequent Words - Python Solution"
import heapq
from collections import Counter
from typing import List


class WordFrequency:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        # If the frequency is different
        if self.freq != other.freq:
            # The word with the lower frequency comes first
            return self.freq < other.freq
        else:
            # The word with the lower alphabetical order comes first
            return self.word > other.word


def topKFrequent(words: List[str], k: int) -> List[str]:
    heap = []

    for word, freq in Counter(words).items():
        heapq.heappush(heap, WordFrequency(word, freq))

        if len(heap) > k:
            heapq.heappop(heap)

    heap.sort(reverse=True)
    return [x.word for x in heap]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(topKFrequent(words, k))  # ["i", "love"]

```

## 264. Ugly Number II

-   [LeetCode](https://leetcode.com/problems/ugly-number-ii/) | [LeetCode CH](https://leetcode.cn/problems/ugly-number-ii/) (Medium)

-   Tags: hash table, math, dynamic programming, heap priority queue
```python title="264. Ugly Number II - Python Solution"
import heapq


def nthUglyNumber(n: int) -> int:
    heap = [1]
    seen = set(heap)

    factors = [2, 3, 5]
    current = 1

    # Pop the smallest ugly number n times
    for _ in range(n):
        current = heapq.heappop(heap)  # Pop the smallest ugly number

        for factor in factors:
            new = current * factor
            if new not in seen:
                seen.add(new)
                heapq.heappush(heap, new)

    return current


print(nthUglyNumber(10))  # 12

```

## 451. Sort Characters By Frequency

-   [LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/) | [LeetCode CH](https://leetcode.cn/problems/sort-characters-by-frequency/) (Medium)

-   Tags: hash table, string, sorting, heap priority queue, bucket sort, counting
```python title="451. Sort Characters By Frequency - Python Solution"
import heapq
from collections import Counter


def frequencySort(s: str) -> str:
    result = ""

    # Max Heap
    heap = [(-freq, val) for val, freq in Counter(s).items()]
    heapq.heapify(heap)

    while heap:
        freq, val = heapq.heappop(heap)
        result += val * -freq

    return result


print(frequencySort("tree"))  # eert

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

## 767. Reorganize String

-   [LeetCode](https://leetcode.com/problems/reorganize-string/) | [LeetCode CH](https://leetcode.cn/problems/reorganize-string/) (Medium)

-   Tags: hash table, string, greedy, sorting, heap priority queue, counting
```python title="767. Reorganize String - Python Solution"
import heapq
from collections import Counter


def reorganizeString(s: str) -> str:
    if not s:
        return ""

    heap = [(-freq, char) for char, freq in Counter(s).items()]  # max heap
    heapq.heapify(heap)

    result = []
    prev_count, prev_char = 0, ""

    while heap:
        count, char = heapq.heappop(heap)  # pop the most frequent character
        result.append(char)  # append the character to the result

        if (
            prev_count < 0
        ):  # if the previous character still has remaining count
            heapq.heappush(heap, (prev_count, prev_char))

        prev_count = (
            count + 1
        )  # update the current character's remaining count
        prev_char = char  # update the current character

    # check if there is any invalid result
    if len(result) != len(s):
        return ""

    return "".join(result)


print(reorganizeString("aab"))

```

## 786. K-th Smallest Prime Fraction

-   [LeetCode](https://leetcode.com/problems/k-th-smallest-prime-fraction/) | [LeetCode CH](https://leetcode.cn/problems/k-th-smallest-prime-fraction/) (Medium)

-   Tags: array, two pointers, binary search, sorting, heap priority queue
```python title="786. K-th Smallest Prime Fraction - Python Solution"
import heapq
from typing import List


def kthSmallestPrimeFraction(arr: List[int], k: int) -> List[int]:
    max_heap = []

    for j in range(1, len(arr)):
        for i in range(j):
            heapq.heappush(max_heap, (-arr[i] / arr[j], arr[i], arr[j]))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

    return [max_heap[0][1], max_heap[0][2]]


arr = [1, 2, 3, 5]
k = 3
print(kthSmallestPrimeFraction(arr, k))  # [2, 5]

```
