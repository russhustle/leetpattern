import heapq
from collections import Counter, deque
from typing import List


def least_interval_heap(tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    heap = [-c for c in count.values()]
    heapq.heapify(heap)

    res = 0

    q = deque()

    while heap or q:
        res += 1

        if heap:
            cnt = 1 + heapq.heappop(heap)
            if cnt:
                q.append((cnt, res + n))

        if q and q[0][1] == res:
            heapq.heappush(heap, q.popleft()[0])

    return res


def least_interval_math(tasks: List[str], n: int) -> int:
    freq = Counter(tasks)

    max_exec = max(freq.values())
    max_count = sum(1 for v in freq.values() if v == max_exec)

    return max((max_exec - 1) * (n + 1) + max_count, len(tasks))


def test_least_interval_heap():
    assert least_interval_heap(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert least_interval_heap(["A"], 0) == 1
    assert least_interval_heap(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert least_interval_heap(["A", "A", "A", "A", "B", "B", "B", "C", "C"], 2) == 10


def test_least_interval_math():
    assert least_interval_math(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert least_interval_math(["A"], 0) == 1
    assert least_interval_math(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert least_interval_math(["A", "A", "A", "A", "B", "B", "B", "C", "C"], 2) == 10
