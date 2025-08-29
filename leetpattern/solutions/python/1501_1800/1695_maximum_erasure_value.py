from typing import List


# Sliding Window Variable Size
def maximumUniqueSubarray(nums: List[int]) -> int:
    n = len(nums)
    left = 0
    cur, res = 0, 0
    sub = set()

    for right in range(n):
        while left < right and nums[right] in sub:
            sub.remove(nums[left])
            cur -= nums[left]
            left += 1

        sub.add(nums[right])
        cur += nums[right]
        res = max(res, cur)

    return res


nums = [4, 2, 4, 5, 6]
print(maximumUniqueSubarray(nums))  # 17
