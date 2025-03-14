from typing import List


# Backtracking
def permute(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    path, res = [], []
    used = [False for _ in range(n)]

    def dfs(x: int):
        if x == n:
            res.append(path[:])
            return

        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            dfs(x + 1)
            path.pop()
            used[i] = False

    dfs(0)

    return res


print(permute([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3],
#  [2, 3, 1], [3, 1, 2], [3, 2, 1]]
