import heapq
from typing import List


# Heap - Two Heaps
def findMaximizedCapital(
    k: int, w: int, profits: List[int], capital: List[int]
) -> int:
    if not profits or not capital:
        return w

    minHeap = []
    maxHeap = []

    for i in range(len(profits)):
        heapq.heappush(minHeap, (capital[i], profits[i]))

    for _ in range(k):
        while minHeap and minHeap[0][0] <= w:
            capital, profit = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -profit)

        if not maxHeap:
            break

        w += -heapq.heappop(maxHeap)

    return w


k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
print(findMaximizedCapital(k, w, profits, capital))  # 4
