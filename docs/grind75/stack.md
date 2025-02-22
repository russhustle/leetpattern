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

## 232. Implement Queue using Stacks

-   Implement the following operations of a queue using stacks.
    -   `push(x)` - Push element x to the back of queue.
    -   `pop()` - Removes the element from in front of queue.
    -   `peek()` - Get the front element.
    -   `empty()` - Return whether the queue is empty.

=== "Python"

    ```python
    --8<-- "0232_implement_queue_using_stacks.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0232_implement_queue_using_stacks.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0232_implement_queue_using_stacks.ts"
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

## 42. Trapping Rain Water

=== "Python"

    ```python
    --8<-- "0042_trapping_rain_water.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0042_trapping_rain_water.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0042_trapping_rain_water.ts"
    ```

## 224. Basic Calculator

=== "Python"

    ```python
    --8<-- "0224_basic_calculator.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0224_basic_calculator.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0224_basic_calculator.ts"
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
