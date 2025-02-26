---
comments: True
---

# Grid DFS

## 200. Number of Islands

-   [LeetCode](https://leetcode.com/problems/number-of-islands/) | [LeetCode CH](https://leetcode.cn/problems/number-of-islands/) (Medium)
-   Tags: array, depth first search, breadth first search, union find, matrix
-   Count the number of islands in a 2D grid.
-   Method 1: DFS
-   Method 2: BFS (use a queue to traverse the grid)

-   How to keep track of visited cells?

    1. Mark the visited cell as `0` (or any other value) to avoid revisiting it.
    2. Use a set to store the visited cells.

-   Steps:
    1. Init: variables
    2. DFS/BFS: starting from the cell with `1`, turn all the connected `1`s to `0`.
    3. Traverse the grid, and if the cell is `1`, increment the count and call DFS/BFS.

![0200](../assets/0200.jpg)

```python
--8<-- "0200_number_of_islands.py"
```

## 695. Max Area of Island

-   [LeetCode](https://leetcode.com/problems/max-area-of-island/) | [LeetCode CH](https://leetcode.cn/problems/max-area-of-island/) (Medium)
-   Tags: array, depth first search, breadth first search, union find, matrix

```python
--8<-- "0695_max_area_of_island.py"
```

## 463. Island Perimeter

-   [LeetCode](https://leetcode.com/problems/island-perimeter/) | [LeetCode CH](https://leetcode.cn/problems/island-perimeter/) (Easy)
-   Tags: array, depth first search, breadth first search, matrix

```python
--8<-- "0463_island_perimeter.py"
```

## 2658. Maximum Number of Fish in a Grid

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-fish-in-a-grid/) (Medium)
-   Tags: array, depth first search, breadth first search, union find, matrix

```python
--8<-- "2658_maximum_number_of_fish_in_a_grid.py"
```

## 1034. Coloring A Border

-   [LeetCode](https://leetcode.com/problems/coloring-a-border/) | [LeetCode CH](https://leetcode.cn/problems/coloring-a-border/) (Medium)
-   Tags: array, depth first search, breadth first search, matrix

```python
--8<-- "1034_coloring_a_border.py"
```

## 1020. Number of Enclaves

-   [LeetCode](https://leetcode.com/problems/number-of-enclaves/) | [LeetCode CH](https://leetcode.cn/problems/number-of-enclaves/) (Medium)
-   Tags: array, depth first search, breadth first search, union find, matrix

```python
--8<-- "1020_number_of_enclaves.py"
```

## 2684. Maximum Number of Moves in a Grid

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/) (Medium)
-   Tags: array, dynamic programming, matrix

```python
--8<-- "2684_maximum_number_of_moves_in_a_grid.py"
```

## 1254. Number of Closed Islands

-   [LeetCode](https://leetcode.com/problems/number-of-closed-islands/) | [LeetCode CH](https://leetcode.cn/problems/number-of-closed-islands/) (Medium)
-   Tags: array, depth first search, breadth first search, union find, matrix

```python
--8<-- "1254_number_of_closed_islands.py"
```

## 130. Surrounded Regions

-   [LeetCode](https://leetcode.com/problems/surrounded-regions/) | [LeetCode CH](https://leetcode.cn/problems/surrounded-regions/) (Medium)
-   Tags: array, depth first search, breadth first search, union find, matrix

```python
--8<-- "0130_surrounded_regions.py"
```

## 1905. Count Sub Islands

-   [LeetCode](https://leetcode.com/problems/count-sub-islands/) | [LeetCode CH](https://leetcode.cn/problems/count-sub-islands/) (Medium)
-   Tags: array, depth first search, breadth first search, union find, matrix

```python
--8<-- "1905_count_sub_islands.py"
```

## 1391. Check if There is a Valid Path in a Grid

-   [LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/check-if-there-is-a-valid-path-in-a-grid/) (Medium)
-   Tags: array, depth first search, breadth first search, union find, matrix

```python
--8<-- "1391_check_if_there_is_a_valid_path_in_a_grid.py"
```

## 417. Pacific Atlantic Water Flow

-   [LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [LeetCode CH](https://leetcode.cn/problems/pacific-atlantic-water-flow/) (Medium)
-   Tags: array, depth first search, breadth first search, matrix

```python
--8<-- "0417_pacific_atlantic_water_flow.py"
```

## 529. Minesweeper

-   [LeetCode](https://leetcode.com/problems/minesweeper/) | [LeetCode CH](https://leetcode.cn/problems/minesweeper/) (Medium)
-   Tags: array, depth first search, breadth first search, matrix

```python
--8<-- "0529_minesweeper.py"
```

## 1559. Detect Cycles in 2D Grid

-   [LeetCode](https://leetcode.com/problems/detect-cycles-in-2d-grid/) | [LeetCode CH](https://leetcode.cn/problems/detect-cycles-in-2d-grid/) (Medium)
-   Tags: array, depth first search, breadth first search, union find, matrix

```python
--8<-- "1559_detect_cycles_in_2d_grid.py"
```

## 827. Making A Large Island

-   [LeetCode](https://leetcode.com/problems/making-a-large-island/) | [LeetCode CH](https://leetcode.cn/problems/making-a-large-island/) (Hard)
-   Tags: array, depth first search, breadth first search, union find, matrix

```python
--8<-- "0827_making_a_large_island.py"
```

## 305. Number of Islands II

-   [LeetCode](https://leetcode.com/problems/number-of-islands-ii/) | [LeetCode CH](https://leetcode.cn/problems/number-of-islands-ii/) (Hard)
-   Tags: array, hash table, union find

```python
--8<-- "0305_number_of_islands_ii.py"
```

## 2061. Number of Spaces Cleaning Robot Cleaned

-   [LeetCode](https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/) | [LeetCode CH](https://leetcode.cn/problems/number-of-spaces-cleaning-robot-cleaned/) (Medium)
-   Tags: array, matrix, simulation

```python
--8<-- "2061_number_of_spaces_cleaning_robot_cleaned.py"
```

## 2852. Sum of Remoteness of All Cells

-   [LeetCode](https://leetcode.com/problems/sum-of-remoteness-of-all-cells/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-remoteness-of-all-cells/) (Medium)
-   Tags: array, hash table, depth first search, breadth first search, union find, matrix

```python
--8<-- "2852_sum_of_remoteness_of_all_cells.py"
```

## 489. Robot Room Cleaner

-   [LeetCode](https://leetcode.com/problems/robot-room-cleaner/) | [LeetCode CH](https://leetcode.cn/problems/robot-room-cleaner/) (Hard)
-   Tags: backtracking, interactive

```python
--8<-- "0489_robot_room_cleaner.py"
```
