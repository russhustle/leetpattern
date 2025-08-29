"""
- Return the indices of the two numbers such that they add up to a specific target.
- Approach: Use a hashmap to store the indices of the numbers.
- Time Complexity: O(n)
- Space Complexity: O(n)
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}  # val: idx

    for idx, val in enumerate(nums):
        if (target - val) in hashmap:
            return [hashmap[target - val], idx]

        hashmap[val] = idx


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    assert twoSum(nums, target) == [0, 1]
