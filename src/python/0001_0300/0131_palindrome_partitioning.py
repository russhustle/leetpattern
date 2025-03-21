from typing import List


# Backtracking
def partition(s: str) -> List[List[str]]:
    n = len(s)
    res, path = [], []

    def dfs(start):
        if start == n:
            res.append(path.copy())
            return

        for end in range(start, n):
            cur = s[start : end + 1]
            if cur == cur[::-1]:
                path.append(cur)
                dfs(end + 1)
                path.pop()

    dfs(0)

    return res


if __name__ == "__main__":
    print(partition("aab"))
    # [['a', 'a', 'b'], ['aa', 'b']]
