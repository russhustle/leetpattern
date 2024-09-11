from typing import List


# Array
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:

        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:

            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:

            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |    Naive    |      O(N)       |     O(1)     |
# |-------------|-----------------|--------------|


print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# [1, 2, 3, 6, 9, 8, 7, 4, 5]
