from typing import List


# Two Pointers
def trapTP(height: List[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    leftMax, rightMax = 0, 0
    total = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                total += leftMax - height[left]
            left += 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                total += rightMax - height[right]
            right -= 1

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


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trapTP(height))  # 6
print(trapStack(height))  # 6
