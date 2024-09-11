# Graph - Flood Fill

!!! note
    **Flood Fill** is essentially a graph traversal algorithm (like BFS or DFS) applied to matrices (2D grids).
    It checks adjacent cells (up, down, left, right) of a starting point to determine whether they belong to the same region.
    Typically, it involves modifying or marking the cells that belong to the same connected component.

## LeetCode Problems

1. 0733 - [Flood Fill](https://leetcode.com/problems/flood-fill/) (Easy)
2. 0200 - [Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium)
3. 695 - [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) (Medium)
4. 0463 - [Island Perimeter](https://leetcode.com/problems/island-perimeter/) (Easy)
5. 0130 - [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) (Medium)
6. 0417 - [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) (Medium)

## 733. Flood Fill

- Replace all the pixels of the same color starting from the given pixel.

![733](https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg)

```python
--8<-- "0733_flood_fill.py"
```

## 200. Number of Islands

- Count the number of islands in a 2D grid.

![0200](../imgs/0200.jpg){width=400px}

```python
--8<-- "0200_number_of_islands.py"
```

## 695. Max Area of Island

- Find the maximum area of an island in a 2D grid.

![695](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)

```python
--8<-- "0695_max_area_of_island.py"
```

## 463. Island Perimeter

- Calculate the perimeter of an island in a 2D grid.

![463](https://assets.leetcode.com/uploads/2018/10/12/island.png)

```python
--8<-- "0463_island_perimeter.py"
```

## 130. Surrounded Regions

- Replace all the 'O's with 'X's if surrounded by 'X's.

```python
--8<-- "0130_surrounded_regions.py"
```

## 417. Pacific Atlantic Water Flow

- Find the list of coordinates where water can flow to both the Pacific and Atlantic oceans.

![417](https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg)

```python
--8<-- "0417_pacific_atlantic_water_flow.py"
```
