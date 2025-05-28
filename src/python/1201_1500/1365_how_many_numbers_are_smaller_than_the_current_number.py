"""
-   For each number in the array, return how many numbers are smaller than it.
"""

from typing import List


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    sortedNums = sorted(nums)

    hashmap = dict()

    for i, num in enumerate(sortedNums):
        if num not in hashmap:
            hashmap[num] = i

    result = []
    for i in range(len(sortedNums)):
        result.append(hashmap[nums[i]])

    return result


nums = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums))  # [4, 0, 1, 1, 3]
