from typing import List


class LargestRectangleArea:
    def monotonic_stack(self, heights: List[int]) -> int:
        stack = []
        res = 0
        n = len(heights)

        for i in range(n + 1):
            h = heights[i] if i < n else 0

            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                res = max(res, height * width)

            stack.append(i)

        return res


if __name__ == "__main__":
    sol = LargestRectangleArea()
    assert sol.monotonic_stack([2, 1, 5, 6, 2, 3]) == 10
    assert sol.monotonic_stack([2, 4]) == 4
