from typing import List


def longestCycle(edges: List[int]) -> int:
    n = len(edges)
    res = -1
    cur = 1
    vis = [0 for _ in range(n)]

    for i in range(n):
        start = cur
        while i != -1 and vis[i] == 0:
            vis[i] = cur
            cur += 1
            i = edges[i]
        if i != -1 and vis[i] >= start:
            res = max(res, cur - vis[i])

    return res


if __name__ == "__main__":
    edges = [3, 3, 4, 2, 3]
    print(longestCycle(edges))  # 3
