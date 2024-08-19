import heapq
from collections import Counter
from typing import List


# Counter
def topKFrequent1(nums: List[int], k: int) -> List[int]:
    heap = []  # min heap

    for val, count in Counter(nums).items():
        if len(heap) < k:
            heapq.heappush(heap, (count, val))
        else:
            heapq.heappushpop(heap, (count, val))

    return [i for (_, i) in heap]


# Dictionary
def topKFrequent2(nums: List[int], k: int) -> List[int]:
    heap = []  # min heap
    counts = dict()

    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for val, count in counts.items():
        if len(heap) < k:
            heapq.heappush(heap, (count, val))
        else:
            heapq.heappushpop(heap, (count, val))

    return [i for (_, i) in heap]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent1(nums, k))  # [2, 1]
print(topKFrequent2(nums, k))  # [2, 1]
