---
comments: True
---

# DP 2D

- [x] [118. Pascal's Triangle](https://leetcode.cn/problems/pascals-triangle/) (Easy)
- [x] [119. Pascal's Triangle II](https://leetcode.cn/problems/pascals-triangle-ii/) (Easy)
- [x] [62. Unique Paths](https://leetcode.cn/problems/unique-paths/) (Medium)
- [x] [63. Unique Paths II](https://leetcode.cn/problems/unique-paths-ii/) (Medium)

## 118. Pascal's Triangle

-   [LeetCode](https://leetcode.com/problems/pascals-triangle/) | [LeetCode CH](https://leetcode.cn/problems/pascals-triangle/) (Easy)

-   Tags: array, dynamic programming
-   Generate the first `numRows` of Pascal's triangle.

```plaintext
                 numRows    index
     1              1         0
    1 1             2         1
   1 2 1            3         2
  1 3 3 1           4         3
 1 4 6 4 1          5         4
```

```python title="118. Pascal's Triangle - Python Solution"
--8<-- "0118_pascals_triangle.py"
```

## 119. Pascal's Triangle II

-   [LeetCode](https://leetcode.com/problems/pascals-triangle-ii/) | [LeetCode CH](https://leetcode.cn/problems/pascals-triangle-ii/) (Easy)

-   Tags: array, dynamic programming
-   Return the `rowIndex`th row of Pascal's triangle.

```python title="119. Pascal's Triangle II - Python Solution"
--8<-- "0119_pascals_triangle_ii.py"
```

## 62. Unique Paths

-   [LeetCode](https://leetcode.com/problems/unique-paths/) | [LeetCode CH](https://leetcode.cn/problems/unique-paths/) (Medium)

-   Tags: math, dynamic programming, combinatorics
-   Count the number of unique paths to reach the bottom-right corner of a `m x n` grid.

![62](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

```python title="62. Unique Paths - Python Solution"
--8<-- "0062_unique_paths.py"
```

```cpp title="62. Unique Paths - C++ Solution"
--8<-- "cpp/0062_unique_paths.cc"
```

## 63. Unique Paths II

-   [LeetCode](https://leetcode.com/problems/unique-paths-ii/) | [LeetCode CH](https://leetcode.cn/problems/unique-paths-ii/) (Medium)

-   Tags: array, dynamic programming, matrix
-   Count the number of unique paths to reach the bottom-right corner of a `m x n` grid with obstacles.

![63](https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg)

```python title="63. Unique Paths II - Python Solution"
--8<-- "0063_unique_paths_ii.py"
```
