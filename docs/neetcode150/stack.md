---
comments: True
---

# Stack

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

```python
--8<-- "0020_valid_parentheses.py"
```

## 155. Min Stack

-   [LeetCode](https://leetcode.com/problems/min-stack/) | [LeetCode CH](https://leetcode.cn/problems/min-stack/) (Medium)
-   Tags: stack, design
-   Implement a stack that supports push, pop, top, and retrieving the minimum element in constant time.

```python
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

```python
--8<-- "0150_evaluate_reverse_polish_notation.py"
```

## 22. Generate Parentheses

-   [LeetCode](https://leetcode.com/problems/generate-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/generate-parentheses/) (Medium)
-   Tags: string, dynamic programming, backtracking

```python
--8<-- "0022_generate_parentheses.py"
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

```python
--8<-- "0739_daily_temperatures.py"
```

## 853. Car Fleet

-   [LeetCode](https://leetcode.com/problems/car-fleet/) | [LeetCode CH](https://leetcode.cn/problems/car-fleet/) (Medium)
-   Tags: array, stack, sorting, monotonic stack

```python
--8<-- "0853_car_fleet.py"
```

## 84. Largest Rectangle in Histogram

-   [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [LeetCode CH](https://leetcode.cn/problems/largest-rectangle-in-histogram/) (Hard)
-   Tags: array, stack, monotonic stack

```python
--8<-- "0084_largest_rectangle_in_histogram.py"
```
