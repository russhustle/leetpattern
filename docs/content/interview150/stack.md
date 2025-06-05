---
comments: True
---

# Stack

## Table of Contents

- [x] [20. Valid Parentheses](https://leetcode.cn/problems/valid-parentheses/) (Easy)
- [ ] [71. Simplify Path](https://leetcode.cn/problems/simplify-path/) (Medium)
- [x] [155. Min Stack](https://leetcode.cn/problems/min-stack/) (Medium)
- [x] [150. Evaluate Reverse Polish Notation](https://leetcode.cn/problems/evaluate-reverse-polish-notation/) (Medium)
- [x] [224. Basic Calculator](https://leetcode.cn/problems/basic-calculator/) (Hard)

## 20. Valid Parentheses

-   [LeetCode](https://leetcode.com/problems/valid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/valid-parentheses/) (Easy)

-   Tags: string, stack
-   Determine if the input string is valid.
-   Steps for the string `()[]{}`:

| char | action | stack |
| ---- | ------ | ----- |
| `(`  | push   | "("   |
| `)`  | pop    | ""    |
| `[`  | push   | "["   |
| `]`  | pop    | ""    |
| `{`  | push   | "{"   |
| `}`  | pop    | ""    |


```python title="20. Valid Parentheses - Python Solution"
# Stack
def isValid(s: str) -> bool:
    hashmap = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = []

    for c in s:
        if c in hashmap:
            if stack and stack[-1] == hashmap[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False


print(isValid("()"))  # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))  # False

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

## 71. Simplify Path

-   [LeetCode](https://leetcode.com/problems/simplify-path/) | [LeetCode CH](https://leetcode.cn/problems/simplify-path/) (Medium)

-   Tags: string, stack
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
-   Steps for the list `["2", "1", "+", "3", "*"]`:

| token | action | stack    |
| ----- | ------ | -------- |
| `2`   | push   | `[2]`    |
| `1`   | push   | `[2, 1]` |
| `+`   | pop    | `[3]`    |
| `3`   | push   | `[3, 3]` |
| `*`   | pop    | `[9]`    |


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


print(evalRPN(["2", "1", "+", "3", "*"]))  # 9
print(evalRPN(["4", "13", "5", "/", "-"]))  # 2
print(evalRPN(["18"]))  # 18
print(evalRPN(["4", "3", "-"]))  # 1

```

## 224. Basic Calculator

-   [LeetCode](https://leetcode.com/problems/basic-calculator/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator/) (Hard)

-   Tags: math, string, stack, recursion

```python title="224. Basic Calculator - Python Solution"
# Stack
def calculate(s: str) -> int:
    stack = []
    result = 0
    number = 0
    sign = 1

    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)

        elif char == "+":
            result += sign * number
            number = 0
            sign = 1
        elif char == "-":
            result += sign * number
            number = 0
            sign = -1

        elif char == "(":
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ")":
            result += sign * number
            number = 0
            result *= stack.pop()  # pop sign
            result += stack.pop()  # pop previous result

    result += sign * number

    return result


print(calculate("(1+(4+5+2)-3)+(6+8)"))  # 23

```
