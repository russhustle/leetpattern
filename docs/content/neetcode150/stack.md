---
comments: True
---

# Stack

## Table of Contents

- [x] [20. Valid Parentheses](https://leetcode.cn/problems/valid-parentheses/) (Easy)
- [x] [155. Min Stack](https://leetcode.cn/problems/min-stack/) (Medium)
- [x] [150. Evaluate Reverse Polish Notation](https://leetcode.cn/problems/evaluate-reverse-polish-notation/) (Medium)
- [x] [22. Generate Parentheses](https://leetcode.cn/problems/generate-parentheses/) (Medium)
- [x] [739. Daily Temperatures](https://leetcode.cn/problems/daily-temperatures/) (Medium)
- [x] [853. Car Fleet](https://leetcode.cn/problems/car-fleet/) (Medium)
- [x] [84. Largest Rectangle in Histogram](https://leetcode.cn/problems/largest-rectangle-in-histogram/) (Hard)

## 20. Valid Parentheses

-   [LeetCode](https://leetcode.com/problems/valid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/valid-parentheses/) (Easy)

-   Tags: string, stack
```python title="20. Valid Parentheses - Python Solution"
# Stack
def is_valid(s: str) -> bool:
    if len(s) % 2:
        return False

    pairs = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    stack = []
    for ch in s:
        if ch in pairs:
            stack.append(ch)
        elif not stack or ch != pairs[stack.pop()]:
            return False

    return True if not stack else False


def test_is_valid():
    assert is_valid("()[]{}")
    assert not is_valid("(]")
    assert not is_valid("([)]")
    assert is_valid("{[]}")

```

```cpp title="20. Valid Parentheses - C++ Solution"
#include <cassert>
#include <stack>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
   public:
    bool isValid(string s) {
        unordered_map<char, char> map{{')', '('}, {'}', '{'}, {']', '['}};
        stack<char> stack;
        if (s.length() % 2 == 1) return false;

        for (char& ch : s) {
            if (stack.empty() || map.find(ch) == map.end()) {
                stack.push(ch);
            } else {
                if (map[ch] != stack.top()) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.empty();
    }
};

int main() {
    Solution s;
    assert(s.isValid("()") == true);
    assert(s.isValid("()[]{}") == true);
    assert(s.isValid("(]") == false);
    assert(s.isValid("([)]") == false);
    assert(s.isValid("{[]}") == true);
    return 0;
}
```

## 155. Min Stack

-   [LeetCode](https://leetcode.com/problems/min-stack/) | [LeetCode CH](https://leetcode.cn/problems/min-stack/) (Medium)

-   Tags: stack, design
-   Implement a stack that supports push, pop, top, and retrieving the minimum element in constant time.

```python title="155. Min Stack - Python Solution"
# Stack
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append((val, min(val, self.getMin())))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


obj = MinStack()
obj.push(3)
obj.push(2)
obj.pop()
print(obj.top())  # 3
print(obj.getMin())  # 3

```

```cpp title="155. Min Stack - C++ Solution"
#include <algorithm>
#include <climits>
#include <iostream>
#include <stack>
#include <utility>
using namespace std;

class MinStack {
    stack<pair<int, int>> st;

   public:
    MinStack() { st.emplace(0, INT_MAX); }

    void push(int val) { st.emplace(val, min(getMin(), val)); }

    void pop() { st.pop(); }

    int top() { return st.top().first; }

    int getMin() { return st.top().second; }
};

int main() {
    MinStack minStack;
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    cout << minStack.getMin() << endl;  // -3
    minStack.pop();
    cout << minStack.top() << endl;     // 0
    cout << minStack.getMin() << endl;  // -2
    return 0;
}
```

## 150. Evaluate Reverse Polish Notation

-   [LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [LeetCode CH](https://leetcode.cn/problems/evaluate-reverse-polish-notation/) (Medium)

-   Tags: array, math, stack
```python title="150. Evaluate Reverse Polish Notation - Python Solution"
from typing import List


# Stack
def evalRPN(tokens: List[str]) -> int:
    stack = []

    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(c))

    return stack[0]


def test_evalRPN():
    print(evalRPN(["2", "1", "+", "3", "*"]))  # 9
    print(evalRPN(["4", "13", "5", "/", "-"]))  # 2
    print(evalRPN(["18"]))  # 18
    print(evalRPN(["4", "3", "-"]))  # 1

```

## 22. Generate Parentheses

-   [LeetCode](https://leetcode.com/problems/generate-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/generate-parentheses/) (Medium)

-   Tags: string, dynamic programming, backtracking
```python title="22. Generate Parentheses - Python Solution"
from typing import List


# Backtracking
def generateParenthesis1(n: int) -> List[str]:
    path, res = [], []

    def dfs(openN, closeN):
        if openN == closeN == n:
            res.append("".join(path))
            return

        if openN < n:
            path.append("(")
            dfs(openN + 1, closeN)
            path.pop()

        if closeN < openN:
            path.append(")")
            dfs(openN, closeN + 1)
            path.pop()

    dfs(0, 0)

    return res


# Backtracking
def generateParenthesis2(n: int) -> List[str]:
    m = n * 2
    res, path = [], [""] * m

    def dfs(i, left):
        if i == m:
            res.append("".join(path))
            return

        if left < n:
            path[i] = "("
            dfs(i + 1, left + 1)
        if i - left < left:
            path[i] = ")"
            dfs(i + 1, left)

    dfs(0, 0)
    return res


if __name__ == "__main__":
    print(generateParenthesis1(3))
    # ['((()))', '(()())', '(())()', '()(())', '()()()']
    print(generateParenthesis2(3))
    # ['((()))', '(()())', '(())()', '()(())', '()()()']

```

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

## 853. Car Fleet

-   [LeetCode](https://leetcode.com/problems/car-fleet/) | [LeetCode CH](https://leetcode.cn/problems/car-fleet/) (Medium)

-   Tags: array, stack, sorting, monotonic stack
```python title="853. Car Fleet - Python Solution"
from typing import List


# Stack
def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)
    stack = []

    for p, s in cars:
        time = (target - p) / s

        if not stack or time > stack[-1]:
            stack.append(time)

    return len(stack)


print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # 3

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
