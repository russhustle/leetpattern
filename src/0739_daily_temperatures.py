from typing import List


# Monotonic Stack
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0 for _ in range(len(temperatures))]
    stack = []  # [temp, index]

    for idx, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            _, last_index = stack.pop()
            res[last_index] = idx - last_index

        stack.append([temp, idx])

    return res


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1, 1, 4, 2, 1, 1, 0, 0]
