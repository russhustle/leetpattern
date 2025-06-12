from typing import List


# Enumeate Right Maintain Left
def maxScoreSightseeingPair(values: List[int]) -> int:
    max_i = values[0] + 0
    res = 0

    for j in range(1, len(values)):
        res = max(res, max_i + values[j] - j)
        max_i = max(max_i, values[j] + j)

    return res


if __name__ == "__main__":
    assert maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11
    assert maxScoreSightseeingPair([1, 2]) == 2
    assert maxScoreSightseeingPair([1, 3, 5]) == 7
    assert maxScoreSightseeingPair([1, 2, 3, 4, 5]) == 8
