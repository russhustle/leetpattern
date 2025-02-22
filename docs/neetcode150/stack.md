---
comments: True
---

# Stack

## 20. Valid Parentheses

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

=== "Python"

    ```python
    --8<-- "0020_valid_parentheses.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0020_valid_parentheses.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0020_valid_parentheses.ts"
    ```

## 155. Min Stack

-   Implement a stack that supports push, pop, top, and retrieving the minimum element in constant time.

=== "Python"

    ```python
    --8<-- "0155_min_stack.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0155_min_stack.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0155_min_stack.ts"
    ```

## 150. Evaluate Reverse Polish Notation

-   Steps for the list `["2", "1", "+", "3", "*"]`:

| token | action | stack    |
| ----- | ------ | -------- |
| `2`   | push   | `[2]`    |
| `1`   | push   | `[2, 1]` |
| `+`   | pop    | `[3]`    |
| `3`   | push   | `[3, 3]` |
| `*`   | pop    | `[9]`    |

=== "Python"

    ```python
    --8<-- "0150_evaluate_reverse_polish_notation.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0150_evaluate_reverse_polish_notation.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0150_evaluate_reverse_polish_notation.ts"
    ```

## 22. Generate Parentheses

=== "Python"

    ```python
    --8<-- "0022_generate_parentheses.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0022_generate_parentheses.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0022_generate_parentheses.ts"
    ```

## 739. Daily Temperatures

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

=== "Python"

    ```python
    --8<-- "0739_daily_temperatures.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0739_daily_temperatures.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0739_daily_temperatures.ts"
    ```

## 853. Car Fleet

=== "Python"

    ```python
    --8<-- "0853_car_fleet.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0853_car_fleet.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0853_car_fleet.ts"
    ```

## 84. Largest Rectangle in Histogram

=== "Python"

    ```python
    --8<-- "0084_largest_rectangle_in_histogram.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0084_largest_rectangle_in_histogram.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0084_largest_rectangle_in_histogram.ts"
    ```
