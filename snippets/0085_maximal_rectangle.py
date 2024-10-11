from typing import List


# Monotonic Stack
def maximalRectangle(matrix: List[List[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix[0])
    heights = [0] * (n + 1)
    max_area = 0

    for row in matrix:
        for i in range(n):
            if row[i] == "1":
                heights[i] += 1
            else:
                heights[i] = 0

        stack = [-1]
        for i in range(n + 1):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

    return max_area


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(maximalRectangle(matrix))  # 6
