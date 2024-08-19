from typing import List


# 1. Prefix Sum
def subarraySum(nums: List[int], k: int) -> int:
    prefix_sums = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        if (current_sum - k) in prefix_sums:
            count += prefix_sums[current_sum - k]

        if current_sum in prefix_sums:
            prefix_sums[current_sum] += 1
        else:
            prefix_sums[current_sum] = 1

    return count


# 2. Optimized Prefix Sum
def subarraySumOptimized(nums: List[int], k: int) -> int:
    prefix_sum = 0
    count = 0
    prefix_sums = {0: 1}

    for num in nums:
        prefix_sum += num
        count += prefix_sums.get(prefix_sum - k, 0)
        prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1

    return count


nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))  # 2
print(subarraySumOptimized(nums, k))  # 2
