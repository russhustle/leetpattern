from typing import List


def findDuplicate(nums: List[int]) -> int:

    fast, slow = nums[0], nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


# Time complexity: O(n)
# Space complexity: O(1)

nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums)) # 2
