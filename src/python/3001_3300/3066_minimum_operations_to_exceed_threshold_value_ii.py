from heapq import heapify, heappop, heappush
from typing import List


# Heap
def minOperations(nums: List[int], k: int) -> int:
    heapify(nums)
    res = 0

    while nums[0] < k:
        x = heappop(nums)
        y = heappop(nums)
        heappush(nums, x * 2 + y)
        res += 1

    return res


if __name__ == "__main__":
    assert minOperations([2, 11, 10, 1, 3], 10) == 2
    assert minOperations([1, 1, 2, 4, 9], 20) == 4
