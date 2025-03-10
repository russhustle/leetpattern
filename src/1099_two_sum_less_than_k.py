from typing import List


# Left Right Pointers
def twoSumLessThanK(nums: List[int], k: int) -> int:
    nums.sort()
    left, right = 0, len(nums) - 1
    res = float("-inf")

    while left < right:
        total = nums[left] + nums[right]

        if total >= k:
            right -= 1
        else:
            res = max(res, total)
            left += 1

    return res if res != float("-inf") else -1


nums = [34, 23, 1, 24, 75, 33, 54, 8]
k = 60
print(twoSumLessThanK(nums, k))  # 58
