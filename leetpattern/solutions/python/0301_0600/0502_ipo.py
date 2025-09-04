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
