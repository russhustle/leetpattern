"""
- Heap
    - Time: O(n log n); Space: O(n)
- 0/1 Knapsack
    - Time: O(n); Space: O(n)
"""

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
