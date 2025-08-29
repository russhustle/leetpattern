from typing import List


# Sort
def countWays(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    count = 0

    if nums[0] > 0:
        count += 1

    for x in range(1, n):
        if nums[x - 1] < x < nums[x]:
            count += 1

    if nums[n - 1] < n:
        count += 1

    return count


nums = [6, 0, 3, 3, 6, 7, 2, 7]
print(countWays(nums))  # 3
