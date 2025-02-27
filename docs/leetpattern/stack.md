---
comments: True
---

# Stack

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
- [x] [772. Basic Calculator III](https://leetcode.cn/problems/basic-calculator-iii/) (Hard)
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
| \*   | pop    | "lee"   |
| \*   | pop    | "le"    |
| c    | push   | "lec"   |
| o    | push   | "leco"  |
| d    | push   | "lecod" |
| \*   | pop    | "leco"  |
| e    | push   | "lecoe" |

```python title="2390. Removing Stars From a String"
--8<-- "2390_removing_stars_from_a_string.py"
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

```python title="1544. Make The String Great"
--8<-- "1544_make_the_string_great.py"
```

## 20. Valid Parentheses

-   [LeetCode](https://leetcode.com/problems/valid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/valid-parentheses/) (Easy)
-   Tags: string, stack
-   Determine if the input string is valid.
-   Steps for the string `()[]{}`:

| char | action | stack |
| ---- | ------ | ----- |
| `(`  | push   | "\("  |
| `)`  | pop    | ""    |
| `[`  | push   | "\["  |
| `]`  | pop    | ""    |
| `{`  | push   | "\{"  |
| `}`  | pop    | ""    |

```python title="20. Valid Parentheses"
--8<-- "0020_valid_parentheses.py"
```

## 155. Min Stack

-   [LeetCode](https://leetcode.com/problems/min-stack/) | [LeetCode CH](https://leetcode.cn/problems/min-stack/) (Medium)
-   Tags: stack, design
-   Implement a stack that supports push, pop, top, and retrieving the minimum element in constant time.

```python title="155. Min Stack"
--8<-- "0155_min_stack.py"
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

```python title="150. Evaluate Reverse Polish Notation"
--8<-- "0150_evaluate_reverse_polish_notation.py"
```

## 394. Decode String

-   [LeetCode](https://leetcode.com/problems/decode-string/) | [LeetCode CH](https://leetcode.cn/problems/decode-string/) (Medium)
-   Tags: string, stack, recursion

```python title="394. Decode String"
--8<-- "0394_decode_string.py"
```

## 22. Generate Parentheses

-   [LeetCode](https://leetcode.com/problems/generate-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/generate-parentheses/) (Medium)
-   Tags: string, dynamic programming, backtracking

```python title="22. Generate Parentheses"
--8<-- "0022_generate_parentheses.py"
```

## 853. Car Fleet

-   [LeetCode](https://leetcode.com/problems/car-fleet/) | [LeetCode CH](https://leetcode.cn/problems/car-fleet/) (Medium)
-   Tags: array, stack, sorting, monotonic stack

```python title="853. Car Fleet"
--8<-- "0853_car_fleet.py"
```

## 224. Basic Calculator

-   [LeetCode](https://leetcode.com/problems/basic-calculator/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator/) (Hard)
-   Tags: math, string, stack, recursion

```python title="224. Basic Calculator"
--8<-- "0224_basic_calculator.py"
```

## 227. Basic Calculator II

-   [LeetCode](https://leetcode.com/problems/basic-calculator-ii/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator-ii/) (Medium)
-   Tags: math, string, stack

```python title="227. Basic Calculator II"
--8<-- "0227_basic_calculator_ii.py"
```

## 772. Basic Calculator III

-   [LeetCode](https://leetcode.com/problems/basic-calculator-iii/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator-iii/) (Hard)
-   Tags: math, string, stack, recursion

```python title="772. Basic Calculator III"
--8<-- "0772_basic_calculator_iii.py"
```

## 770. Basic Calculator IV

-   [LeetCode](https://leetcode.com/problems/basic-calculator-iv/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator-iv/) (Hard)
-   Tags: hash table, math, string, stack, recursion

```python title="770. Basic Calculator IV"
--8<-- "0770_basic_calculator_iv.py"
```
