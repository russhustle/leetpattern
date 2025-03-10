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
