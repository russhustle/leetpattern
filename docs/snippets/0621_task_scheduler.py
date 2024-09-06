import heapq
from collections import Counter, deque
from typing import List


# Heap
def leastInterval1(tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    heap = [-c for c in count.values()]
    heapq.heapify(heap)

    time = 0

    q = deque()

    while heap or q:
        time += 1

        if heap:
            cnt = 1 + heapq.heappop(heap)
            if cnt:
                q.append((cnt, time + n))

        if q and q[0][1] == time:
            heapq.heappush(heap, q.popleft()[0])

    return time


def leastInterval2(tasks: List[str], n: int) -> int:
    freq = Counter(tasks)

    maxExec = max(freq.values())
    maxCount = sum(1 for v in freq.values() if v == maxExec)

    return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(leastInterval1(tasks, n))  # 8
print(leastInterval2(tasks, n))  # 8
