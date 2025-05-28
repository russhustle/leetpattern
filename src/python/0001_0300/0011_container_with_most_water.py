"""
- Return the maximum area of water that can be trapped between the vertical lines.

![11](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)
"""

from typing import List


# Brute Force
def maxAreaBF(height: List[int]) -> int:
    max_area = 0

    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            h = min(height[i], height[j])
            w = j - i
            max_area = max(max_area, h * w)

    return max_area


# Left Right Pointers
def maxAreaLR(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    res = 0

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        res = max(res, h * w)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return res


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# | Brute Force| O(n^2) |  O(1)   |
# | Left Right |  O(n)  |  O(1)   |
# |------------|--------|---------|


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxAreaBF(height))  # 49
print(maxAreaLR(height))  # 49
