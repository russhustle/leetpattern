from typing import List


# Fast Slow Pointer
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


# | Algorithm          | TC   | SC   |
# |--------------------|------|------|
# | Fast Slow Pointer  | O(n) | O(1) |
# |--------------------|------|------|

nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))  # 2
