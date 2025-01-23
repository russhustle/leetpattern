---
comments: true
---

# Stack

## LeetCode Problems

| Order | Number | LeetCode                                                                                            | 力扣                                                                               | Difficulty |
| ----- | ------ | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------- |
| 1     | 2390   | [Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/)         | [移除字符串中的星号](https://leetcode.cn/problems/removing-stars-from-a-string/)   | Medium     |
| 2     | 1544   | [Make The String Great](https://leetcode.com/problems/make-the-string-great/)                       | [使字符串变好](https://leetcode.cn/problems/make-the-string-great/)                | Easy       |
| 3     | 0020   | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)                               | [有效的括号](https://leetcode.cn/problems/valid-parentheses/)                      | Easy       |
| 4     | 0155   | [Min Stack](https://leetcode.com/problems/min-stack/)                                               | [最小栈](https://leetcode.cn/problems/min-stack/)                                  | Easy       |
| 5     | 0150   | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [逆波兰表达式求值](https://leetcode.cn/problems/evaluate-reverse-polish-notation/) | Medium     |
| 6     | 0394   | [Decode String](https://leetcode.com/problems/decode-string/)                                       | [字符串解码](https://leetcode.cn/problems/decode-string/)                          | Medium     |
| 7     | 0022   | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)                         | [括号生成](https://leetcode.cn/problems/generate-parentheses/)                     | Medium     |
| 8     | 0853   | [Car Fleet](https://leetcode.com/problems/car-fleet/)                                               | [车队](https://leetcode.cn/problems/car-fleet/)                                    | Medium     |
| 9     | 0224   | [Basic Calculator](https://leetcode.com/problems/basic-calculator/)                                 | [基本计算器](https://leetcode.cn/problems/basic-calculator/)                       | Hard       |
| 10    | 0227   | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)                           | [基本计算器 II](https://leetcode.cn/problems/basic-calculator-ii/)                 | Medium     |
| 11    | 0772   | [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/)                         | [基本计算器 III](https://leetcode.cn/problems/basic-calculator-iii/)               | Hard       |
| 12    | 0770   | [Basic Calculator IV](https://leetcode.com/problems/basic-calculator-iv/)                           | [基本计算器 IV](https://leetcode.cn/problems/basic-calculator-iv/)                 | Hard       |

## 2390. Removing Stars From a String

-   Remove all `*` characters and their adjacent characters from the string.

```python
--8<-- "2390_removing_stars_from_a_string.py"
```

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

## 1544. Make The String Great

-   Remove all adjacent characters that are the same and have different cases.

```python
--8<-- "1544_make_the_string_great.py"
```

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

## 20. Valid Parentheses

-   Determine if the input string is valid.

```python
--8<-- "0020_valid_parentheses.py"
```

-   Steps for the string `()[]{}`:

| char | action | stack |
| ---- | ------ | ----- |
| `(`  | push   | "\("  |
| `)`  | pop    | ""    |
| `[`  | push   | "\["  |
| `]`  | pop    | ""    |
| `{`  | push   | "\{"  |
| `}`  | pop    | ""    |

## 155. Min Stack

-   Implement a stack that supports push, pop, top, and retrieving the minimum element in constant time.

```python
--8<-- "0155_min_stack.py"
```

## 150. Evaluate Reverse Polish Notation

```python
--8<-- "0150_evaluate_reverse_polish_notation.py"
```

-   Steps for the list `["2", "1", "+", "3", "*"]`:

| token | action | stack    |
| ----- | ------ | -------- |
| `2`   | push   | `[2]`    |
| `1`   | push   | `[2, 1]` |
| `+`   | pop    | `[3]`    |
| `3`   | push   | `[3, 3]` |
| `*`   | pop    | `[9]`    |

## 394. Decode String

```python
--8<-- "0394_decode_string.py"
```

## 22. Generate Parentheses

```python
--8<-- "0022_generate_parentheses.py"
```

## 853. Car Fleet

```python
--8<-- "0853_car_fleet.py"
```

## 224. Basic Calculator

```python
--8<-- "0224_basic_calculator.py"
```

## 227. Basic Calculator II

```python
--8<-- "0227_basic_calculator_ii.py"
```

## 772. Basic Calculator III

```python
--8<-- "0772_basic_calculator_iii.py"
```

## 770. Basic Calculator IV

```python
--8<-- "0770_basic_calculator_iv.py"
```
