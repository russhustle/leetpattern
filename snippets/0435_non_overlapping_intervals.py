from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    if len(intervals) <= 1:
        return 0

    intervals.sort(key=lambda x: x[0])
    result = 0

    for i in range(1, len(intervals)):
        if intervals[i][0] >= intervals[i - 1][1]:
            continue
        else:
            result += 1
            intervals[i][1] = min(intervals[i][1], intervals[i - 1][1])

    return result


print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # 1
