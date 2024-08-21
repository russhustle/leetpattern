from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = dict()

    for idx, val in enumerate(nums):
        if (target - val) in hashmap:
            return [hashmap[target - val], idx]
        hashmap[val] = idx


nums = [2, 7, 11, 15]
target = 18
print(twoSum(nums, target))  # [1, 2]
