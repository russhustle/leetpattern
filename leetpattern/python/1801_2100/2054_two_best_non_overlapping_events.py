from bisect import bisect_left
from typing import List


class maxTwoEvents:
    @staticmethod
    def binary_search(events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        stack = [(0, 0)]
        res = 0

        for start, end, val in events:
            i = bisect_left(stack, (start,)) - 1
            res = max(res, stack[i][1] + val)

            if val > stack[-1][1]:
                stack.append((end, val))

        return res


if __name__ == "__main__":
    events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]
    assert maxTwoEvents.binary_search(events) == 4
