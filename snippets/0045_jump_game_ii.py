from typing import List


def jump(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0

    cover = 0
    count = 0
    i = 0

    while cover >= 0:
        for i in range(i, cover + 1):
            cover = max(cover, nums[i] + i)
            if cover >= len(nums) - 1:
                return count + 1
        count += 1

    return count


print(jump([2, 3, 1, 1, 4]))  # 2
