from typing import List


# Set
def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)  # O(n)
    longest = 0

    for n in nums:
        if (n - 1) not in numSet:  # left boundary
            length = 0

            while (n + length) in numSet:
                length += 1

            longest = max(longest, length)

    return longest


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |     Set     |      O(n)       |    O(n)      |
# |-------------|-----------------|--------------|


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))  # 4
