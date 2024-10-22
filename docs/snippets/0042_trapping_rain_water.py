from typing import List


# DP
def trapDP(height: List[int]) -> int:
    if not height:
        return 0
    n = len(height)

    max_left = [0 for _ in range(n)]
    max_right = [0 for _ in range(n)]

    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], height[i - 1])

    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], height[i + 1])

    total = 0

    for i in range(n):
        min_height = min(max_left[i], max_right[i])
        if min_height > height[i]:
            total += min_height - height[i]

    return total


# Left Right Pointers
def trapLR(height: List[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    maxL, maxR = height[left], height[right]
    total = 0

    while left < right:
        if maxL < maxR:
            left += 1
            maxL = max(maxL, height[left])
            total += maxL - height[left]
        else:
            right -= 1
            maxR = max(maxR, height[right])
            total += maxR - height[right]

    return total


# Monotonic Stack
def trapStack(height: List[int]) -> int:
    stack = []
    total = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(height[i], height[stack[-1]]) - height[top]
            total += distance * bounded_height
        stack.append(i)

    return total


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# | DP         |  O(N)  |  O(N)   |
# | Left Right |  O(N)  |  O(1)   |
# | Monotonic  |  O(N)  |  O(N)   |
# |------------|--------|---------|


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trapDP(height))  # 6
print(trapLR(height))  # 6
print(trapStack(height))  # 6
