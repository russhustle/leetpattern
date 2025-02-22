---
comments: True
---

# MST

## 1135. Connecting Cities With Minimum Cost

-  [LeetCode](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) | [LeetCode CH](https://leetcode.cn/problems/connecting-cities-with-minimum-cost/) (Medium)

=== "Python"

    ```python
    --8<-- "1135_connecting_cities_with_minimum_cost.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/1135_connecting_cities_with_minimum_cost.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/1135_connecting_cities_with_minimum_cost.ts"
    ```

## 1584. Min Cost to Connect All Points

-  [LeetCode](https://leetcode.com/problems/min-cost-to-connect-all-points/) | [LeetCode CH](https://leetcode.cn/problems/min-cost-to-connect-all-points/) (Medium)

-   **Tree**: a connected acyclic graph
-   **Spanning Tree**: a subgraph that is a tree and connects all the vertices together
-   **Minimum Spanning Tree (MST)**: a spanning tree with the minimum possible sum of edge weights
-   Prim's Algorithm
    -   Data Structure: Heap
    -   Time Complexity: O(E \* logV)
    -   Space Complexity: O(V + E)
-   Kruskal's Algorithm

    -   Union Find
    -   Time Complexity: O(E \* logV)
    -   Space Complexity: O(V + E)

-   Demonstration

Example graph

![mst1](../assets/mst_1.png)

MST

![mst2](../assets/mst_2.png)

=== "Python"

    ```python
    --8<-- "1584_min_cost_to_connect_all_points.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/1584_min_cost_to_connect_all_points.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/1584_min_cost_to_connect_all_points.ts"
    ```

## 1168. Optimize Water Distribution in a Village

-  [LeetCode](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) | [LeetCode CH](https://leetcode.cn/problems/optimize-water-distribution-in-a-village/) (Hard)

![1168_0](../assets/1168_0.png)

![1168_1](../assets/1168_1.png)

=== "Python"

    ```python
    --8<-- "1168_optimize_water_distribution_in_a_village.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/1168_optimize_water_distribution_in_a_village.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/1168_optimize_water_distribution_in_a_village.ts"
    ```

## 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

-  [LeetCode](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) | [LeetCode CH](https://leetcode.cn/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) (Hard)

=== "Python"

    ```python
    --8<-- "1489_find_critical_and_pseudo_critical_edges_in_minimum_spanning_tree.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/1489_find_critical_and_pseudo_critical_edges_in_minimum_spanning_tree.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/1489_find_critical_and_pseudo_critical_edges_in_minimum_spanning_tree.ts"
    ```
