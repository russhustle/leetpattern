from typing import List


# Greedy - Interval
def findMinArrowShotsGreedy1(points: List[List[int]]) -> int:
    n = len(points)
    if n == 0:
        return 0

    points.sort(key=lambda x: x[0])
    arrow = 1

    for i in range(1, n):
        if points[i][0] > points[i - 1][1]:
            arrow += 1
        else:
            points[i][1] = min(points[i][1], points[i - 1][1])

    return arrow


# Greedy - Interval
def findMinArrowShotsGreedy2(points: List[List[int]]) -> int:
    result = len(points)
    if result == 0:
        return 0

    points.sort()
    prev = points[0]

    for i in range(1, len(points)):
        cur = points[i]
        if cur[0] <= prev[1]:
            result -= 1
            prev = [cur[0], min(prev[1], cur[1])]
        else:
            prev = cur

    return result


# |------------|-----------|---------|
# |  Approach  |  Time     |  Space  |
# |------------|-----------|---------|
# |  Greedy    |  O(NlogN) |  O(1)   |
# |------------|-----------|---------|


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(findMinArrowShotsGreedy1(points))  # 2
print(findMinArrowShotsGreedy2(points))  # 2
