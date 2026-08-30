from heapq import heappop, heappush
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """Min Heap: O(n log n) time, O(n) space.
        Track active meeting end times; the peak heap size is the minimum
        number of rooms required.

        Timeline (letters mark meeting endpoints):
            |                          G----H
            |                     E-----------F
            |   C--------------D
            | A----------B
            +----------------------------------

        Heap simulation (earliest end first):
            A: push B                   -> [B]
            C: C < B, push D            -> [B, D]
            E: pop B and D, push F      -> [F]
            G: G < F, push H            -> [H, F]

        The peak heap size is 2, so two rooms are required.
        """
        ends = []
        res = 0

        for start, end in sorted(intervals):
            while ends and ends[0] <= start:
                heappop(ends)
            heappush(ends, end)
            res = max(res, len(ends))

        return res


def test_min_meeting_rooms():
    s = Solution()
    for fn in (s.minMeetingRooms,):
        assert fn([]) == 0
        assert fn([[0, 30], [5, 10], [15, 20]]) == 2
        assert fn([[7, 10], [2, 4]]) == 1
        assert fn([[1, 5], [5, 10], [5, 8]]) == 2
