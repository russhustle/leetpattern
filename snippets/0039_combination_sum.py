from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    path = []

    def backtracking(total, start):
        if total > target:
            return None
        if total == target:
            result.append(path[:])
            return None

        for i in range(start, len(candidates)):
            total += candidates[i]
            path.append(candidates[i])

            backtracking(total, i)

            total -= candidates[i]
            path.pop()

    backtracking(0, 0)
    return result


print(combinationSum([2, 3, 6, 7], 7))  # [[2, 2, 3], [7]]
