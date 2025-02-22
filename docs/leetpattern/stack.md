---
comments: True
---

# Stack

## 2390. Removing Stars From a String

-  [LeetCode](https://leetcode.com/problems/removing-stars-from-a-string/) | [LeetCode CH](https://leetcode.cn/problems/removing-stars-from-a-string/) (Medium)

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

=== "Python"

    ```python
    --8<-- "2390_removing_stars_from_a_string.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/2390_removing_stars_from_a_string.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/2390_removing_stars_from_a_string.ts"
    ```

## 1544. Make The String Great

-  [LeetCode](https://leetcode.com/problems/make-the-string-great/) | [LeetCode CH](https://leetcode.cn/problems/make-the-string-great/) (Easy)

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

=== "Python"

    ```python
    --8<-- "1544_make_the_string_great.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/1544_make_the_string_great.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/1544_make_the_string_great.ts"
    ```

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

## 394. Decode String

-  [LeetCode](https://leetcode.com/problems/decode-string/) | [LeetCode CH](https://leetcode.cn/problems/decode-string/) (Medium)

=== "Python"

    ```python
    --8<-- "0394_decode_string.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0394_decode_string.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0394_decode_string.ts"
    ```

## 22. Generate Parentheses

-  [LeetCode](https://leetcode.com/problems/generate-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/generate-parentheses/) (Medium)

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

## 853. Car Fleet

-  [LeetCode](https://leetcode.com/problems/car-fleet/) | [LeetCode CH](https://leetcode.cn/problems/car-fleet/) (Medium)

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

## 227. Basic Calculator II

-  [LeetCode](https://leetcode.com/problems/basic-calculator-ii/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator-ii/) (Medium)

=== "Python"

    ```python
    --8<-- "0227_basic_calculator_ii.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0227_basic_calculator_ii.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0227_basic_calculator_ii.ts"
    ```

## 772. Basic Calculator III

-  [LeetCode](https://leetcode.com/problems/basic-calculator-iii/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator-iii/) (Hard)

=== "Python"

    ```python
    --8<-- "0772_basic_calculator_iii.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0772_basic_calculator_iii.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0772_basic_calculator_iii.ts"
    ```

## 770. Basic Calculator IV

-  [LeetCode](https://leetcode.com/problems/basic-calculator-iv/) | [LeetCode CH](https://leetcode.cn/problems/basic-calculator-iv/) (Hard)

=== "Python"

    ```python
    --8<-- "0770_basic_calculator_iv.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0770_basic_calculator_iv.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0770_basic_calculator_iv.ts"
    ```
