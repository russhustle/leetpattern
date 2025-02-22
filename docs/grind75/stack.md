---
comments: True
---

# Stack

## 20. Valid Parentheses

-  [LeetCode](https://leetcode.com/problems/valid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/valid-parentheses/) (Easy)

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

-  [LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/) | [LeetCode CH](https://leetcode.cn/problems/implement-queue-using-stacks/) (Easy)

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

-  [LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [LeetCode CH](https://leetcode.cn/problems/evaluate-reverse-polish-notation/) (Medium)

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

-  [LeetCode](https://leetcode.com/problems/min-stack/) | [LeetCode CH](https://leetcode.cn/problems/min-stack/) (Medium)

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

-  [LeetCode](https://leetcode.com/problems/trapping-rain-water/) | [LeetCode CH](https://leetcode.cn/problems/trapping-rain-water/) (Hard)

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

-  [LeetCode](https://leetcode.com/problems/basic-calculator/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator/) (Hard)

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

-  [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [LeetCode CH](https://leetcode.cn/problems/largest-rectangle-in-histogram/) (Hard)

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
