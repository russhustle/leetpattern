---
comments: True
---

# Simulation

## Table of Contents

- [x] [874. Walking Robot Simulation](https://leetcode.cn/problems/walking-robot-simulation/) (Medium)

## 874. Walking Robot Simulation

-   [LeetCode](https://leetcode.com/problems/walking-robot-simulation/) | [LeetCode CH](https://leetcode.cn/problems/walking-robot-simulation/) (Medium)

-   Tags: array, hash table, simulation
```python title="874. Walking Robot Simulation - Python Solution"
from typing import List


# Simulation
def robotSim(commands: List[int], obstacles: List[List[int]]) -> int:
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    obstacles_set = set(map(tuple, obstacles))

    x, y, d = 0, 0, 0
    res = 0

    for command in commands:
        if command == -2:  # Turn left
            d = (d - 1) % 4
        elif command == -1:  # Turn right
            d = (d + 1) % 4
        else:
            dx, dy = dirs[d]
            for _ in range(command):
                if (x + dx, y + dy) not in obstacles_set:
                    x += dx
                    y += dy
                    res = max(res, x**2 + y**2)
                else:
                    break

    return res


commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
print(robotSim(commands, obstacles))  # 65

```

