from typing import List


# Prefix Sum
def numberOfSubarrays(nums: List[int], k: int) -> int:
    count = 0
    odd_counts = {0: 1}  # odd_count -> count
    odd_count = 0

    for num in nums:
        if num % 2 == 1:
            odd_count += 1
        if odd_count - k in odd_counts:
            count += odd_counts[odd_count - k]
        if odd_count in odd_counts:
            odd_counts[odd_count] += 1
        else:
            odd_counts[odd_count] = 1

    return count


nums = [1, 1, 2, 1, 1]
k = 3
print(numberOfSubarrays(nums, k))  # 2
