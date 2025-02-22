---
comments: True
---

# Amazon

## 1. Two Sum

-   Return the indices of the two numbers such that they add up to a specific target.

| Approach | Time Complexity | Space Complexity |
| -------- | --------------- | ---------------- |
| Hashmap  | O(n)            | O(n)             |

=== "Python"

    ```python
    --8<-- "0001_two_sum.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0001_two_sum.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0001_two_sum.ts"
    ```

## 146. LRU Cache

-   Design and implement a data structure for **Least Recently Used (LRU) cache**. It should support the following operations: get and put.

![146](https://miro.medium.com/v2/resize:fit:650/0*fOwBd3z0XtHh7WN1.png){width=300px}

-   Data structure
    -   Doubly Linked List: to store the key-value pairs.
    -   Hash Map: to store the key-node pairs.

=== "Python"

    ```python
    --8<-- "0146_lru_cache.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0146_lru_cache.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0146_lru_cache.ts"
    ```

## 200. Number of Islands

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
