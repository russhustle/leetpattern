import heapq
from collections import Counter
from typing import List


# 1. Heap + Counter
def topKFrequent1(nums: List[int], k: int) -> List[int]:
    minHeap = []

    for val, count in Counter(nums).items():
        if len(minHeap) < k:
            heapq.heappush(minHeap, (count, val))
        else:
            heapq.heappushpop(minHeap, (count, val))

    return [i for (_, i) in minHeap]


# 2. Heap + Dict
def topKFrequent2(nums: List[int], k: int) -> List[int]:
    minHeap = []

    counts = dict()
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for val, count in counts.items():
        if len(minHeap) < k:
            heapq.heappush(minHeap, (count, val))
        else:
            heapq.heappushpop(minHeap, (count, val))

    return [i for (_, i) in minHeap]


# 3. OrderedDict
def topKFrequent3(nums: List[int], k: int) -> List[int]:
    return [i for i, _ in Counter(nums).most_common(k)]


# |-------------|-------------|--------------|
# |   Approach  |    Time     |    Space     |
# |-------------|-------------|--------------|
# |   Heap      |    O(n)     |    O(n)      |
# |-------------|-------------|--------------|


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent1(nums, k))  # [2, 1]
print(topKFrequent2(nums, k))  # [2, 1]
print(topKFrequent3(nums, k))  # [1, 2]
