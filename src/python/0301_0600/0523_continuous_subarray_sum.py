from typing import List


# Prefix Sum
def checkSubarraySum(nums: List[int], k: int) -> bool:
    if k == 0:
        for i in range(1, len(nums)):
            if nums[i - 1] == 0 and nums[i] == 0:
                return True

    prefix_sum = 0
    mod_dict = {0: -1}

    for i, num in enumerate(nums):
        prefix_sum += num
        mod = prefix_sum % k

        if mod in mod_dict:
            if i - mod_dict[mod] > 1:
                return True
        else:
            mod_dict[mod] = i

    return False


nums = [23, 2, 4, 6, 7]
k = 6
print(checkSubarraySum(nums, k))  # True
