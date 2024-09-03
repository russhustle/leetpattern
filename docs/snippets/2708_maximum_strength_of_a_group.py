from typing import List


# DP
def maxStrength(nums: List[int]) -> int:
    if not nums:
        return 0

    cur_min, cur_max = nums[0], nums[0]

    for i, num in enumerate(nums):
        if i == 0:
            continue

        temp_min = min(cur_min, num, num * cur_min, num * cur_max)
        temp_max = max(cur_max, num, num * cur_min, num * cur_max)
        cur_min, cur_max = temp_min, temp_max

    return cur_max


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |  DP        |  O(N)  |  O(1)   |
# |------------|--------|---------|


nums = [3, -1, -5, 2, 5, -9]
print(maxStrength(nums))  # 1350
