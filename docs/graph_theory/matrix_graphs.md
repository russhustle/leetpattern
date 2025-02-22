---
comments: True
---

# Matrix Graphs

## 200. Number of Islands

-  [LeetCode](https://leetcode.com/problems/number-of-islands/) | [LeetCode CH](https://leetcode.cn/problems/number-of-islands/) (Medium)

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

=== "Python"

    ```python
    --8<-- "0200_number_of_islands.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0200_number_of_islands.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0200_number_of_islands.ts"
    ```

## 1020. Number of Enclaves

-  [LeetCode](https://leetcode.com/problems/number-of-enclaves/) | [LeetCode CH](https://leetcode.cn/problems/number-of-enclaves/) (Medium)

=== "Python"

    ```python
    --8<-- "1020_number_of_enclaves.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/1020_number_of_enclaves.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/1020_number_of_enclaves.ts"
    ```

## 1254. Number of Closed Islands

-  [LeetCode](https://leetcode.com/problems/number-of-closed-islands/) | [LeetCode CH](https://leetcode.cn/problems/number-of-closed-islands/) (Medium)

=== "Python"

    ```python
    --8<-- "1254_number_of_closed_islands.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/1254_number_of_closed_islands.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/1254_number_of_closed_islands.ts"
    ```

## 695. Max Area of Island

-  [LeetCode](https://leetcode.com/problems/max-area-of-island/) | [LeetCode CH](https://leetcode.cn/problems/max-area-of-island/) (Medium)

=== "Python"

    ```python
    --8<-- "0695_max_area_of_island.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0695_max_area_of_island.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0695_max_area_of_island.ts"
    ```

## 417. Pacific Atlantic Water Flow

-  [LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [LeetCode CH](https://leetcode.cn/problems/pacific-atlantic-water-flow/) (Medium)

=== "Python"

    ```python
    --8<-- "0417_pacific_atlantic_water_flow.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0417_pacific_atlantic_water_flow.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0417_pacific_atlantic_water_flow.ts"
    ```
