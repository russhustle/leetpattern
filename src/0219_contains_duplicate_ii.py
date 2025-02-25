from typing import List


# Hash
def containsNearbyDuplicateHash(nums: List[int], k: int) -> bool:
    hashmap = {}  # num: last index

    for idx, num in enumerate(nums):
        if num in hashmap:
            if idx - hashmap[num] <= k:
                return True

        hashmap[num] = idx

    return False


# Sliding window - Fixed
def containsNearbyDuplicateWindow(nums: List[int], k: int) -> bool:
    window = set()
    left = 0

    for right in range(len(nums)):
        if right - left > k:
            window.remove(nums[left])
            left += 1
        if nums[right] in window:
            return True
        window.add(nums[right])

    return False


nums = [1, 2, 3, 1]
k = 3
print(containsNearbyDuplicateHash(nums, k))  # True
print(containsNearbyDuplicateWindow(nums, k))  # True
