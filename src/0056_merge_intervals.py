from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(intervals[i][1], result[-1][1])
        else:
            result.append(intervals[i])

    return result


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# [[1, 6], [8, 10], [15, 18]]
