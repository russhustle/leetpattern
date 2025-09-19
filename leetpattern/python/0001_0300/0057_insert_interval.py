from typing import List


# Interval
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    n = len(intervals)

    if n == 0:
        return [newInterval]

    if newInterval[1] < intervals[0][0]:
        return [newInterval] + intervals

    if newInterval[0] > intervals[-1][1]:
        return intervals + [newInterval]

    i = 0
    result = []

    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    while i < n:
        result.append(intervals[i])
        i += 1

    return result


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(insert(intervals, newInterval))  # [[1, 5], [6, 9]]
