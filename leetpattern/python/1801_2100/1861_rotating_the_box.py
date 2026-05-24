from copy import deepcopy
from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """Gravity then rotate: O(m*n) time, O(m*n) space.
        Simulate gravity rightward by tracking the next empty
        slot from the right, then rotate 90° clockwise.
        """
        for row in box:
            empty = len(row) - 1
            for i in range(len(row) - 1, -1, -1):
                if row[i] == "*":
                    empty = i - 1
                elif row[i] == "#":
                    row[i] = "."
                    row[empty] = "#"
                    empty -= 1

        m, n = len(box), len(box[0])
        return [[box[m - 1 - j][i] for j in range(m)] for i in range(n)]


def test_rotate_the_box():
    s = Solution()
    b1 = [["#", ".", "#"]]
    assert s.rotateTheBox(deepcopy(b1)) == [
        ["."],
        ["#"],
        ["#"],
    ]
    b2 = [["#", ".", "*", "."], ["#", "#", "*", "."]]
    assert s.rotateTheBox(deepcopy(b2)) == [
        ["#", "."],
        ["#", "#"],
        ["*", "*"],
        [".", "."],
    ]
    b3 = [
        ["#", "#", "*", ".", "*", "."],
        ["#", "#", "#", "*", ".", "."],
        ["#", "#", "#", ".", "#", "."],
    ]
    assert s.rotateTheBox(deepcopy(b3)) == [
        [".", "#", "#"],
        [".", "#", "#"],
        ["#", "#", "*"],
        ["#", "*", "."],
        ["#", ".", "*"],
        ["#", ".", "."],
    ]
