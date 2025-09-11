"""
- Given an array of meeting time `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.
"""

import heapq
from typing import List


# Heap
def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    minHeap = [intervals[0][1]]

    for i in range(1, len(intervals)):
        if intervals[i][0] >= minHeap[0]:
            heapq.heappop(minHeap)
        heapq.heappush(minHeap, intervals[i][1])

    return len(minHeap)


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert minMeetingRooms(intervals) == 2
