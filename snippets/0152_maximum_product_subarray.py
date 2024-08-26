from typing import List


def maxProduct(nums: List[int]) -> int:
    n = len(nums)
    dp_max = [0 for _ in range(n)]
    dp_min = [0 for _ in range(n)]

    dp_max[0] = nums[0]
    dp_min[0] = nums[0]
    max_product = nums[0]

    for i in range(1, n):
        dp_max[i] = max(
            nums[i],
            nums[i] * dp_max[i - 1],
            nums[i] * dp_min[i - 1],
        )
        dp_min[i] = min(
            nums[i],
            nums[i] * dp_max[i - 1],
            nums[i] * dp_min[i - 1],
        )

        max_product = max(max_product, dp_max[i])

    return max_product


nums = [2, 3, -2, 4]
print(maxProduct(nums))  # 6
