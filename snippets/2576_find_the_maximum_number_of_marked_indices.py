from typing import List


# Fast Slow Pointers
def maxNumOfMarkedIndices(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    slow, fast = 0, n // 2
    count = 0

    while slow < n // 2 and fast < n:
        if nums[fast] >= 2 * nums[slow]:
            count += 2
            slow += 1
        fast += 1

    return count


nums = [3, 5, 2, 4]
print(maxNumOfMarkedIndices(nums))  # 2
