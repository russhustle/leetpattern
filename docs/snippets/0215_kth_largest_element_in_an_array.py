import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)  # min heap

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)  # pop the smallest element
            heapq.heappush(heap, num)  # push the new element

    return heap[0]


# Time complexity: O(n * log(k))
#   - O(log(k)) for heapify
#   - O(n) for iterating through the input list
# Space complexity: O(k)

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # 5
