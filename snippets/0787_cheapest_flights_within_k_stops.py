from typing import List


# Bellman-Ford
def findCheapestPriceBF(
    n: int, flights: List[List[int]], src: int, dst: int, k: int
) -> int:
    prices = [float("inf")] * n
    prices[src] = 0

    for _ in range(k + 1):
        temp_prices = prices.copy()

        for s, d, p in flights:
            if prices[s] == float("inf"):
                continue
            if prices[s] + p < temp_prices[d]:
                temp_prices[d] = prices[s] + p

        prices = temp_prices

    return prices[dst] if prices[dst] != float("inf") else -1


# |------------|---------|---------|
# |  Approach  |  Time   |  Space  |
# |------------|---------|---------|
# |Bellman-Ford| O(k * E)|  O(n)   |
# |------------|---------|---------|


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
print(findCheapestPriceBF(n, flights, src, dst, k))  # 700
