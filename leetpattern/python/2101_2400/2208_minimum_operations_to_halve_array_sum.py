import heapq
from typing import List


def halveArray(nums: List[int]) -> int:
    if not nums:
        return 0

    res = 0
    cur_sum = sum(nums)
    target = cur_sum / 2

    max_heap = [-num for num in nums]  # max heap
    heapq.heapify(max_heap)

    while cur_sum > target:
        mx = -heapq.heappop(max_heap)
        new = mx / 2
        heapq.heappush(max_heap, -new)
        cur_sum -= new
        res += 1

    return res


if __name__ == "__main__":
    assert halveArray([5, 19, 8, 1]) == 3
    assert halveArray([3, 8, 20]) == 3
