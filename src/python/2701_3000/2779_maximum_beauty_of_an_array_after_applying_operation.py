from typing import List


# Sliding Window Variable Max
def maximumBeauty(nums: List[int], k: int) -> int:
    nums.sort()
    res, left = 0, 0

    for right, x in enumerate(nums):
        while x - nums[left] > k * 2:
            left += 1
        res = max(res, right - left + 1)

    return res


if __name__ == "__main__":
    assert maximumBeauty([4, 6, 1, 2], 2) == 3
