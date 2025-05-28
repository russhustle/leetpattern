---
comments: True
---

# Expression Parsing

## Table of Contents

- [x] [150. Evaluate Reverse Polish Notation](https://leetcode.cn/problems/evaluate-reverse-polish-notation/) (Medium)
- [ ] [1006. Clumsy Factorial](https://leetcode.cn/problems/clumsy-factorial/) (Medium)
- [x] [224. Basic Calculator](https://leetcode.cn/problems/basic-calculator/) (Hard)
- [x] [227. Basic Calculator II](https://leetcode.cn/problems/basic-calculator-ii/) (Medium)
- [ ] [726. Number of Atoms](https://leetcode.cn/problems/number-of-atoms/) (Hard)
- [ ] [1106. Parsing A Boolean Expression](https://leetcode.cn/problems/parsing-a-boolean-expression/) (Hard)
- [ ] [591. Tag Validator](https://leetcode.cn/problems/tag-validator/) (Hard)
- [ ] [736. Parse Lisp Expression](https://leetcode.cn/problems/parse-lisp-expression/) (Hard)
- [ ] [1096. Brace Expansion II](https://leetcode.cn/problems/brace-expansion-ii/) (Hard)
- [ ] [1896. Minimum Cost to Change the Final Value of Expression](https://leetcode.cn/problems/minimum-cost-to-change-the-final-value-of-expression/) (Hard)
- [x] [770. Basic Calculator IV](https://leetcode.cn/problems/basic-calculator-iv/) (Hard)
- [ ] [439. Ternary Expression Parser](https://leetcode.cn/problems/ternary-expression-parser/) (Medium) 👑
- [x] [772. Basic Calculator III](https://leetcode.cn/problems/basic-calculator-iii/) (Hard) 👑
- [ ] [1087. Brace Expansion](https://leetcode.cn/problems/brace-expansion/) (Medium) 👑
- [ ] [1597. Build Binary Expression Tree From Infix Expression](https://leetcode.cn/problems/build-binary-expression-tree-from-infix-expression/) (Hard) 👑
- [ ] [1628. Design an Expression Tree With Evaluate Function](https://leetcode.cn/problems/design-an-expression-tree-with-evaluate-function/) (Medium) 👑

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

## 1006. Clumsy Factorial

-   [LeetCode](https://leetcode.com/problems/clumsy-factorial/) | [LeetCode CH](https://leetcode.cn/problems/clumsy-factorial/) (Medium)

-   Tags: math, stack, simulation
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

## 726. Number of Atoms

-   [LeetCode](https://leetcode.com/problems/number-of-atoms/) | [LeetCode CH](https://leetcode.cn/problems/number-of-atoms/) (Hard)

-   Tags: hash table, string, stack, sorting
## 1106. Parsing A Boolean Expression

-   [LeetCode](https://leetcode.com/problems/parsing-a-boolean-expression/) | [LeetCode CH](https://leetcode.cn/problems/parsing-a-boolean-expression/) (Hard)

-   Tags: string, stack, recursion
## 591. Tag Validator

-   [LeetCode](https://leetcode.com/problems/tag-validator/) | [LeetCode CH](https://leetcode.cn/problems/tag-validator/) (Hard)

-   Tags: string, stack
## 736. Parse Lisp Expression

-   [LeetCode](https://leetcode.com/problems/parse-lisp-expression/) | [LeetCode CH](https://leetcode.cn/problems/parse-lisp-expression/) (Hard)

-   Tags: hash table, string, stack, recursion
## 1096. Brace Expansion II

-   [LeetCode](https://leetcode.com/problems/brace-expansion-ii/) | [LeetCode CH](https://leetcode.cn/problems/brace-expansion-ii/) (Hard)

-   Tags: string, backtracking, stack, breadth first search
## 1896. Minimum Cost to Change the Final Value of Expression

-   [LeetCode](https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-to-change-the-final-value-of-expression/) (Hard)

-   Tags: math, string, dynamic programming, stack
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

## 439. Ternary Expression Parser

-   [LeetCode](https://leetcode.com/problems/ternary-expression-parser/) | [LeetCode CH](https://leetcode.cn/problems/ternary-expression-parser/) (Medium)

-   Tags: string, stack, recursion
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

## 1087. Brace Expansion

-   [LeetCode](https://leetcode.com/problems/brace-expansion/) | [LeetCode CH](https://leetcode.cn/problems/brace-expansion/) (Medium)

-   Tags: string, backtracking, breadth first search
## 1597. Build Binary Expression Tree From Infix Expression

-   [LeetCode](https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/) | [LeetCode CH](https://leetcode.cn/problems/build-binary-expression-tree-from-infix-expression/) (Hard)

-   Tags: string, stack, tree, binary tree
## 1628. Design an Expression Tree With Evaluate Function

-   [LeetCode](https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/) | [LeetCode CH](https://leetcode.cn/problems/design-an-expression-tree-with-evaluate-function/) (Medium)

-   Tags: array, math, stack, tree, design, binary tree
