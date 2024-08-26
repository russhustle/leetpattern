from typing import List


# 1. Prefix Sum
def subarraySum(nums: List[int], k: int) -> int:
    prefix_sums = {0: 1}
    currentSum = 0
    count = 0

    for num in nums:
        currentSum += num
        if (currentSum - k) in prefix_sums:
            count += prefix_sums[currentSum - k]

        if currentSum in prefix_sums:
            prefix_sums[currentSum] += 1
        else:
            prefix_sums[currentSum] = 1

    return count


# 2. Optimized Prefix Sum
def subarraySumOptimized(nums: List[int], k: int) -> int:
    prefixSum = 0
    count = 0
    prefix_sums = {0: 1}

    for num in nums:
        prefixSum += num
        count += prefix_sums.get(prefixSum - k, 0)
        prefix_sums[prefixSum] = prefix_sums.get(prefixSum, 0) + 1

    return count


nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))  # 2
print(subarraySumOptimized(nums, k))  # 2
