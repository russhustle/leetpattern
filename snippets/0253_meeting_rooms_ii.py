import heapq
from typing import List


# Heap
def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    heap = [intervals[0][1]]

    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])

    return len(heap)


intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals))  # 2
