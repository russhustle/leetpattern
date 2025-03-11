import heapq
from typing import List


# Brute Force
def getFinalStateBF(nums: List[int], k: int, multiplier: int) -> List[int]:
    for _ in range(k):
        minNum = min(nums)
        idx = nums.index(minNum)
        nums[idx] *= multiplier

    return nums


# Heap
def getFinalStateHeap(nums: List[int], k: int, multiplier: int) -> List[int]:
    minHeap = []
    for idx, num in enumerate(nums):
        heapq.heappush(minHeap, (num, idx))

    for _ in range(k):
        num, idx = heapq.heappop(minHeap)
        nums[idx] = num * multiplier
        heapq.heappush(minHeap, (nums[idx], idx))

    return nums


k = 5
multiplier = 2
print(getFinalStateBF([2, 1, 3, 5, 6], k, multiplier))  # [8, 4, 6, 5, 6]
print(getFinalStateHeap([2, 1, 3, 5, 6], k, multiplier))  # [8, 4, 6, 5, 6]
