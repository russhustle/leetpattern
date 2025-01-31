from typing import List

import matplotlib.pyplot as plt


# Greedy - Interval
def findMinArrowShotsGreedy1(points: List[List[int]]) -> int:
    n = len(points)
    if n <= 1:
        return n

    res = 1
    points.sort(key=lambda x: x[0])

    for i in range(1, n):
        if points[i][0] > points[i - 1][1]:
            res += 1
        else:
            points[i][1] = min(points[i][1], points[i - 1][1])
    return res


# Greedy - Interval (Neetcode's version)
def findMinArrowShotsGreedy2(points: List[List[int]]) -> int:
    res = len(points)
    if res == 0:
        return 0

    points.sort()
    prev = points[0]

    for i in range(1, len(points)):
        cur = points[i]
        if cur[0] <= prev[1]:
            res -= 1
            prev = [cur[0], min(prev[1], cur[1])]
        else:
            prev = cur

    return res


# Greedy - Interval
def findMinArrowShotsGreedy3(points: List[List[int]]) -> int:
    if not points:
        return 0

    points.sort(key=lambda x: x[1])

    res = 1
    cur_end = points[0][1]

    for i in range(1, len(points)):
        if points[i][0] > cur_end:
            res += 1
            cur_end = points[i][1]

    return res


# Utility
def plot(points, i=None):
    plt.figure(figsize=(8, 4))
    for idx in range(len(points)):
        color = "b" if idx == i else "k"
        plt.plot(
            [points[idx][0], points[idx][1]],
            [idx + 1, idx + 1],
            f"{color}o-",
            label=f"Line {idx + 1}",
        )

    plt.title("Find Min Arrow Shots")
    plt.xlabel("X-axis")
    plt.xlim(0, 17)
    plt.grid(True)
    plt.savefig(f"find_min_arrow_shots_{i}.png")
    plt.show()


# |------------|-----------|---------|
# |  Approach  |  Time     |  Space  |
# |------------|-----------|---------|
# |  Greedy    |  O(NlogN) |  O(1)   |
# |------------|-----------|---------|


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(findMinArrowShotsGreedy1(points))  # 2
print(findMinArrowShotsGreedy2(points))  # 2
