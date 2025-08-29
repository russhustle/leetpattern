from heapq import heapify, heapreplace
from math import inf
from typing import List


# Heap
def smallestRange(nums: List[List[int]]) -> List[int]:
    heap = [(arr[0], i, 0) for i, arr in enumerate(nums)]
    heapify(heap)

    res_l = heap[0][0]
    res_r = right = max(arr[0] for arr in nums)

    while heap[0][2] + 1 < len(nums[heap[0][1]]):
        _, i, j = heap[0]
        x = nums[i][j + 1]
        heapreplace(heap, (x, i, j + 1))
        right = max(right, x)
        left = heap[0][0]
        if right - left < res_r - res_l:
            res_l, res_r = left, right

    return [res_l, res_r]


# Sliding Window Variable Min
def smallestRangeSliding(nums: List[List[int]]) -> List[int]:
    pairs = sorted((x, i) for (i, arr) in enumerate(nums) for x in arr)
    res_l, res_r = -inf, inf
    empty = len(nums)
    cnt = [0] * empty
    left = 0

    for r, i in pairs:
        if cnt[i] == 0:
            empty -= 1
        cnt[i] += 1
        while empty == 0:
            l, i = pairs[left]
            if r - l < res_r - res_l:
                res_l, res_r = l, r
            cnt[i] -= 1
            if cnt[i] == 0:
                empty += 1
            left += 1

    return [res_l, res_r]


if __name__ == "__main__":
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    assert smallestRange(nums) == [20, 24]
    assert smallestRangeSliding(nums) == [20, 24]
