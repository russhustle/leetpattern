from typing import List


# 1.Brute Force
def containsDuplicateBF(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False


# 2. Sort
def containsDuplicateSort(nums: List[int]) -> bool:
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    return False


# 3.Set
def containsDuplicateSet(nums: List[int]) -> bool:
    seen = set()

    for i in nums:
        if i in seen:
            return True
        seen.add(i)

    return False


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# | Brute Force |    O(n^2)       |    O(1)      |
# |     Sort    |    O(n log n)   |    O(1)      |
# |     Set     |    O(n)         |    O(n)      |
# |-------------|-----------------|--------------|

print(containsDuplicateBF([1, 2, 3, 1]))  # True
print(containsDuplicateSort([1, 2, 3, 1]))  # True
print(containsDuplicateSet([1, 2, 3, 1]))  # True
