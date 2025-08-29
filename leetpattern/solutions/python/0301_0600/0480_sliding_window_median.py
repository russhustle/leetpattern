import heapq
from typing import List

from sortedcontainers import SortedList


# Heap - Two Heaps
def medianSlidingWindow1(nums: List[int], k: int) -> List[float]:
    min_heap, max_heap = [], []

    for i in range(k):
        heapq.heappush(min_heap, (nums[i], i))
    for i in range(k // 2):
        n, idx = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-n, idx))

    res = [
        (
            (min_heap[0][0] - max_heap[0][0]) / 2
            if k % 2 == 0
            else min_heap[0][0] * 1.0
        )
    ]

    for i in range(k, len(nums)):
        if nums[i] < min_heap[0][0]:
            heapq.heappush(max_heap, (-nums[i], i))

            if nums[i - k] >= min_heap[0][0]:
                n, idx = heapq.heappop(max_heap)
                heapq.heappush(min_heap, (-n, idx))
        else:
            heapq.heappush(min_heap, (nums[i], i))

            if nums[i - k] <= min_heap[0][0]:
                n, idx = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-n, idx))

        while min_heap and min_heap[0][1] <= i - k:
            heapq.heappop(min_heap)
        while max_heap and max_heap[0][1] <= i - k:
            heapq.heappop(max_heap)

        res.append(
            (min_heap[0][0] - max_heap[0][0]) / 2
            if k % 2 == 0
            else min_heap[0][0] * 1.0
        )

    return res


# Sorted List
def medianSlidingWindow2(nums: List[int], k: int) -> List[float]:
    window = SortedList()
    res = []

    for i in range(len(nums)):
        window.add(nums[i])

        if len(window) == k:
            if k % 2 == 1:
                res.append(window[k // 2])
            else:
                res.append((window[k // 2 - 1] + window[k // 2]) / 2.0)

            window.remove(nums[i - k + 1])

    return res


nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
k = 3
print(medianSlidingWindow1(nums, k))
print(medianSlidingWindow2(nums, k))
