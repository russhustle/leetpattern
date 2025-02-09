---
comments: true
---

# Graph - Breadth First Search (BFS)

## Prerequisites problems

1. 0102 - [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/) (Medium)
2. 0733 - [Flood Fill](https://leetcode.com/problems/flood-fill/) | [图像渲染](https://leetcode.cn/problems/flood-fill/) (Easy)
3. 0200 - [Number of Islands](https://leetcode.com/problems/number-of-islands/) | [岛屿数量](https://leetcode.cn/problems/number-of-islands/) (Medium)

## LeetCode Problems

1. 0994 - [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | [腐烂的橘子](https://leetcode.cn/problems/rotting-oranges/) (Medium)
2. 0127 - [Word Ladder](https://leetcode.com/problems/word-ladder/) | [单词接龙](https://leetcode.cn/problems/word-ladder/) (Hard)
3. 1466 - [Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) | [重新规划路线以到达所有城市](https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) (Medium)
4. 0286 - [Walls and Gates](https://leetcode.com/problems/walls-and-gates/) | [墙与门](https://leetcode.cn/problems/walls-and-gates/) (Medium)
5. 0815 - [Bus Routes](https://leetcode.com/problems/bus-routes/) | [公交路线](https://leetcode.cn/problems/bus-routes/) (Hard)

## 994. Rotting Oranges

-   Return the minimum number of minutes that must elapse until no cell has a fresh orange.
-   Hint: Multi-source BFS to count the level.

![994](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

```python
--8<-- "0994_rotting_oranges.py"
```

## 127. Word Ladder

-   Return the length of the shortest transformation sequence from `beginWord` to `endWord`.

```python
--8<-- "0127_word_ladder.py"
```

## 1466. Reorder Routes to Make All Paths Lead to the City Zero

-   Return the minimum number of connections needed to connect all the cities such that all the roads are used in the right direction.

![1466](https://assets.leetcode.com/uploads/2020/05/13/sample_1_1819.png)

```python
--8<-- "1466_reorder_routes_to_make_all_paths_lead_to_the_city_zero.py"
```

## 286. Walls and Gates

-   Fill each empty room with the distance to its nearest gate.

![286](https://assets.leetcode.com/uploads/2021/01/03/grid.jpg)

```python
--8<-- "0286_walls_and_gates.py"
```

## 0815. Bus Routes

-   Return the least number of buses one must take to reach the destination from the source.

```python
--8<-- "0815_bus_routes.py"
```
