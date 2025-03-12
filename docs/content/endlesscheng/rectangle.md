---
comments: True
---

# Rectangle

- [x] [84. Largest Rectangle in Histogram](https://leetcode.cn/problems/largest-rectangle-in-histogram/) (Hard)
- [ ] [1793. Maximum Score of a Good Subarray](https://leetcode.cn/problems/maximum-score-of-a-good-subarray/) (Hard)
- [x] [85. Maximal Rectangle](https://leetcode.cn/problems/maximal-rectangle/) (Hard)
- [ ] [1504. Count Submatrices With All Ones](https://leetcode.cn/problems/count-submatrices-with-all-ones/) (Medium)
- [x] [42. Trapping Rain Water](https://leetcode.cn/problems/trapping-rain-water/) (Hard)
- [ ] [755. Pour Water](https://leetcode.cn/problems/pour-water/) (Medium) 👑

## 84. Largest Rectangle in Histogram

-   [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [LeetCode CH](https://leetcode.cn/problems/largest-rectangle-in-histogram/) (Hard)

-   Tags: array, stack, monotonic stack

```python title="84. Largest Rectangle in Histogram - Python Solution"
from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    maxArea = 0
    stack = []  # pair: (index, height)

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))

    return maxArea


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10

```

## 1793. Maximum Score of a Good Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-score-of-a-good-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-score-of-a-good-subarray/) (Hard)

-   Tags: array, two pointers, binary search, stack, monotonic stack

## 85. Maximal Rectangle

-   [LeetCode](https://leetcode.com/problems/maximal-rectangle/) | [LeetCode CH](https://leetcode.cn/problems/maximal-rectangle/) (Hard)

-   Tags: array, dynamic programming, stack, matrix, monotonic stack
- Return the area of the largest rectangle that can be formed within a rectangle of 1's.

![0085](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg)

```python title="85. Maximal Rectangle - Python Solution"
from typing import List


# Monotonic Stack
def maximalRectangle(matrix: List[List[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix[0])
    heights = [0] * (n + 1)
    max_area = 0

    for row in matrix:
        for i in range(n):
            if row[i] == "1":
                heights[i] += 1
            else:
                heights[i] = 0

        stack = [-1]
        for i in range(n + 1):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

    return max_area


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(maximalRectangle(matrix))  # 6

```

## 1504. Count Submatrices With All Ones

-   [LeetCode](https://leetcode.com/problems/count-submatrices-with-all-ones/) | [LeetCode CH](https://leetcode.cn/problems/count-submatrices-with-all-ones/) (Medium)

-   Tags: array, dynamic programming, stack, matrix, monotonic stack

## 42. Trapping Rain Water

-   [LeetCode](https://leetcode.com/problems/trapping-rain-water/) | [LeetCode CH](https://leetcode.cn/problems/trapping-rain-water/) (Hard)

-   Tags: array, two pointers, dynamic programming, stack, monotonic stack
-   ![42](../assets/0042.png)

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZI2z5pq0TqA?si=OEYg01dbmzvmtIwZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

| Approach   | Time | Space |
| ---------- | ---- | ----- |
| DP         | O(N) | O(N)  |
| Left Right | O(N) | O(1)  |
| Monotonic  | O(N) | O(N)  |

```python title="42. Trapping Rain Water - Python Solution"
from typing import List


# DP
def trapDP(height: List[int]) -> int:
    if not height:
        return 0

    n = len(height)
    maxLeft, maxRight = [0 for _ in range(n)], [0 for _ in range(n)]

    for i in range(1, n):
        maxLeft[i] = max(maxLeft[i - 1], height[i - 1])

    for i in range(n - 2, -1, -1):
        maxRight[i] = max(maxRight[i + 1], height[i + 1])

    res = 0
    for i in range(n):
        res += max(0, min(maxLeft[i], maxRight[i]) - height[i])

    return res


# Left Right Pointers
def trapLR(height: List[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    maxL, maxR = height[left], height[right]
    res = 0

    while left < right:
        if maxL < maxR:
            left += 1
            maxL = max(maxL, height[left])
            res += maxL - height[left]
        else:
            right -= 1
            maxR = max(maxR, height[right])
            res += maxR - height[right]

    return res


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
print(trapDP(height))  # 6
print(trapLR(height))  # 6
print(trapStack(height))  # 6

```

```cpp title="42. Trapping Rain Water - C++ Solution"
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution
{
public:
    int trap(vector<int> &height)
    {
        if (height.empty())
            return 0;

        int res = 0;
        int left = 0, right = height.size() - 1;
        int maxL = height[left], maxR = height[right];

        while (left < right)
        {
            if (maxL < maxR)
            {
                left++;
                maxL = max(maxL, height[left]);
                res += maxL - height[left];
            }
            else
            {
                right--;
                maxR = max(maxR, height[right]);
                res += maxR - height[right];
            }
        }
        return res;
    }
};

int main()
{
    vector<int> height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    Solution solution;
    cout << solution.trap(height) << endl;
    return 0;
}

```

## 755. Pour Water

-   [LeetCode](https://leetcode.com/problems/pour-water/) | [LeetCode CH](https://leetcode.cn/problems/pour-water/) (Medium)

-   Tags: array, simulation
