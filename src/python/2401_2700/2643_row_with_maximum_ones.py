from typing import List


def rowAndMaximumOnes(mat: List[List[int]]) -> List[int]:
    """Return the index of the row with the maximum number of ones."""
    res = [0, 0]
    for i, row in enumerate(mat):
        cnt = sum(row)
        if cnt > res[1]:
            res[0], res[1] = i, cnt

    return res


if __name__ == "__main__":
    mat = [[0, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
    print(rowAndMaximumOnes(mat))  # [2, 4]
