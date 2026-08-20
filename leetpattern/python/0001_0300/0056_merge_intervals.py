def merge(intervals: list[list[int]]) -> list[list[int]]:
    """
    Merge all overlapping intervals.

    |                    G----H
    |                  E===========F
    |     C--------D
    |  A========B
    |
    |-----------------------------------
    Draw the above to explain the process to the interviewer.
    Time complexity: O(nlogn) due to sorting.
    Space complexity: O(n) for the result list.
    """
    n = len(intervals)
    if n <= 1:
        return intervals

    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]

    for i in range(1, n):
        if intervals[i][0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])

    return res


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# [[1, 6], [8, 10], [15, 18]]
