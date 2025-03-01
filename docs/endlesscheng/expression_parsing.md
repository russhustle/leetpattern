---
comments: True
---

# Expression Parsing

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
- [ ] [439. Ternary Expression Parser](https://leetcode.cn/problems/ternary-expression-parser/) (Medium)
- [x] [772. Basic Calculator III](https://leetcode.cn/problems/basic-calculator-iii/) (Hard)
- [ ] [1087. Brace Expansion](https://leetcode.cn/problems/brace-expansion/) (Medium)
- [ ] [1597. Build Binary Expression Tree From Infix Expression](https://leetcode.cn/problems/build-binary-expression-tree-from-infix-expression/) (Hard)
- [ ] [1628. Design an Expression Tree With Evaluate Function](https://leetcode.cn/problems/design-an-expression-tree-with-evaluate-function/) (Medium)

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
--8<-- "0150_evaluate_reverse_polish_notation.py"
```

## 1006. Clumsy Factorial

-   [LeetCode](https://leetcode.com/problems/clumsy-factorial/) | [LeetCode CH](https://leetcode.cn/problems/clumsy-factorial/) (Medium)

-   Tags: math, stack, simulation

## 224. Basic Calculator

-   [LeetCode](https://leetcode.com/problems/basic-calculator/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator/) (Hard)

-   Tags: math, string, stack, recursion

```python title="224. Basic Calculator - Python Solution"
--8<-- "0224_basic_calculator.py"
```

## 227. Basic Calculator II

-   [LeetCode](https://leetcode.com/problems/basic-calculator-ii/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator-ii/) (Medium)

-   Tags: math, string, stack

```python title="227. Basic Calculator II - Python Solution"
--8<-- "0227_basic_calculator_ii.py"
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
--8<-- "0770_basic_calculator_iv.py"
```

## 439. Ternary Expression Parser

-   [LeetCode](https://leetcode.com/problems/ternary-expression-parser/) | [LeetCode CH](https://leetcode.cn/problems/ternary-expression-parser/) (Medium)

-   Tags: string, stack, recursion

## 772. Basic Calculator III

-   [LeetCode](https://leetcode.com/problems/basic-calculator-iii/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator-iii/) (Hard)

-   Tags: math, string, stack, recursion

```python title="772. Basic Calculator III - Python Solution"
--8<-- "0772_basic_calculator_iii.py"
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
