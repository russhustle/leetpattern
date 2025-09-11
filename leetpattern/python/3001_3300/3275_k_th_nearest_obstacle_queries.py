from heapq import heappop, heappush
from typing import List


# Heap
def resultsArray(queries: List[List[int]], k: int) -> List[int]:
    n = len(queries)
    res = [-1 for _ in range(n)]
    maxHeap = []

    for i in range(n):
        dist = abs(queries[i][0]) + abs(queries[i][1])
        heappush(maxHeap, -dist)

        if i < k - 1:
            continue

        while len(maxHeap) > k:
            heappop(maxHeap)

        res[i] = -maxHeap[0]

    return res


if __name__ == "__main__":
    queries = [[1, 2], [3, 4], [2, 3], [-3, 0]]
    k = 2
    assert resultsArray(queries, k) == [-1, 7, 5, 3]
