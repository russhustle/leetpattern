---
comments: True
---

# Stack

## Table of Contents

- [x] [439. Ternary Expression Parser](https://leetcode.cn/problems/ternary-expression-parser/) (Medium) 👑
- [ ] [484. Find Permutation](https://leetcode.cn/problems/find-permutation/) (Medium) 👑
- [x] [772. Basic Calculator III](https://leetcode.cn/problems/basic-calculator-iii/) (Hard) 👑

## 439. Ternary Expression Parser

-   [LeetCode](https://leetcode.com/problems/ternary-expression-parser/) | [LeetCode CH](https://leetcode.cn/problems/ternary-expression-parser/) (Medium)

-   Tags: string, stack, recursion
```python title="439. Ternary Expression Parser - Python Solution"
# Stack
def parseTernary(expression: str) -> str:
    stack = []
    i = len(expression) - 1

    while i >= 0:
        c = expression[i]
        if stack and stack[-1] == "?":
            stack.pop()  # remove '?'
            true_val = stack.pop()
            stack.pop()  # remove ':'
            false_val = stack.pop()
            if c == "T":
                stack.append(true_val)
            else:
                stack.append(false_val)
        else:
            stack.append(c)
        i -= 1

    return stack[-1]


if __name__ == "__main__":
    assert parseTernary("T?2:3") == "2"
    assert parseTernary("F?1:T?4:5") == "4"
    assert parseTernary("T?T?F:5:3") == "F"

```

## 484. Find Permutation

-   [LeetCode](https://leetcode.com/problems/find-permutation/) | [LeetCode CH](https://leetcode.cn/problems/find-permutation/) (Medium)

-   Tags: array, string, stack, greedy
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
