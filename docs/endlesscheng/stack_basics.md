---
comments: True
---

# Stack Basics

- [x] [1441. Build an Array With Stack Operations](https://leetcode.cn/problems/build-an-array-with-stack-operations/) (Medium)
- [x] [844. Backspace String Compare](https://leetcode.cn/problems/backspace-string-compare/) (Easy)
- [x] [682. Baseball Game](https://leetcode.cn/problems/baseball-game/) (Easy)
- [x] [2390. Removing Stars From a String](https://leetcode.cn/problems/removing-stars-from-a-string/) (Medium)
- [ ] [1472. Design Browser History](https://leetcode.cn/problems/design-browser-history/) (Medium)
- [ ] [946. Validate Stack Sequences](https://leetcode.cn/problems/validate-stack-sequences/) (Medium)
- [ ] [3412. Find Mirror Score of a String](https://leetcode.cn/problems/find-mirror-score-of-a-string/) (Medium)
- [ ] [71. Simplify Path](https://leetcode.cn/problems/simplify-path/) (Medium)

## 1441. Build an Array With Stack Operations

-   [LeetCode](https://leetcode.com/problems/build-an-array-with-stack-operations/) | [LeetCode CH](https://leetcode.cn/problems/build-an-array-with-stack-operations/) (Medium)

-   Tags: array, stack, simulation

```python title="1441. Build an Array With Stack Operations - Python Solution"
--8<-- "1441_build_an_array_with_stack_operations.py"
```

## 844. Backspace String Compare

-   [LeetCode](https://leetcode.com/problems/backspace-string-compare/) | [LeetCode CH](https://leetcode.cn/problems/backspace-string-compare/) (Easy)

-   Tags: two pointers, string, stack, simulation

```python title="844. Backspace String Compare - Python Solution"
--8<-- "0844_backspace_string_compare.py"
```

## 682. Baseball Game

-   [LeetCode](https://leetcode.com/problems/baseball-game/) | [LeetCode CH](https://leetcode.cn/problems/baseball-game/) (Easy)

-   Tags: array, stack, simulation

```python title="682. Baseball Game - Python Solution"
--8<-- "0682_baseball_game.py"
```

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

```python title="2390. Removing Stars From a String - Python Solution"
--8<-- "2390_removing_stars_from_a_string.py"
```

## 1472. Design Browser History

-   [LeetCode](https://leetcode.com/problems/design-browser-history/) | [LeetCode CH](https://leetcode.cn/problems/design-browser-history/) (Medium)

-   Tags: array, linked list, stack, design, doubly linked list, data stream

## 946. Validate Stack Sequences

-   [LeetCode](https://leetcode.com/problems/validate-stack-sequences/) | [LeetCode CH](https://leetcode.cn/problems/validate-stack-sequences/) (Medium)

-   Tags: array, stack, simulation

## 3412. Find Mirror Score of a String

-   [LeetCode](https://leetcode.com/problems/find-mirror-score-of-a-string/) | [LeetCode CH](https://leetcode.cn/problems/find-mirror-score-of-a-string/) (Medium)

-   Tags: hash table, string, stack, simulation

## 71. Simplify Path

-   [LeetCode](https://leetcode.com/problems/simplify-path/) | [LeetCode CH](https://leetcode.cn/problems/simplify-path/) (Medium)

-   Tags: string, stack
