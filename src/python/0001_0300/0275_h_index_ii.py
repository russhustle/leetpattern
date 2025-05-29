"""
- Hint: logarithmic time -- binary search
"""

from typing import List


# Binary Search Max Answer
def hIndex(citations: List[int]) -> int:
    n = len(citations)
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2

        if citations[mid] >= n - mid:
            right = mid - 1
        else:
            left = mid + 1

    return n - left


if __name__ == "__main__":
    citations = [0, 1, 3, 5, 6]
    assert hIndex(citations) == 3
