from typing import List


# Sliding Window Fixed Size
def getAverages(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    res = [-1 for _ in range(n)]
    size = 2 * k + 1

    if size > n:
        return res
    if k == 0:
        return nums

    cur = 0
    for idx, num in enumerate(nums):
        cur += num

        if idx < 2 * k:
            continue

        res[idx - k] = cur // size
        cur -= nums[idx - 2 * k]

    return res


nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
k = 3
print(getAverages(nums, k))
# [-1, -1, -1, 5, 4, 4, -1, -1, -1]
