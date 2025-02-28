---
comments: True
---

# Graph BFS

- [x] [994. Rotting Oranges](https://leetcode.cn/problems/rotting-oranges/) (Medium)
- [x] [127. Word Ladder](https://leetcode.cn/problems/word-ladder/) (Hard)
- [x] [1466. Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) (Medium)
- [x] [286. Walls and Gates](https://leetcode.cn/problems/walls-and-gates/) (Medium)
- [x] [815. Bus Routes](https://leetcode.cn/problems/bus-routes/) (Hard)

## 994. Rotting Oranges

-   [LeetCode](https://leetcode.com/problems/rotting-oranges/) | [LeetCode CH](https://leetcode.cn/problems/rotting-oranges/) (Medium)
-   Tags: array, breadth first search, matrix
-   Return the minimum number of minutes that must elapse until no cell has a fresh orange.
-   Hint: Multi-source BFS to count the level.

![994](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

```python title="994. Rotting Oranges - Python Solution"
--8<-- "0994_rotting_oranges.py"
```

## 127. Word Ladder

-   [LeetCode](https://leetcode.com/problems/word-ladder/) | [LeetCode CH](https://leetcode.cn/problems/word-ladder/) (Hard)
-   Tags: hash table, string, breadth first search
-   The most classic BFS problem.
-   Return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

<iframe width="560" height="315" src="https://www.youtube.com/embed/h9iTnkgv05E?si=51-3ZwweoJrPqRW9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

| Approach | Time        | Space     |
| -------- | ----------- | --------- |
| BFS      | O(n \* m^2) | O(n \* m) |

```python title="127. Word Ladder - Python Solution"
--8<-- "0127_word_ladder.py"
```

## 1466. Reorder Routes to Make All Paths Lead to the City Zero

-   [LeetCode](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) | [LeetCode CH](https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) (Medium)
-   Tags: depth first search, breadth first search, graph
-   ![1466](https://assets.leetcode.com/uploads/2020/05/13/sample_1_1819.png)

```python title="1466. Reorder Routes to Make All Paths Lead to the City Zero - Python Solution"
--8<-- "1466_reorder_routes_to_make_all_paths_lead_to_the_city_zero.py"
```

## 286. Walls and Gates

-   [LeetCode](https://leetcode.com/problems/walls-and-gates/) | [LeetCode CH](https://leetcode.cn/problems/walls-and-gates/) (Medium)
-   Tags: array, breadth first search, matrix
![286](https://assets.leetcode.com/uploads/2021/01/03/grid.jpg)

```python title="286. Walls and Gates - Python Solution"
--8<-- "0286_walls_and_gates.py"
```

## 815. Bus Routes

-   [LeetCode](https://leetcode.com/problems/bus-routes/) | [LeetCode CH](https://leetcode.cn/problems/bus-routes/) (Hard)
-   Tags: array, hash table, breadth first search

```python title="815. Bus Routes - Python Solution"
--8<-- "0815_bus_routes.py"
```
