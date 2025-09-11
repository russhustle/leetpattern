import heapq
from collections import Counter
from typing import List


# Heap + Counter
def topKFrequent(nums: List[int], k: int) -> List[int]:
    minHeap = []

    for val, freq in Counter(nums).items():
        if len(minHeap) < k:
            heapq.heappush(minHeap, (freq, val))
        else:
            heapq.heappushpop(minHeap, (freq, val))

    return [i for _, i in minHeap]


# Counter (Most Common)
def topKFrequentCounter(nums: List[int], k: int) -> List[int]:
    commons = Counter(nums).most_common(k)
    return [i for i, _ in commons]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))  # [1, 2]
print(topKFrequentCounter(nums, k))  # [1, 2]
