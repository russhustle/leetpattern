from typing import List


# Backtracking
def partition(s: str) -> List[List[str]]:
    res = []
    n = len(s)

    def backtrack(idx, path):
        if idx == n:
            res.append(path[:])
            return None

        for j in range(idx, n):
            cur = s[idx : j + 1]
            if cur == cur[::-1]:
                path.append(cur)
                backtrack(j + 1, path)
                path.pop()

    backtrack(0, [])

    return res


print(partition("aab"))  # [['a', 'a', 'b'], ['aa', 'b']]
