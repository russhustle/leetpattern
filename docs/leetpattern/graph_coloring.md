---
comments: True
---

# Graph Coloring

## 785. Is Graph Bipartite?

-   Determine if a graph is bipartite.

How to group

|          | Uncolored | Color 1 | Color 2 | Operation   |
| -------- | --------- | ------- | ------- | ----------- |
| Method 1 | -1        | 0       | 1       | `1 - color` |
| Method 2 | 0         | 1       | -1      | `-color`    |

=== "Python"

    ```python
    --8<-- "0785_is_graph_bipartite.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0785_is_graph_bipartite.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0785_is_graph_bipartite.ts"
    ```

## 886. Possible Bipartition

-   Determine if a graph can be divided into two groups such that no two nodes of the same group are connected.

=== "Python"

    ```python
    --8<-- "0886_possible_bipartition.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0886_possible_bipartition.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0886_possible_bipartition.ts"
    ```

## 924. Minimize Malware Spread

=== "Python"

    ```python
    --8<-- "0924_minimize_malware_spread.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0924_minimize_malware_spread.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0924_minimize_malware_spread.ts"
    ```
