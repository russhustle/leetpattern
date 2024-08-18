from typing import List


def wiggleMaxLength(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    if len(nums) <= 1:
        return len(nums)

    up = [0 for _ in range(len(nums))]
    down = [0 for _ in range(len(nums))]

    up[0], down[0] = 1, 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up[i] = down[i - 1] + 1
            down[i] = down[i - 1]
        elif nums[i] < nums[i - 1]:
            down[i] = up[i - 1] + 1
            up[i] = up[i - 1]
        else:
            up[i] = up[i - 1]
            down[i] = down[i - 1]

    return max(up[-1], down[-1])


nums = [1, 7, 4, 9, 2, 5]
print(wiggleMaxLength(nums))  # 6
