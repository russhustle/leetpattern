---
comments: True
---

# Heap

## Table of Contents

- [x] [1046. Last Stone Weight](https://leetcode.cn/problems/last-stone-weight/) (Easy)

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
