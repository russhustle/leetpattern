import heapq
from typing import List


# Heap - Merge K Sorted
def kSmallestPairs(
    nums1: List[int], nums2: List[int], k: int
) -> List[List[int]]:
    if not nums1 or not nums2 or k <= 0:
        return []

    result = []
    min_heap = []

    for j in range(min(k, len(nums2))):
        heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))

    while k > 0 and min_heap:
        _, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])
        k -= 1

        if i + 1 < len(nums1):
            heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))

    return result


nums1 = [1, 2, 4, 5, 6]
nums2 = [3, 5, 7, 9]
k = 3
print(kSmallestPairs(nums1, nums2, k))
# [[1, 3], [2, 3], [1, 5]]
