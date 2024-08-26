from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    result, path = [], []
    candidates.sort()

    def backtracking(total, start):
        if total == target:
            result.append(path[:])
            return None

        for i in range(start, len(candidates)):

            if i > start and candidates[i] == candidates[i - 1]:
                continue

            if total + candidates[i] > target:
                break

            total += candidates[i]
            path.append(candidates[i])
            backtracking(total, i + 1)
            total -= candidates[i]
            path.pop()

    backtracking(0, 0)

    return result


print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
# [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
