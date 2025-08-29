from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    n = len(candidates)
    res, path = [], []

    def dfs(total, start):
        if total > target:
            return
        if total == target:
            res.append(path.copy())
            return

        for i in range(start, n):
            total += candidates[i]
            path.append(candidates[i])
            dfs(total, i)
            total -= candidates[i]
            path.pop()

    dfs(0, 0)

    return res


if __name__ == "__main__":
    print(combinationSum([2, 3, 5], 8))
    # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print(combinationSum([2, 3, 6, 7], 7))
    # [[2, 2, 3], [7]]
