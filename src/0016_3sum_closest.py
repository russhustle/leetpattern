from typing import List


# Left Right Pointers
def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    res = 0
    minDiff = float("inf")

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total > target:
                if total - target < minDiff:
                    minDiff = total - target
                    res = total
                right -= 1

            elif total < target:
                if target - total < minDiff:
                    minDiff = target - total
                    res = total
                left += 1

            else:
                return total

    return res

nums = [-1,2,1,-4]
target = 1
assert threeSumClosest(nums, target) == 2