from typing import List


# Sliding window - Fixed
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
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
print(containsNearbyDuplicate(nums, k))  # True
