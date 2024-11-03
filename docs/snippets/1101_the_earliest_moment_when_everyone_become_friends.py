from typing import List


# Union Find
def earliestAcq(logs: List[List[int]], n: int) -> int:
    logs.sort()
    par = {i: i for i in range(n)}

    def find(n):
        p = par[n]
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p

    for time, a, b in logs:
        pa, pb = find(a), find(b)
        if pa != pb:
            par[pa] = pb
            n -= 1
        if n == 1:
            return time
    return -1


logs = [[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]]
n = 4
print(earliestAcq(logs, n))  # 3
