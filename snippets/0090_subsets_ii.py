from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    path, result = [], []
    nums.sort()

    def backtracking(startIndex):
        if path not in result:
            result.append(path[:])

        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            backtracking(i + 1)
            path.pop()

    backtracking(startIndex=0)

    return result


print(subsetsWithDup([1, 2, 2]))
# [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
