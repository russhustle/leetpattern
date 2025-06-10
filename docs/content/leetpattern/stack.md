---
comments: True
---

# Stack

## Table of Contents

- [x] [2390. Removing Stars From a String](https://leetcode.cn/problems/removing-stars-from-a-string/) (Medium)
- [x] [1544. Make The String Great](https://leetcode.cn/problems/make-the-string-great/) (Easy)
- [x] [20. Valid Parentheses](https://leetcode.cn/problems/valid-parentheses/) (Easy)
- [x] [155. Min Stack](https://leetcode.cn/problems/min-stack/) (Medium)
- [x] [150. Evaluate Reverse Polish Notation](https://leetcode.cn/problems/evaluate-reverse-polish-notation/) (Medium)
- [x] [394. Decode String](https://leetcode.cn/problems/decode-string/) (Medium)
- [x] [22. Generate Parentheses](https://leetcode.cn/problems/generate-parentheses/) (Medium)
- [x] [853. Car Fleet](https://leetcode.cn/problems/car-fleet/) (Medium)
- [x] [224. Basic Calculator](https://leetcode.cn/problems/basic-calculator/) (Hard)
- [x] [227. Basic Calculator II](https://leetcode.cn/problems/basic-calculator-ii/) (Medium)
- [x] [772. Basic Calculator III](https://leetcode.cn/problems/basic-calculator-iii/) (Hard) 👑
- [x] [770. Basic Calculator IV](https://leetcode.cn/problems/basic-calculator-iv/) (Hard)

## 2390. Removing Stars From a String

-   [LeetCode](https://leetcode.com/problems/removing-stars-from-a-string/) | [LeetCode CH](https://leetcode.cn/problems/removing-stars-from-a-string/) (Medium)

-   Tags: string, stack, simulation
-   Remove all `*` characters and their adjacent characters from the string.
-   Steps for the string `leet**cod*e`:

| char | action | stack   |
| ---- | ------ | ------- |
| l    | push   | "l"     |
| e    | push   | "le"    |
| e    | push   | "lee"   |
| t    | push   | "leet"  |
| *    | pop    | "lee"   |
| *    | pop    | "le"    |
| c    | push   | "lec"   |
| o    | push   | "leco"  |
| d    | push   | "lecod" |
| *    | pop    | "leco"  |
| e    | push   | "lecoe" |


```python title="2390. Removing Stars From a String - Python Solution"
# Stack
def removeStars(s: str) -> str:
    stack = []

    for char in s:
        if char == "*":
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


s = "leet**cod*e"
print(removeStars(s))  # "lecoe"

```

## 1544. Make The String Great

-   [LeetCode](https://leetcode.com/problems/make-the-string-great/) | [LeetCode CH](https://leetcode.cn/problems/make-the-string-great/) (Easy)

-   Tags: string, stack
-   Remove all adjacent characters that are the same and have different cases.
-   Steps for the string `leEeetcode`:

| char | action | stack      |
| ---- | ------ | ---------- |
| l    | push   | "l"        |
| e    | push   | "le"       |
| E    | pop    | "l"        |
| e    | push   | "le"       |
| e    | push   | "lee"      |
| t    | push   | "leet"     |
| c    | push   | "leetc"    |
| o    | push   | "leetco"   |
| d    | push   | "leetcod"  |
| e    | push   | "leetcode" |


```python title="1544. Make The String Great - Python Solution"
# Stack
def makeGood(s: str) -> str:
    stack = []

    for i in range(len(s)):
        if stack and stack[-1] == s[i].swapcase():
            stack.pop()
        else:
            stack.append(s[i])
    return "".join(stack)


print(makeGood("leEeetcode"))  # "leetcode"

```

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

    for ch in s:
        if ch in hashmap:
            if stack and stack[-1] == hashmap[ch]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)

    return True if not stack else False


if __name__ == "__main__":
    assert isValid("()[]{}")
    assert not isValid("(]")
    assert not isValid("([)]")
    assert isValid("{[]}")
    assert isValid("")

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

## 394. Decode String

-   [LeetCode](https://leetcode.com/problems/decode-string/) | [LeetCode CH](https://leetcode.cn/problems/decode-string/) (Medium)

-   Tags: string, stack, recursion

```python title="394. Decode String - Python Solution"
# Stack
def decodeString(s: str) -> str:
    stack = []  # (str, int)
    num = 0
    res = ""

    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == "[":
            stack.append((res, num))
            res, num = "", 0
        elif c == "]":
            top = stack.pop()
            res = top[0] + res * top[1]
        else:
            res += c

    return res


s = "3[a2[c]]"
print(decodeString(s))  # accaccacc

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

## 227. Basic Calculator II

-   [LeetCode](https://leetcode.com/problems/basic-calculator-ii/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator-ii/) (Medium)

-   Tags: math, string, stack

```python title="227. Basic Calculator II - Python Solution"
# Stack
def calculate(s: str) -> int:
    stack = []
    num = 0
    sign = "+"

    for index, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)

        if char in "+-*/" or index == len(s) - 1:
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            elif sign == "/":
                stack.append(int(stack.pop() / num))
            sign = char
            num = 0

    return sum(stack)


s = "3+2*2"
print(calculate(s))  # 7

```

## 772. Basic Calculator III

-   [LeetCode](https://leetcode.com/problems/basic-calculator-iii/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator-iii/) (Hard)

-   Tags: math, string, stack, recursion

```python title="772. Basic Calculator III - Python Solution"
# Stack
def calculate(s: str) -> int:
    def helper(index):
        stack = []
        num = 0
        sign = "+"

        while index < len(s):
            char = s[index]
            if char.isdigit():
                num = num * 10 + int(char)
            if char == "(":
                num, index = helper(index + 1)
            if char in "+-*/)" or index == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))  # 向零取整
                num = 0
                sign = char
            if char == ")":
                break
            index += 1

        return sum(stack), index

    s = s.replace(" ", "")
    result, _ = helper(0)

    return result


s = "2*(5+5*2)/3+(6/2+8)"
print(calculate(s))  # 21

```

## 770. Basic Calculator IV

-   [LeetCode](https://leetcode.com/problems/basic-calculator-iv/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator-iv/) (Hard)

-   Tags: hash table, math, string, stack, recursion

```python title="770. Basic Calculator IV - Python Solution"
from collections import defaultdict
from typing import List


# Stack
class Solution:
    def __init__(self):
        self.operators = set(["+", "-", "*"])

    def basicCalculatorIV(
        self, expression: str, evalvars: List[str], evalints: List[int]
    ) -> List[str]:
        evalmap = dict(zip(evalvars, evalints))
        tokens = self.parse_expression(expression)
        result_terms = self.evaluate(tokens, evalmap)
        return self.format_result(result_terms)

    def parse_expression(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isalnum():  # Variable or digit
                start = i
                while i < len(expression) and (
                    expression[i].isalnum() or expression[i] == "_"
                ):
                    i += 1
                tokens.append(expression[start:i])
            elif expression[i] in self.operators or expression[i] in "()":
                tokens.append(expression[i])
                i += 1
            elif expression[i] == " ":
                i += 1  # skip whitespace
        return tokens

    def evaluate(self, tokens, evalmap):
        def apply_operator(op, b, a):
            if op == "+":
                return self.add_terms(a, b)
            elif op == "-":
                return self.add_terms(a, self.negate_terms(b))
            elif op == "*":
                return self.multiply_terms(a, b)

        def process_token(token):
            if token.isalnum():
                if token in evalmap:
                    stack.append({(): evalmap[token]})
                elif token.isdigit():
                    stack.append({(): int(token)})
                else:
                    stack.append({(token,): 1})
            elif token == "(":
                ops.append(token)
            elif token == ")":
                while ops and ops[-1] != "(":
                    operate()
                ops.pop()
            else:
                while (
                    ops
                    and ops[-1] in precedence
                    and precedence[ops[-1]] >= precedence[token]
                ):
                    operate()
                ops.append(token)

        def operate():
            if len(stack) < 2 or not ops:
                return
            b = stack.pop()
            a = stack.pop()
            op = ops.pop()
            stack.append(apply_operator(op, b, a))

        stack = []
        ops = []
        precedence = {"+": 1, "-": 1, "*": 2}

        for token in tokens:
            process_token(token)

        while ops:
            operate()
        return self.combine_terms(stack[-1])

    def add_terms(self, a, b):
        result = defaultdict(int, a)
        for term, coef in b.items():
            result[term] += coef
        return dict(result)

    def negate_terms(self, a):
        return {term: -coef for term, coef in a.items()}

    def multiply_terms(self, a, b):
        result = defaultdict(int)
        for term1, coef1 in a.items():
            for term2, coef2 in b.items():
                new_term = tuple(sorted(term1 + term2))
                result[new_term] += coef1 * coef2
        return dict(result)

    def combine_terms(self, terms):
        result = defaultdict(int)
        for term, coef in terms.items():
            if coef != 0:
                result[term] = coef
        return dict(result)

    def format_result(self, result_terms):
        result = []
        for term in sorted(result_terms.keys(), key=lambda x: (-len(x), x)):
            coef = result_terms[term]
            if coef != 0:
                term_str = "*".join(term)
                if term_str:
                    result.append(f"{coef}*{term_str}")
                else:
                    result.append(str(coef))
        return result


calculator = Solution()
expression = "e + 8 - a + 5"
evalvars = ["e"]
evalints = [1]
print(calculator.basicCalculatorIV(expression, evalvars, evalints))
# ['-1*a', '14']

```
