from typing import List


# Monotonic Stack
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    result = [0 for _ in range(len(temperatures))]
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            _, stackIdx = stack.pop()
            result[stackIdx] = i - stackIdx

        stack.append([t, i])

    return result


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1, 1, 4, 2, 1, 1, 0, 0]
