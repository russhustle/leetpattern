from collections import deque
from typing import List


# BFS
def shortestPathAllKeys(grid: List[str]) -> int:
    m, n = len(grid), len(grid[0])
    q = deque()
    visited = set()
    total = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for r in range(m):
        for c in range(n):
            if grid[r][c] == "@":
                q.append((r, c, 0, 0))
                visited.add((r, c, 0))
            if grid[r][c].islower():
                total += 1

    while q:
        r, c, keys, steps = q.popleft()

        if keys == (1 << total) - 1:
            return steps

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n:
                cell = grid[nr][nc]

                if cell == "#":
                    continue

                new_keys = keys
                if cell.islower():
                    new_keys |= 1 << (ord(cell) - ord("a"))

                if cell.isupper() and not (
                    keys & (1 << (ord(cell) - ord("A")))
                ):
                    continue

                if (nr, nc, new_keys) not in visited:
                    visited.add((nr, nc, new_keys))
                    q.append((nr, nc, new_keys, steps + 1))

    return -1


grid = ["@.a..", "###.#", "b.A.B"]
print(shortestPathAllKeys(grid))  # 8
