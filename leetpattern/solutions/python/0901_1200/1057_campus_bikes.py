from heapq import heappop, heappush
from typing import List


# Heap
def assignBikes(workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
    dist = []
    done1, done2 = set(), set()
    res = [0 for _ in range(len(workers))]

    for i, w in enumerate(workers):
        for j, b in enumerate(bikes):
            d = abs(w[0] - b[0]) + abs(w[1] - b[1])
            heappush(dist, (d, i, j))

    while dist:
        d, i, j = heappop(dist)
        if i not in done1 and j not in done2:
            res[i] = j
            done1.add(i)
            done2.add(j)

    return res


if __name__ == "__main__":
    workers = [[0, 0], [2, 1]]
    bikes = [[1, 2], [3, 3]]
    assert assignBikes(workers, bikes) == [1, 0]
    workers = [[0, 0], [1, 1], [2, 0]]
    bikes = [[1, 0], [2, 2], [2, 1]]
    assert assignBikes(workers, bikes) == [0, 2, 1]
