---
comments: true
---

# Dynamic Programming - 2 Dimensional Table

## LeetCode Problems

1. 0118 - [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) (Easy)
2. 0119 - [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/) (Easy)
3. 0062 - [Unique Paths](https://leetcode.com/problems/unique-paths/) (Medium)
4. 0063 - [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) (Medium)

## 118. Pascal's Triangle

-   Generate the first `numRows` of Pascal's triangle.

```plaintext
                 numRows    index
     1              1         0
    1 1             2         1
   1 2 1            3         2
  1 3 3 1           4         3
 1 4 6 4 1          5         4
```

```python
--8<-- "0118_pascals_triangle.py"
```

## 119. Pascal's Triangle II

-   Return the `rowIndex`th row of Pascal's triangle.

```python
--8<-- "0119_pascals_triangle_ii.py"
```

## 62. Unique Paths

-   Count the number of unique paths to reach the bottom-right corner of a `m x n` grid.

![62](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

```python
--8<-- "0062_unique_paths.py"
```

## 63. Unique Paths II

-   Count the number of unique paths to reach the bottom-right corner of a `m x n` grid with obstacles.

![63](https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg)

```python
--8<-- "0063_unique_paths_ii.py"
```
