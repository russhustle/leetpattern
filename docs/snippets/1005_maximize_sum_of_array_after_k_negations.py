from heapq import heapify, heapreplace
from typing import List


# Greedy
def largestSumAfterKNegationsGreedy(nums: List[int], k: int) -> int:
    nums.sort(key=abs, reverse=True)

    for i in range(len(nums)):
        if nums[i] < 0 and k > 0:
            nums[i] *= -1
            k -= 1

    if k % 2:
        nums[-1] *= -1

    return sum(nums)


# Heap
def largestSumAfterKNegationsHeap(nums: List[int], k: int) -> int:
    heapify(nums)

    while k and nums[0] < 0:
        heapreplace(nums, -nums[0])
        k -= 1

    if k % 2:
        heapreplace(nums, -nums[0])

    return sum(nums)


print(largestSumAfterKNegationsGreedy([4, 2, 3], 1))  # 5
print(largestSumAfterKNegationsHeap([4, 2, 3], 1))
