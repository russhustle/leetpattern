from typing import List


# Prefix Sum
def getSumAbsoluteDifferences(nums: List[int]) -> List[int]:
    n = len(nums)
    totalSum = sum(nums)
    prefixSum = 0
    res = [0 for _ in range(n)]

    for i in range(n):
        leftSum = prefixSum
        rightSum = totalSum - prefixSum - nums[i]

        leftCount = i
        rightCount = n - i - 1

        res[i] = (nums[i] * leftCount - leftSum) + (rightSum - nums[i] * rightCount)
        prefixSum += nums[i]

    return res


nums = [1, 4, 6, 8, 10]
print(getSumAbsoluteDifferences(nums))  # [24, 15, 13, 15, 21]
