---
comments: true
---

# Graph - Minimum Spanning Tree (MST)

## Minimum Spanning Tree

-   **Tree**: a connected acyclic graph
-   **Spanning Tree**: a subgraph that is a tree and connects all the vertices together
-   **Minimum Spanning Tree (MST)**: a spanning tree with the minimum possible sum of edge weights
-   Algorithm

    -   Prim's Algorithm
        -   Data Structure: Heap
        -   Time Ciomplexity: $O(E \log V)$
        -   Space Complexity: $O(V + E)$
    -   Kruskal's Algorithm
        -   Union Find
        -   Time Complexity: $O(E \log V)$
        -   Space Complexity: $O(V + E)$

-   Demonstration

Example graph

![mst1](../imgs/mst_1.png)

MST

![mst2](../imgs/mst_2.png)

```python title="template/graph_mst.py"
--8<-- "template/graph_mst.py"
```

## LeetCode Problems

1. 1584 - [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) (Medium)
2. 1135 - [Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) (Medium)
3. 1168 - [Optimize Water Distribution in a Village](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) (Hard)
4. 1489 - [Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) (Hard)
5. 1631 - [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) (Medium)
6. 1579 - [Remove Max Number of Edges to Keep Graph Fully Traversable](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) (Hard)

## 1584. Min Cost to Connect All Points

```python
--8<-- "1584_min_cost_to_connect_all_points.py"
```

## 1135. Connecting Cities With Minimum Cost

```python
--8<-- "1135_connecting_cities_with_minimum_cost.py"
```

## 1168. Optimize Water Distribution in a Village

```python
--8<-- "1168_optimize_water_distribution_in_a_village.py"
```

## 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

```python
--8<-- "1489_find_critical_and_pseudo_critical_edges_in_minimum_spanning_tree.py"
```

## 1631. Path With Minimum Effort

```python
--8<-- "1631_path_with_minimum_effort.py"
```

## 1579. Remove Max Number of Edges to Keep Graph Fully Traversable

-   Return the maximum number of edges you can remove so that the graph remains fully traversable.

![1579](../imgs/1579.png){width=200px}

```python
--8<-- "1579_remove_max_number_of_edges_to_keep_graph_fully_traversable.py"
```
