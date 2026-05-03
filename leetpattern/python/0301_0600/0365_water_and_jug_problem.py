from collections import deque


class canMeasureWater:
    def bfs(self, x: int, y: int, target: int) -> bool:
        if target == 0:
            return False
        if x + y < target:
            return False

        visited = set()
        q = deque([(0, 0)])
        visited.add((0, 0))

        while q:
            j1, j2 = q.popleft()
            if j1 + j2 == target or j1 == target or j2 == target:
                return True

            next_states = [
                (x, j2),  # fill jug 1
                (j1, y),  # fill jug 2
                (0, j2),  # empty jug 1
                (j1, 0),  # empty jug 2
                # pour from jug 1 to jug 2
                (j1 - min(j1, y - j2), j2 + min(j1, y - j2)),
                # pour from jug 2 to jug 1
                (j1 + min(j2, x - j1), j2 - min(j2, x - j1)),
            ]

            for state in next_states:
                if state not in visited:
                    q.append(state)
                    visited.add(state)

        return False
