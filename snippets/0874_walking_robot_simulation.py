from typing import List


# Simulation
def robotSim(commands: List[int], obstacles: List[List[int]]) -> int:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    obstacles_set = set(map(tuple, obstacles))

    x, y, d = 0, 0, 0
    max_distance = 0

    for command in commands:
        if command == -2:  # Turn left
            d = (d - 1) % 4
        elif command == -1:  # Turn right
            d = (d + 1) % 4
        else:
            dx, dy = directions[d]
            for _ in range(command):
                if (x + dx, y + dy) not in obstacles_set:
                    x += dx
                    y += dy
                    max_distance = max(max_distance, x**2 + y**2)
                else:
                    break

    return max_distance


commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
print(robotSim(commands, obstacles))  # 65
