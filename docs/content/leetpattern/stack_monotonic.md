---
comments: True
---

# Stack Monotonic

## Table of Contents

- [x] [739. Daily Temperatures](https://leetcode.cn/problems/daily-temperatures/) (Medium)
- [x] [496. Next Greater Element I](https://leetcode.cn/problems/next-greater-element-i/) (Easy)
- [x] [503. Next Greater Element II](https://leetcode.cn/problems/next-greater-element-ii/) (Medium)
- [x] [84. Largest Rectangle in Histogram](https://leetcode.cn/problems/largest-rectangle-in-histogram/) (Hard)
- [x] [85. Maximal Rectangle](https://leetcode.cn/problems/maximal-rectangle/) (Hard)
- [x] [42. Trapping Rain Water](https://leetcode.cn/problems/trapping-rain-water/) (Hard)
- [x] [901. Online Stock Span](https://leetcode.cn/problems/online-stock-span/) (Medium)
- [x] [316. Remove Duplicate Letters](https://leetcode.cn/problems/remove-duplicate-letters/) (Medium)
- [x] [456. 132 Pattern](https://leetcode.cn/problems/132-pattern/) (Medium)
- [x] [2281. Sum of Total Strength of Wizards](https://leetcode.cn/problems/sum-of-total-strength-of-wizards/) (Hard)

## 739. Daily Temperatures

-   [LeetCode](https://leetcode.com/problems/daily-temperatures/) | [LeetCode CH](https://leetcode.cn/problems/daily-temperatures/) (Medium)

-   Tags: array, stack, monotonic stack
-   Return an array `res` such that `res[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature.

| Index | Temp | > stack last | stack                           | result    |
| ----- | ---- | ------------ | ------------------------------- | --------- |
| 0     | 73   | False        | `[ [73, 0] ]`                   | 1 - 0 = 1 |
| 1     | 74   | True         | `[ [74, 1] ]`                   | 2 - 1 = 1 |
| 2     | 75   | True         | `[ [75, 2] ]`                   | 6 - 2 = 4 |
| 3     | 71   | False        | `[ [75, 2], [71, 3] ]`          | 5 - 3 = 2 |
| 4     | 69   | False        | `[ [75, 2], [71, 3], [69, 4] ]` | 5 - 4 = 1 |
| 5     | 72   | True         | `[ [75, 2], [72, 5] ]`          | 6 - 5 = 1 |
| 6     | 76   | True         | `[ [76, 6] ]`                   | 0         |
| 7     | 73   | False        | `[[76, 6], [73, 7]]`            | 0         |

```python title="739. Daily Temperatures - Python Solution"
from typing import List


# Monotonic Stack
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0 for _ in range(len(temperatures))]
    stack = []  # [temp, index]

    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            _, idx = stack.pop()
            res[idx] = i - idx

        stack.append([temp, i])

    return res


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1, 1, 4, 2, 1, 1, 0, 0]

```

## 496. Next Greater Element I

-   [LeetCode](https://leetcode.com/problems/next-greater-element-i/) | [LeetCode CH](https://leetcode.cn/problems/next-greater-element-i/) (Easy)

-   Tags: array, hash table, stack, monotonic stack
```python title="496. Next Greater Element I - Python Solution"
from typing import List


# Monotonic Stack
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    next_greater = {}
    stack = []
    result = []

    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)

    for num in nums1:
        result.append(next_greater.get(num, -1))

    return result


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))  # [3, -1, -1]

```

## 503. Next Greater Element II

-   [LeetCode](https://leetcode.com/problems/next-greater-element-ii/) | [LeetCode CH](https://leetcode.cn/problems/next-greater-element-ii/) (Medium)

-   Tags: array, stack, monotonic stack
```python title="503. Next Greater Element II - Python Solution"
from typing import List


# Monotonic Stack
def nextGreaterElements(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            result[stack.pop()] = nums[i % n]
        if i < n:
            stack.append(i)

    return result


nums = [1, 2, 1]
print(nextGreaterElements(nums))  # [2, -1, 2]

```

## 84. Largest Rectangle in Histogram

-   [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [LeetCode CH](https://leetcode.cn/problems/largest-rectangle-in-histogram/) (Hard)

-   Tags: array, stack, monotonic stack
```python title="84. Largest Rectangle in Histogram - Python Solution"
from typing import List


# Monotonic Stack
def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        h = 0 if i == n else heights[i]

        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10

```

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

## 42. Trapping Rain Water

-   [LeetCode](https://leetcode.com/problems/trapping-rain-water/) | [LeetCode CH](https://leetcode.cn/problems/trapping-rain-water/) (Hard)

-   Tags: array, two pointers, dynamic programming, stack, monotonic stack
- ![42](../../assets/0042.png)

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

## 901. Online Stock Span

-   [LeetCode](https://leetcode.com/problems/online-stock-span/) | [LeetCode CH](https://leetcode.cn/problems/online-stock-span/) (Medium)

-   Tags: stack, design, monotonic stack, data stream
-   Design a class `StockSpanner` to return the number of consecutive days (including the current day) the price of the stock has been less than or equal to the current price.

```python title="901. Online Stock Span - Python Solution"
from typing import List


# Monotonic Stack
class StockSpanner:

    def __init__(self):
        self.stack = [(-1, float("inf"))]
        self.cur_day = -1

    def next(self, price: int) -> int:
        while price >= self.stack[-1][1]:
            self.stack.pop()
        self.cur_day += 1
        self.stack.append((self.cur_day, price))
        return self.cur_day - self.stack[-2][0]


if __name__ == "__main__":
    ss = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    print([ss.next(price) for price in prices])  # [1, 1, 1, 2, 1, 4, 6]

```

## 316. Remove Duplicate Letters

-   [LeetCode](https://leetcode.com/problems/remove-duplicate-letters/) | [LeetCode CH](https://leetcode.cn/problems/remove-duplicate-letters/) (Medium)

-   Tags: string, stack, greedy, monotonic stack
```python title="316. Remove Duplicate Letters - Python Solution"
# Monotonic Stack
def removeDuplicateLetters(s: str) -> str:
    stack = []
    seen = set()
    last = {c: i for i, c in enumerate(s)}

    for i, c in enumerate(s):
        if c not in seen:
            while stack and c < stack[-1] and i < last[stack[-1]]:
                seen.discard(stack.pop())
            seen.add(c)
            stack.append(c)

    return "".join(stack)


s = "cbacdcbc"
print(removeDuplicateLetters(s))  # acdb

```

## 456. 132 Pattern

-   [LeetCode](https://leetcode.com/problems/132-pattern/) | [LeetCode CH](https://leetcode.cn/problems/132-pattern/) (Medium)

-   Tags: array, binary search, stack, monotonic stack, ordered set
```python title="456. 132 Pattern - Python Solution"
from typing import List


# Monotonic Stack
def find132pattern(nums: List[int]) -> bool:
    n = len(nums)
    if n < 3:
        return False

    stack = []
    second_max = float("-inf")

    for i in range(n - 1, -1, -1):
        if nums[i] < second_max:
            return True

        while stack and stack[-1] < nums[i]:
            second_max = stack.pop()

        stack.append(nums[i])

    return False


nums = [-1, 3, 2, 0]
print(find132pattern(nums))  # True

```

## 2281. Sum of Total Strength of Wizards

-   [LeetCode](https://leetcode.com/problems/sum-of-total-strength-of-wizards/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-total-strength-of-wizards/) (Hard)

-   Tags: array, stack, monotonic stack, prefix sum
```python title="2281. Sum of Total Strength of Wizards - Python Solution"
from itertools import accumulate
from typing import List


# Monotonic Stack
def totalStrength(strength: List[int]) -> int:
    n = len(strength)
    left = [-1 for _ in range(n)]
    right = [n for _ in range(n)]
    stack = []

    for i, v in enumerate(strength):
        while stack and strength[stack[-1]] >= v:
            right[stack.pop()] = i
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    prefix_sum = list(accumulate(accumulate(strength, initial=0), initial=0))

    ans = 0
    for i, v in enumerate(strength):
        l, r = left[i] + 1, right[i] - 1
        tot = (i - l + 1) * (prefix_sum[r + 2] - prefix_sum[i + 1]) - (
            r - i + 1
        ) * (prefix_sum[i + 1] - prefix_sum[l])
        ans += v * tot

    return ans % (10**9 + 7)


strength = [1, 3, 1, 2]
print(totalStrength(strength))  # 44

```
