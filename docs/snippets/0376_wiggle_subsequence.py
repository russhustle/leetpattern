from typing import List


# DP
def wiggleMaxLengthDP(nums: List[int]) -> int:
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


# Greedy
def wiggleMaxLengthGreedy(nums: List[int]) -> int:
    if len(nums) < 2:
        return len(nums)

    prev_diff = nums[1] - nums[0]
    count = 2 if prev_diff != 0 else 1

    for i in range(2, len(nums)):
        diff = nums[i] - nums[i - 1]
        if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
            count += 1
            prev_diff = diff

    return count


nums = [1, 7, 4, 9, 2, 5]
print(wiggleMaxLengthDP(nums))  # 6
print(wiggleMaxLengthGreedy(nums))  # 6
