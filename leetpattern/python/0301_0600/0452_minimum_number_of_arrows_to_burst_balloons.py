from typing import List


class findMinArrowShots:
    @staticmethod
    def interval_end(points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return n

        points.sort(key=lambda x: x[1])

        res = 1
        cur = points[0][1]

        for i, j in points[1:]:
            if i > cur:
                res += 1
                cur = j

        return res

    @staticmethod
    def interval_start(points: List[List[int]]) -> int:
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


if __name__ == "__main__":
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    assert findMinArrowShots.interval_end(points) == 2
    assert findMinArrowShots.interval_start(points) == 2
