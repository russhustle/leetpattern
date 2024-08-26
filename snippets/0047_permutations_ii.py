from typing import List


def permuteUnique(nums: List[int]) -> List[List[int]]:
    nums.sort()
    path, result = [], []
    used = [False for _ in range(len(nums))]

    def backtracking():
        if len(path) == len(nums):
            result.append(path[:])

        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            path.append(nums[i])
            backtracking()
            path.pop()
            used[i] = False

    backtracking()

    return result


print(permuteUnique([1, 1, 2]))
# [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
