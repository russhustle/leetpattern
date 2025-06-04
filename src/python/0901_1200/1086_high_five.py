from collections import defaultdict
from heapq import heappush, heappushpop
from typing import List


# Heap
def highFive(items: List[List[int]]) -> List[List[int]]:
    hashmap = defaultdict(list)  # id: scores

    for idx, score in items:
        if len(hashmap[idx]) < 5:
            heappush(hashmap[idx], score)
        else:
            heappushpop(hashmap[idx], score)

    res = []
    for idx in sorted(hashmap.keys()):
        res.append([idx, sum(hashmap[idx]) // 5])
    return res


if __name__ == "__main__":
    items = [
        [1, 91],
        [1, 92],
        [2, 93],
        [2, 97],
        [1, 60],
        [2, 77],
        [1, 65],
        [1, 87],
        [1, 100],
        [2, 100],
        [2, 76],
    ]
    assert highFive(items) == [[1, 87], [2, 88]]
