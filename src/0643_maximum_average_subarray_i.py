from typing import List


# Sliding Window Fixed Size
def findMaxAverage1(nums: List[int], k: int) -> float:
    maxSum = float("-inf")
    cur = 0

    for idx, num in enumerate(nums):
        cur += num

        if idx < k - 1:
            continue

        maxSum = max(maxSum, cur)
        cur -= nums[idx - k + 1]

    return maxSum / k


# Sliding Window Fixed Size
def findMaxAverage2(nums: List[int], k: int) -> float:
    n = len(nums)
    if n == 1:
        return float(nums[0])

    cur = sum(nums[:k])

    maxSum = cur
    for i in range(k, n):
        cur += nums[i] - nums[i - k]
        maxSum = max(maxSum, cur)

    return maxSum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage1(nums, k))  # 12.75
print(findMaxAverage2(nums, k))  # 12.75
