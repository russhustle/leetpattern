from typing import List


def findSubsequences(nums: List[int]) -> List[List[int]]:
    path, result = [], []

    def backtracking(startIndex):
        if len(path) > 1:
            result.append(path[:])

        used = set()
        for i in range(startIndex, len(nums)):

            if (path and nums[i] < path[-1]) or nums[i] in used:
                continue

            used.add(nums[i])
            path.append(nums[i])
            backtracking(i + 1)
            path.pop()

    backtracking(0)

    return result


print(findSubsequences([4, 6, 7, 7]))
# [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]
