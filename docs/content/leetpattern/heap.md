---
comments: True
---

# Heap

## Table of Contents

- [x] [1046. Last Stone Weight](https://leetcode.cn/problems/last-stone-weight/) (Easy)

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
